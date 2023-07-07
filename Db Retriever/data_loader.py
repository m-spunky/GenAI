import langchain.document_loaders as loader

data = loader.TextLoader('Db Retriever/document.txt')
data = data.load()
print(data)
