import os
from dotenv import load_dotenv

load_dotenv()

# API KEY
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# FILE PATHS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRANSCRIPTS_PATH = os.path.join(BASE_DIR, "data", "transcripts")
RESULTS_FILE = os.path.join(BASE_DIR, "data", "results.xlsx")