from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# Equivalent to SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

with open('Db Retriever/document.txt') as f:
    file = f.read()


query_result = embeddings.embed_query(file)

print(query_result)
