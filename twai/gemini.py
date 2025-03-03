import google.generativeai as genai
from environs import Env

env = Env()
env.read_env()
key = env("TOKEN")

# Gemini API
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Function to prompt
def prompt(content):
    message = (
    "Rules: keeping exactly the structure words, semantic and lexical context"
    "Make: Translate tweets to english"
    f"Message: {content}")

    response = model.generate_content([message])
    return response.text