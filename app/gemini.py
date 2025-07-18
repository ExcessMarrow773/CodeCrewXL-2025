from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()
chat = client.chats.create(model="gemini-2.0-flash")

while True:
    message = input("> ")
    if message == "exit":
        break
    response = chat.send_message(message)
    print(response.text)