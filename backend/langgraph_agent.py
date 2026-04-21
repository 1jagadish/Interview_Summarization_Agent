from langgraph.graph import StateGraph, END
from typing import TypedDict
from google import genai
from config.settings import GEMINI_API_KEY

# ===== INIT CLIENT =====
client = genai.Client(api_key=GEMINI_API_KEY)

# ===== STATE =====
class State(TypedDict):
    transcript: str
    summary: str
    strengths: str
    weaknesses: str
    recommendation: str


# ===== LLM CALL =====
def call_llm(prompt):
    try:
        response = client.models.generate_content(
            model="models/gemini-1.5-flash",   # ✅ CHANGE HERE
            contents=prompt
        )

        return response.candidates[0].content.parts[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# ===== AGENTS =====

def summary_agent(state):
    prompt = f"""
Summarize the interview in 5–6 professional lines.

Transcript:
{state['transcript']}
"""
    return {"summary": call_llm(prompt)}


def strengths_agent(state):
    prompt = f"""
List key strengths in bullet points.

Transcript:
{state['transcript']}
"""
    return {"strengths": call_llm(prompt)}


def weaknesses_agent(state):
    prompt = f"""
List weaknesses or areas of improvement.

Transcript:
{state['transcript']}
"""
    return {"weaknesses": call_llm(prompt)}


def recommendation_agent(state):
    prompt = f"""
Based on the interview, give ONLY one:
Best Fit / Good Fit / Partial Fit

Transcript:
{state['transcript']}
"""
    return {"recommendation": call_llm(prompt)}


# ===== GRAPH =====
def run_agent(transcript):

    graph = StateGraph(State)

    graph.add_node("summary", summary_agent)
    graph.add_node("strengths", strengths_agent)
    graph.add_node("weaknesses", weaknesses_agent)
    graph.add_node("recommendation", recommendation_agent)

    graph.set_entry_point("summary")

    graph.add_edge("summary", "strengths")
    graph.add_edge("strengths", "weaknesses")
    graph.add_edge("weaknesses", "recommendation")
    graph.add_edge("recommendation", END)

    app = graph.compile()

    return app.invoke({
        "transcript": transcript,
        "summary": "",
        "strengths": "",
        "weaknesses": "",
        "recommendation": ""
    })