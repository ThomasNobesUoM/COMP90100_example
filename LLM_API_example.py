import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv(("OPENAI_API_KEY"))

if not api_key:
    raise ValueError("API key not found. check your .env file")
else:
    print("API key found and looks good so far!")
   
# Step 5: Define the API endpoints and headers 
API_URL = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

assistant_role = "You are a helpful assistant that explains concepts clearly." # instructs the LLM how to respond
user_question = "Explain what an API is in one sentence." # could ask as input() instead

# Step 6: Construct the request body
payload = {
    "model": "gpt-4o-mini",
    "messages":
        [
            {
                "role": "system",
                "content": assistant_role
            },
            {
                "role": "user",
                "content": user_question
            }
        ],
    "temperature": 0.3,
    "max_tokens": 50
}

# Step 7: send the request
response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code != 200:
    print("Request failed with status code:", response.status_code)
    print(response.text)
    exit()

# Step 8: Parse and print the LLM response
data = response.json()

print("*"*50, "\nFull response:")
print(data)

generated_text = data["choices"][0]["message"]["content"]

print("Model response:")
print(generated_text)
