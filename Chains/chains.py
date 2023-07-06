from langchain.schema import (AIMessage,HumanMessage,SystemMessage)
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI



bot = ChatOpenAI(model="gpt-3.5-turbo")
# PREDETERMINED KNOWLEDGE FOR MODEL - 1
context = [
    # SystemMessage provides context to the model that it will reference for each completion.
    SystemMessage(content="You are an expert data scientist with an expertise in building deep learning models."),
    # The HumanMessage refers to prompt.
    HumanMessage(content="Explain the concept of autoencoder in a couple of lines")
]
result = bot(context)





# PREDETRMINED KNOWLEDGE FOR MODEL - 2
template = """
You are an expert data scientist with an expertise in building deep learning models. 
Explain the concept of {concept} in a couple of lines
"""
prompt = PromptTemplate(
    input_variables=["concept"],
    template=template,
)
chain = LLMChain(
    model = OpenAI(model="text-ada-001"),
    prompt = prompt    
)
result = chain.run("autoencoder")



# PIPELINE FOR MODELS

template1 = """
You are an expert data scientist with an expertise in building deep learning models. 
Explain the concept of {concept} in a couple of lines
"""
prompt1 = PromptTemplate(
    input_variables=["concept"],
    template=template,
)
chain1 = LLMChain(
    model = OpenAI(model="text-ada-001"),
    prompt = prompt1    
)



template2 = """
Describe this {concept_desc} tom me like i'm five. 
"""
prompt2 = PromptTemplate(
    input_variables=["concept_desc"],
    template=template,
)
chain2 = LLMChain(
    model = OpenAI(model="text-ada-001"),
    prompt = prompt2    
)

# SEQUENTIAL EXECUTION OF CHAINS
from langchain.chains import SimpleSequentialChain
pipeline = SimpleSequentialChain(chains=[chain1,chain2],verbose=True)
result = pipeline.run("autoencoder")


# VECTOR EMBEDDING
from langchain.text_splitter import RecursiveCharacterTextSplitter
ts = RecursiveCharacterTextSplitter(chunk_size=100)

