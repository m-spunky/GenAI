import langchain.document_loaders as loader
import langchain.text_splitter as transformer
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS

class DBR:
    def __init__(self,file_path):
        self.file = file_path
        with open('Db Retriever/document.txt') as f:
            self.docs = f.read()


    def load_data(self):
        data = loader.TextLoader(self.file)
        data = data.load()
        return data


    def transform_data(self,chunk_s=30,chunk_o=0):
        splitter = transformer.CharacterTextSplitter(
            separator=".",
            chunk_size = chunk_s,
            chunk_overlap=chunk_o
        )
        loaded_data = self.load_data()[0].page_content
        transform_data = splitter.create_documents([loaded_data])
        return transform_data
    

    def embed_data(self,model="all-MiniLM-L6-v2",):
        embeddings = HuggingFaceEmbeddings(model_name=model)
        #SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

        embedding_doc = embeddings.embed_query(self.docs)

        return embedding_doc
    
    def store_data(self,doc=None):
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        if doc == None:
            document = self.transform_data(chunk_s=80,chunk_o=10)
        else:
            document = doc

        db = FAISS.from_documents(document, embeddings)
        return db

    def search_data(self,query,db):
        similar_query = db.similarity_search(query)
        return similar_query

# db = DBR("Db Retriever/essay.txt")
# db_sd = db.store_data()
# print(db.embed_data())
# print(db.search_data('communication',db_sd))

