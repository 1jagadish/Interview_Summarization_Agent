from pydantic import BaseModel

<<<<<<< HEAD

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
=======
class AnalyzeRequest(BaseModel):
    candidate: str
    role: str
    transcript: str
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e
