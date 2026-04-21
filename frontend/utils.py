import os

# Absolute path fix
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TRANSCRIPT_PATH = os.path.join(BASE_DIR, "data", "transcripts")


def load_transcripts():
    transcripts = {}

    if not os.path.exists(TRANSCRIPT_PATH):
        return transcripts

    files = os.listdir(TRANSCRIPT_PATH)

    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(TRANSCRIPT_PATH, file), "r", encoding="utf-8") as f:
                key = file.replace(".txt", "").replace("_", " ").title()
                transcripts[key] = f.read()

    return transcripts