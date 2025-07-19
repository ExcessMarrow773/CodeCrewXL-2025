# filepath: [gemini.py](http://_vscodecontentref_/1)
from google import genai

client = genai.Client(api_key="AIzaSyDRQcTgr7SEhBu7Pnykm5KE4IURvVXIOjQ")  # <-- Add your API key here

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="",
    
)
print(response.text)