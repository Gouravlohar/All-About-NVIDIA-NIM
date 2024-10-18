import requests
import base64
from dotenv import load_dotenv
import os
import time
load_dotenv()

invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-3-medium"


api_key = os.getenv('STABLE_DIFFUSION_API')

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/json",
}

payload = {
    "prompt": input("Enter Your Image Prompt Here: "),
    "cfg_scale": 5,
    "aspect_ratio": "16:9",
    "seed": 0,
    "steps": 50,
    "negative_prompt": ""
}


start_time = time.time()

response = requests.post(invoke_url, headers=headers, json=payload)


end_time = time.time()

response.raise_for_status()
response_body = response.json()
image_data = response_body.get('image')

if image_data:
    image_bytes = base64.b64decode(image_data)
    with open('generated_image.png', 'wb') as image_file:
        image_file.write(image_bytes)
    print("Image saved as 'generated_image.png'")
else:
    print("No image data found in the response")

response_time = end_time - start_time
print(f"Response time: {response_time} seconds")