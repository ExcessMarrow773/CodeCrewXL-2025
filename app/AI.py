import os
from google import genai
from transformers import pipeline
from dotenv import load_dotenv
from timer import timer


class AI:
    def __init__(self):
        load_dotenv()
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    @timer('generate_gemini_content', 'ms')
    def generate_gemini_content(self, context, prompt):
        client = genai.Client(api_key='AIzaSyDRQcTgr7SEhBu7Pnykm5KE4IURvVXIOjQ')

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=context + "\n" + prompt,
        )

        return response
    @timer('sentiment_analysis', 'ms')
    def sentiment_analysis(self, data):

        sentiment_pipeline = pipeline(model="nlptown/bert-base-multilingual-uncased-sentiment")
        data = ["I love you", "I hate you"]
        
        return sentiment_pipeline(data)
    
    
if __name__ == "__main__":
    ai_version = True 
    if ai_version == False:
        ai = AI()
        data = ["I love you", "I hate you"]
        print(ai.sentiment_analysis(data))
    if ai_version == True:
        ai = AI()
        context = ""
        prompt = "Hi AI''"
        print(ai.generate_gemini_content(context, prompt).text)

