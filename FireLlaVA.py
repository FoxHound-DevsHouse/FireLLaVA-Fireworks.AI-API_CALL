import requests
import json

base64code = "MY_BASE_64 CODE"

url = "https://api.fireworks.ai/inference/v1/chat/completions"
payload = {
  "model": "accounts/fireworks/models/firellava-13b",
  "max_tokens": 512,
  "top_p": 1,
  "top_k": 40,
  "presence_penalty": 0,
  "frequency_penalty": 0,
  "temperature": 0.6,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Explain this in detail i am a novice in machine learning "
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/jpeg;base64," + base64code
          }
        }
      ]
    }
  ]
}
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": "Bearer <MY_API_KEY>"
}
response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
llm_response = response.json()['choices'][0]['message']['content'].replace('\n', '')
print(llm_response)
