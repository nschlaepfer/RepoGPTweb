from flask import Flask, render_template, send_from_directory, request, jsonify
import os
from dotenv import load_dotenv
from git_operations import clone_repo
from code_processing import split_code_into_chunks, process_file_with_openai
from embedding_generation import generate_embeddings
from pinecone_operations import upload_to_pinecone
from tqdm import tqdm
import time
import shutil

app = Flask(__name__)
load_dotenv()  # take environment variables from .env.

code_file_extensions = [".py", ".html", ".js", ".css", ".c", ".cpp", ".java", ".go", ".rs", ".rb", ".php", ".swift", ".kt", ".ts", ".scala", ".cs", ".sh", ".r", ".m", ".f", ".pl", ".asm", ".sql", ".s", ".p", ".clj", ".hs", ".lua", ".pas", ".dart", ".groovy", ".julia", ".raku", ".ada", ".cob", ".d", ".elm", ".erl", ".f#", ".haskell", ".kotlin", ".lisp", ".perl", ".rust", ".scala", ".scheme", ".shell", ".typescript", ".vba", ".vb", ".xml", ".yaml", ".json"]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            repo_link = request.form.get('repo_link')
            user_choice = request.form.get('user_choice')
            pinecone_api_key = request.form.get('pinecone_api_key')
            open_api_key = request.form.get('openai_api_key')

            if not pinecone_api_key:
                pinecone_api_key = os.getenv('PINECONE_API_KEY')
            if not open_api_key:
                open_api_key = os.getenv('OPEN_API_KEY')

            directory = clone_repo(repo_link)

            result_text = ""

            if user_choice in ['1', '3']:
                embeddings = generate_embeddings(directory)
                upload_to_pinecone(embeddings, pinecone_api_key)
                result_text += "Embeddings generated and uploaded to Pinecone.\n"

            readme_files = []
            if user_choice in ['2', '3']:
                for subdir, dirs, files in os.walk(directory):
                    for file in files:
                        filepath = subdir + os.sep + file
                        if any(filepath.endswith(ext) for ext in code_file_extensions):
                            try:
                                readme_path = process_file_with_openai(filepath, "3.5-turbo-16k")
                                readme_files.append(readme_path)
                            except UnicodeDecodeError:
                                return jsonify({"error": f'Error processing file: {filepath}'})

            result_text += "Files processed and commented.\n"

            # Create a zip file of the processed files
            zip_file_path = os.path.join(app.root_path, "processed_files")
            shutil.make_archive(zip_file_path, 'zip', directory)
            print(f"Zip file created at {zip_file_path}.zip")

            return jsonify({'result': result_text, 'readme_files': readme_files})
        except Exception as e:
            return jsonify({"error": str(e)})

    return render_template('home.html')

@app.route('/download', methods=['GET'])
def download_files():
    directory = app.root_path  # Use Flask's root path
    filename = 'processed_files.zip'
    file_path = os.path.join(directory, filename)
    print(f"Directory: {directory}")
    print(f"Files in directory: {os.listdir(directory)}")
    print(f"Attempting to download file at {file_path}")
    if os.path.exists(file_path):
        return send_from_directory(directory, filename, as_attachment=True)
    else:
        return "File not found", 404

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        repo_link = data['repoLink']
        user_choice = data['userChoice']
        pinecone_api_key = data['pineconeApiKey'] or os.getenv('PINECONE_API_KEY')
        open_api_key = data['openaiApiKey'] or os.getenv('OPEN_API_KEY')

        directory = clone_repo(repo_link)

        result_text = ""

        if user_choice in ['1', '3']:
            embeddings = generate_embeddings(directory)
            upload_to_pinecone(embeddings, pinecone_api_key)
            result_text += "Embeddings generated and uploaded to Pinecone.\n"

        readme_files = []
        if user_choice in ['2', '3']:
            for subdir, dirs, files in os.walk(directory):
                for file in files:
                    filepath = subdir + os.sep + file
                    if any(filepath.endswith(ext) for ext in code_file_extensions):
                        try:
                            readme_path, comments = process_file_with_openai(filepath, "3.5-turbo-16k")
                            readme_files.append(readme_path)
                        except UnicodeDecodeError:
                            return jsonify({"error": f'Error processing file: {filepath}'})

            result_text += "Files processed and commented.\n"

        return jsonify({'result': result_text, 'readme_files': readme_files, 'comments': comments})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
