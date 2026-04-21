from pydantic import BaseModel


# ===== INPUT SCHEMA =====
class AnalyzeRequest(BaseModel):
    candidate: str
    role: str
    transcript: str


# ===== OUTPUT SCHEMA (optional but good) =====
class AnalyzeResponse(BaseModel):
    Candidate: str
    Role: str
    Summary: str
    Strengths: str
    Weaknesses: str
    Recommendation: str