import requests
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual OpenRouter API Key
API_KEY = "API_KEY"

# Valid free model
MODEL = "deepseek/deepseek-chat-v3-0324:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Start with system message
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

print("🤖 OpenRouter CLI Chatbot. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": 512,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        print(f"🤖: {reply.strip()}\n")
        messages.append({"role": "assistant", "content": reply})
    else:
        print(f"❌ Error {response.status_code}: {response.text}\n")
