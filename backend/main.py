from fastapi import FastAPI
from backend.langgraph_agent import run_agent
from backend.excel_utils import save_to_excel, read_excel
from backend.schemas import AnalyzeRequest

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Backend running 🚀"}


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