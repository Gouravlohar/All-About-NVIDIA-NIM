from openai import OpenAI
from dotenv import load_dotenv
import os
import time
load_dotenv()

llama_api_key = os.getenv('NVIDIA_API_KEY')

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = llama_api_key)

user_input = input("What you want to ask: ")

start_time = time.time()

completion = client.chat.completions.create(
  model="meta/llama-3.2-3b-instruct",
  messages=[{"role":"user","content":user_input}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

end_time = time.time()

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

response_time = end_time - start_time
print(f"\nResponse time: {response_time} seconds")