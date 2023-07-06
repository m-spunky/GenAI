import openai

openai.api_key = "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"


prompt = "Your Name ?" 
# Prompts = "INSTRUCTION : (if this then this or that)
#            DATA:         (content req for query)
#            QUESTION:     (proper question)
#            ANSWER :      (format of answer)
# "

result = openai.Completion.create(engine ="text-ada-001",
                          prompt=prompt,
                          max_tokens=5
                          )

# model
# ID of the model to use. You can use the List models API to see all of your available models, or see our Model overview for descriptions of them.

# prompt
# The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.

# suffix
# The suffix that comes after a completion of inserted text.

# max_tokens
# Defaults to 16
# The maximum number of tokens to generate in the completion.

# temperature
# Defaults to 1 Range : 0-2
# Randomness of word choosing , if 0 , then select that token which is most probable


# top_p
# Defaults to 1 (==100%)
# An alternative to sampling with temperature, called nucleus sampling, 
# Percentage of tokens taking into account for selection when temperature chnges.

# n 
# Default to 1
# How many completions to generate for each prompt.


# stream
# Defaults to false
# Whether to stream back partial progress. If set, tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a data: [DONE] message. Example Python code.


# logprobs 
# Include the log probabilities on the logprobs most likely tokens, as well the chosen tokens. For example, if logprobs is 5, the API will return a list of the 5 most likely tokens. The API will always return the logprob of the sampled token, so there may be up to logprobs+1 elements in the response.


# echo
# Defaults to false
# Echo back the prompt in addition to the completion

# stop
# Up to 4 sequences where the API will stop generating further tokens. 
# The returned text will not contain the stop sequence.

# presence_penalty
# Number between -2.0 and 2.0. 
# Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

# frequency_penalty
# Number between -2.0 and 2.0. 
# Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

# logit_bias
# Defaults to null
# Modify the likelihood of specified tokens appearing in the completion. Specifying the bias for tokens

print(result["choices"][0]['text'].strip())
# {
#   "id": "cmpl-7ZHUS5kQaCcpbA1ozG9i8tKqLulS4",
#   "object": "text_completion",
#   "created": 1688643068,
#   "model": "text-ada-001",
#   "choices": [
#     {
#       "text": "\n\nMy Name is phonetically mispelled as",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "length"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 5,
#     "completion_tokens": 10,
#     "total_tokens": 15
#   }
# }