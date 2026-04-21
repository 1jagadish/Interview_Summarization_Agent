import pandas as pd
import os
<<<<<<< HEAD

# IMPORT FROM CONFIG
=======
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e
from config.settings import RESULTS_FILE

FILE = RESULTS_FILE


<<<<<<< HEAD
# ===== SAVE DATA =====
def save_to_excel(data):

=======
def save_to_excel(data):

    os.makedirs("data", exist_ok=True)

>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e
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


<<<<<<< HEAD
# ===== LOAD DATA =====
=======
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e
def read_excel():

    if os.path.exists(FILE):
        df = pd.read_excel(FILE)
        return df.to_dict(orient="records")

    return []