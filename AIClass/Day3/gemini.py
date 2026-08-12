from google import genai
import os

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is the indefinite integral of x/(x+1)?"
)

print(response.text)