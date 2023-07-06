from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = "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"

# PIPELINE FOR MODELS

template1 = """
You are an expert data scientist with an expertise in building deep learning models. 
Explain the concept of {concept} in a couple of lines
"""
# template1 = "{concept}"
prompt1 = PromptTemplate(
    input_variables=["concept"],
    template=template1,
)
chain1 = LLMChain(
    llm = OpenAI(model_name="text-davinci-003"),
    prompt = prompt1    
)


template2 = """
Name a process : {concept_desc}  
"""
# template2 = """
# count words in {concept_desc}   
# """
prompt2 = PromptTemplate(
    input_variables=["concept_desc"],
    template=template2,
)
chain2 = LLMChain(
    llm = OpenAI(model_name="text-davinci-003"),
    prompt = prompt2    
)

# SEQUENTIAL EXECUTION OF CHAINS
from langchain.chains import SimpleSequentialChain
pipeline = SimpleSequentialChain(chains=[chain1,chain2],verbose=True)
result = pipeline.run("vector")
print(result)