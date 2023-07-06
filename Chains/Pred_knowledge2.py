from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

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

