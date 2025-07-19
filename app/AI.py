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

        sentiment_pipeline = pipeline(modzael="nlptown/bert-base-multilingual-uncased-sentiment")
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

from django.shortcuts import render
from app.models import Post
from app.AI import AI

def ai(request):
    ai_response = ""
    user_prompt = ""
    formatted_posts = ""
    if request.user.is_authenticated:
        # Only get posts by the current user
        posts = Post.objects.filter(author=request.user.username)
        for post in posts:
            formatted_posts += f'Title:"{post.title}" Body:"{post.body}" IMG:"{post.image.url if post.image else ""}"\n'

    if request.method == "POST":
        user_prompt = request.POST.get("prompt", "")
        # Combine user's posts and their prompt
        full_prompt = f"{formatted_posts}\n{user_prompt}"
        ai_instance = AI()
        response = ai_instance.generate_gemini_content("", full_prompt)
        ai_response = response.text

    return render(request, "app/ai_page.html", {
        "ai_response": ai_response,
        "user_prompt": user_prompt
    })