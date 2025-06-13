import time

from ollama import Client

time.sleep(3)

model = 'gemma3:1b'

client = Client(
    host='http://ollama:11434',
)

client.pull(model=model)

system_prompt = 'You are a helpful AI assisstant.'
user_input = 'Who are you?'

# response = client.generate(model=model, prompt='Hello')
response = client.chat(
    model=model,
    messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_input},
    ],
    options={'temperature': 0.5, 'top_p': 0.95, 'top_k': 20},
)

print(response.message.content)
