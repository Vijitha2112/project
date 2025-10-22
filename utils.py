import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use gemini-2.5-flash model directly
MODEL_NAME = "gemini-2.5-flash"

def generate_recipe(ingredients):
    prompt = f"""
    You are a professional chef. Create a detailed recipe using the following ingredients:
    {ingredients}.
    Include:
    1. Recipe name
    2. Short description
    3. List of ingredients with measurements
    4. Step-by-step cooking instructions
    5. Optional: Serving suggestions
    """

    # Create a generative model instance with gemini-2.5-flash
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)

    return response.text.strip() if response else "Sorry, I couldn't generate a recipe."
