import os
from dotenv import load_dotenv

<<<<<<< HEAD
load_dotenv()

# API KEY
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# FILE PATHS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRANSCRIPTS_PATH = os.path.join(BASE_DIR, "data", "transcripts")
RESULTS_FILE = os.path.join(BASE_DIR, "data", "results.xlsx")
=======
# Load .env
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Excel file path
RESULTS_FILE = "data/results.xlsx"

# Debug print (optional)
print("API KEY LOADED:", GEMINI_API_KEY[:10] if GEMINI_API_KEY else "NOT FOUND")
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e
