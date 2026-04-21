import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Excel file path
RESULTS_FILE = "data/results.xlsx"

# Debug print (optional)
print("API KEY LOADED:", GEMINI_API_KEY[:10] if GEMINI_API_KEY else "NOT FOUND")