from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
document = "In Learning Transferable Visual Models From Natural Language Supervision paper, OpenAI introduces their new model which is called CLIP, for Contrastive Language-Image Pre-training. In a nutshell, this model learns the relationship between a whole sentence and the image it describes.The important thing here is that it is trained on full sentences instead of single classes like car, dog, etc. The intuition is that when trained on whole sentences, the model can learn a lot more things and finds some pattern between images and texts"
 

db = FAISS.from_documents(document, embeddings)
print(db)

# Search by query
query = "Contraceptive Language"
docs = db.similarity_search(query)
print(docs)

# Search by vector
# vector = embeddings[3]
# docs = db.similarity_search_by_vector(vector)
# print(docs)