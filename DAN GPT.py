import openai
openai.api_key = "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"
model_engine = "text-davinci-002"
prompt = input("Hi, I'm your new OpenAI App with DAN Mode enabled. Ask me anything!")
completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2048,)
response = completions.choices[0].text
print(response)
