from fastapi import FastAPI
<<<<<<< HEAD
from langgraph_agent import run_agent
from excel_utils import save_to_excel, read_excel
from schemas import AnalyzeRequest
=======
from backend.langgraph_agent import run_agent
from backend.excel_utils import save_to_excel, read_excel
from backend.schemas import AnalyzeRequest
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e

app = FastAPI()


<<<<<<< HEAD
=======
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}


>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e
@app.post("/analyze")
def analyze(data: AnalyzeRequest):

    result = run_agent(data.transcript)

    output = {
        "Candidate": data.candidate,
        "Role": data.role,
        "Summary": result["summary"],
        "Strengths": result["strengths"],
        "Weaknesses": result["weaknesses"],
        "Recommendation": result["recommendation"]
    }

    save_to_excel(output)

    return output


@app.get("/results")
def get_results():
    return read_excel()