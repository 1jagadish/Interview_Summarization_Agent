from langgraph.graph import StateGraph, END
from typing import TypedDict
<<<<<<< HEAD
import google.generativeai as genai

# IMPORT FROM CONFIG
from config.settings import GEMINI_API_KEY

# CONFIGURE GEMINI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

=======
from google import genai
from config.settings import GEMINI_API_KEY

# ===== INIT CLIENT =====
client = genai.Client(api_key=GEMINI_API_KEY)
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e

# ===== STATE =====
class State(TypedDict):
    transcript: str
    summary: str
    strengths: str
    weaknesses: str
    recommendation: str


# ===== LLM CALL =====
def call_llm(prompt):
<<<<<<< HEAD
    response = model.generate_content(prompt)
    return response.text.strip()
=======
    try:
        response = client.models.generate_content(
            model="models/gemini-1.5-flash",   # ✅ CHANGE HERE
            contents=prompt
        )

        return response.candidates[0].content.parts[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e


# ===== AGENTS =====

def summary_agent(state):
    prompt = f"""
<<<<<<< HEAD
Summarize the interview in 5 clear points.
=======
Summarize the interview in 5–6 professional lines.
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e

Transcript:
{state['transcript']}
"""
    return {"summary": call_llm(prompt)}


def strengths_agent(state):
    prompt = f"""
<<<<<<< HEAD
List the candidate's strengths in bullet points.
=======
List key strengths in bullet points.
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e

Transcript:
{state['transcript']}
"""
    return {"strengths": call_llm(prompt)}


def weaknesses_agent(state):
    prompt = f"""
<<<<<<< HEAD
List the candidate's weaknesses or areas of improvement.
=======
List weaknesses or areas of improvement.
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e

Transcript:
{state['transcript']}
"""
    return {"weaknesses": call_llm(prompt)}


def recommendation_agent(state):
    prompt = f"""
<<<<<<< HEAD
Based on the interview, give a hiring decision:
=======
Based on the interview, give ONLY one:
>>>>>>> 96cc4be99718bec97f852d9e12205c16d8e9959e
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