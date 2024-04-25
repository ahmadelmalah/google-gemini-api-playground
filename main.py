# Initalization
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
genai.configure(api_key=os.environ.get("api_key"))


# Create a new model
model = genai.GenerativeModel("gemini-1.0-pro-latest")
response = model.generate_content("The opposite of hot is")
print(response.text)
