import pandas as pd
import os

# IMPORT FROM CONFIG
from config.settings import RESULTS_FILE

FILE = RESULTS_FILE


# ===== SAVE DATA =====
def save_to_excel(data):

    if os.path.exists(FILE):
        df = pd.read_excel(FILE)
    else:
        df = pd.DataFrame(columns=[
            "Candidate",
            "Role",
            "Summary",
            "Strengths",
            "Weaknesses",
            "Recommendation"
        ])

    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_excel(FILE, index=False)


# ===== LOAD DATA =====
def read_excel():

    if os.path.exists(FILE):
        df = pd.read_excel(FILE)
        return df.to_dict(orient="records")

    return []