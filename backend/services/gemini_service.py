import os
import time
import logging
from typing import Optional

import google.generativeai as genai
from dotenv import load_dotenv


# ==============================
# LOAD ENV VARIABLES
# ==============================
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in environment variables.")


# ==============================
# CONFIGURE GEMINI
# ==============================
genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-flash"

model = genai.GenerativeModel(MODEL_NAME)


# ==============================
# LOGGING SETUP
# ==============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ==============================
# CORE GENERATION FUNCTION
# ==============================
def generate_response(
    prompt: str,
    max_retries: int = 3,
    delay: float = 1.5
) -> str:
    """
    Calls Gemini API with retry logic.

    Args:
        prompt (str): Input prompt
        max_retries (int): retry attempts
        delay (float): delay between retries

    Returns:
        str: LLM response text
    """

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"🔄 Gemini API Call Attempt {attempt}")

            response = model.generate_content(prompt)

            if not response or not response.text:
                raise ValueError("Empty response from Gemini")

            return response.text.strip()

        except Exception as e:
            logger.error(f"❌ Error on attempt {attempt}: {str(e)}")

            if attempt == max_retries:
                return f"Error: Failed after {max_retries} attempts → {str(e)}"

            time.sleep(delay)


# ==============================
# OPTIONAL: STRUCTURED RESPONSE
# ==============================
def generate_json_response(prompt: str) -> Optional[dict]:
    """
    Forces LLM to return JSON safely.

    Returns parsed dictionary if possible.
    """
    import json

    raw_output = generate_response(prompt)

    try:
        return json.loads(raw_output)
    except Exception:
        logger.warning("⚠️ JSON parsing failed. Returning raw output.")
        return {"raw_output": raw_output}