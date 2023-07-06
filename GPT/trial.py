# from Utils.utils4 import Utils4GPT



# prompt = r"Microsoft Windows [Version 10.0.19045.3086](c) Microsoft Corporation. All rights reserved.C:\Users\HP-PC\Desktop\Spunky\GITHUB\Generative AI>C:/Users/HP-PC/AppData/Local/Programs/Python/Python38/python.exec:/Users/HP-PC/Desktop/Spunky/GITHUB/Generative AI/GPT/trial.pyTraceback (most recent call last):File c:/Users/HP-PC/Desktop/Spunky/GITHUB/Generative AI/GPT/trial.py, line 9, in <module>print(utils.count_token())File c:\Users\HP-PC\Desktop\Spunky\GITHUB\Generative AI\GPT\Utils\utils4.py, line 9, in count_tokentokenizer = tiktoken.get_encoding(encoder)File C:\Users\HP-PC\AppData\Local\Programs\Python\Python38\lib\site-packagesiktokenegistry.py, line 60, in get_encoding"

# model = "text-davinci-001"

# utils = Utils4GPT(prompt,model)
# print(utils.count_token())
# print((len(utils.count_token())))


# result = {
#   "id": "cmpl-7ZHUS5kQaCcpbA1ozG9i8tKqLulS4",
#   "object": "text_completion",
#   "created": 1688643068,
#   "model": "text-ada-001",
#   "choices": [
#     {
#       "text": "\n\nMy Name is phonetically mispelled as",
#       "index": 0,
#       "logprobs": None,
#       "finish_reason": "length"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 5,
#     "completion_tokens": 10,
#     "total_tokens": 15
#   }
# }
# res = result["choices"][0]['text'].strip()
# print(res)