import pandas as pd
import os
from config.settings import RESULTS_FILE

FILE = RESULTS_FILE


def save_to_excel(data):

    os.makedirs("data", exist_ok=True)

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


def read_excel():

    if os.path.exists(FILE):
        df = pd.read_excel(FILE)
        return df.to_dict(orient="records")

    return []