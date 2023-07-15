import pinecone


def upload_to_pinecone(embeddings, index_name, api_key):
    """
    Uploads embeddings to a Pinecone index.

    Args:
        embeddings (list): List of embeddings to upload.
        index_name (str): Name of the Pinecone index.
        api_key (str): Pinecone API key.
    """
    pinecone.init(api_key=api_key)
    index = pinecone.Index(index_name)

    index.upsert(ids=range(len(embeddings)), vectors=embeddings)

    pinecone.deinit()


def retrieve_from_pinecone(query_vector, index_name, api_key, top_k=5):
    """
    Retrieves nearest neighbors from a Pinecone index.

    Args:
        query_vector (list): Vector used as the query.
        index_name (str): Name of the Pinecone index.
        api_key (str): Pinecone API key.
        top_k (int): Number of nearest neighbors to retrieve.

    Returns:
        list: List of nearest neighbor IDs.
    """
    pinecone.init(api_key=api_key)
    index = pinecone.Index(index_name)

    results = index.query(queries=[query_vector], top_k=top_k)
    neighbor_ids = [result.id for result in results[0]]

    pinecone.deinit()

    return neighbor_ids
