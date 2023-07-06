from langchain.llms import OpenAI
from langchain import LLMChain,PromptTemplate,HuggingFaceHub
import os

os.environ['OPENAI_API_KEY'] = "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"


# TEMPLATE BUILDING
question = "your name"
template = """{question} ?""" 
prompt = PromptTemplate(input_variables=["question"],template=template)
print(prompt.format(question=question))

# LLM CHAIN FOR HUGGING FACE
# chain = LLMChain(
#     prompt = prompt,
#     model = HuggingFaceHub(repo_id="google/flan-t5-xl",model_kwargs={"max_tokens":5})
# )


# LLM CHAIN FOR OPENAI
# chain = LLMChain(
#     prompt = prompt,
#     model = OpenAI(model="text-ada-001")
# )



# print(chain.run(question))



