from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

i = 1
memory = ConversationBufferMemory()
while i<3 :
    user = str(input('Me :')[4:])
    bot = ConversationChain(
        llm=OpenAI(model="text-davinci-003",openai_api_key = "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"
,max_tokens=20),
        memory=memory
    )
    ai = bot.predict(input=user)
    print(ai)
    i+=1

print(memory.load_memory_variables({}))
# Me :i live in india.
#  India is a beautiful country. There are many vibrant cultures, delicious cuisines, and rich history
# Me :Whats time now here?
#  The time in India right now is 8:30 PM IST.
# {'history': 'Human: ve in india.\nAI:  India is a beautiful country. There are many vibrant cultures, delicious cuisines, and rich history\nHuman: s time now here?\nAI:  The time in India right now is 8:30 PM IST.'}
