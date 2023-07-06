from langchain.schema import (AIMessage,HumanMessage,SystemMessage)
from langchain.chat_models import ChatOpenAI

bot = ChatOpenAI(model="gpt-3.5-turbo")
# PREDETERMINED KNOWLEDGE FOR MODEL - 1
context = [
    # SystemMessage provides context to the model that it will reference for each completion.
    SystemMessage(content="You are an expert data scientist with an expertise in building deep learning models."),
    # The HumanMessage refers to prompt.
    HumanMessage(content="Explain the concept of autoencoder in a couple of lines")
]
result = bot(context)




