from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    candidate: str
    role: str
    transcript: str