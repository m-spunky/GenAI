class Utils4GPT:
    def __init__(self,prompt,model):
        self.prompt = prompt
        self.model = model
        
    def count_token(self):
        import tiktoken
        try:
            encoder = tiktoken.encoding_for_model(model_name=self.model)
            tokenizer = tiktoken.get_encoding(encoder)
            tokens = tokenizer.encode(self.prompt)
            return tokens
        except ValueError:
            tokenizer = tiktoken.get_encoding("p50k_base")
            tokens = tokenizer.encode(self.prompt)   
            return tokens