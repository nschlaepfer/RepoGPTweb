
# RepoGPT 🚀

## 📌 Overview
**RepoGPT** is an evolving web application crafted to empower users with a swift and comprehensive understanding of a GitHub repository. By harnessing the power of **OpenAI** and **Pinecone**, it delves deep into the code, crafts embeddings, and offers invaluable insights into the repository's architecture and functionality. Users are endowed with a downloadable ZIP file of the scrutinized repository, enriched with a companion guide that elucidates the project's essence and proffers enhancement suggestions.

> 📂 **Snapshot of the Repository**: Your provided repository is a Python-centric project, augmented with HTML and CSS files. It exudes the vibes of a web application, intricately woven with code processing, embedding generation, git operations, and Pinecone interactions.

## 📂 Directory Structure
```
src
│
├── code_processing.py          - Functions for OpenAI code processing
├── embedding_generation.py     - Embedding generation functions
├── git_operations.py           - Repository cloning functions
├── gunicorn.conf.py            - Gunicorn configuration
├── main.py                     - Central Flask application
├── pinecone_operations.py      - Pinecone interaction functions
├── user_interface.py           - User input & validation functions
│
├── templates                   - HTML templates for UI
└── static                      - Static assets (CSS, images, etc.)
```

## 📜 Key Files & Functions
- **code_processing.py**
  - `process_chunk_with_openai` - Processes code chunks via OpenAI
  - `process_file_with_openai` - Processes entire files with OpenAI
  - `split_code_into_chunks` - Divides code into digestible chunks
- **embedding_generation.py**
  - `generate_embeddings` - Crafts embeddings for code or characters
- **git_operations.py**
  - `clone_repo` - Clones a repository using a provided link
- **main.py**
  - Central Flask application with routes for analysis, file downloads, and the homepage
- **pinecone_operations.py**
  - `retrieve_from_pinecone` & `upload_to_pinecone` - Pinecone data operations
- **user_interface.py**
  - Functions for user input acquisition, long-operation handling, and validation

## 🛠 Requirements
The `requirements.txt` file is your key to unlocking the project's dependencies.

## 🚀 How to Run
1. 📦 Clone the repository
2. 🔧 Install dependencies via `requirements.txt`
3. 🌍 Set up environment variables as guided by `.envEXAMPLE`
4. 🚀 Launch the Flask app using Gunicorn or another WSGI server
5. 🌐 Navigate to the web interface using your browser

## 📈 Current Status
The project is in its development phase, with a keen emphasis on crafting README files and embedding comments. Presently, the only operational mode is README generation.

## 🌟 Future Enhancements
- **User-Friendly Interface**: A sleek web interface for seamless navigation.
- **Enhanced Analysis**: Amplified code analysis with improvement suggestions.
- **Service Integration**: Potential amalgamation with diverse platforms for enriched functionality.

## 🤝 Contributing
**RepoGPT** is an emblem of open-source. Your contributions can shape its future. Fork, modify, and submit a pull request!

## 🎯 Conclusion
**RepoGPT** aspires to redefine the interaction between developers and GitHub repositories. By offering profound analysis, insights, and downloadable content, it promises a fresh perspective into the coding realm. Stay tuned for exhilarating updates and features!

