# ==============================
# COMMON SYSTEM INSTRUCTION
# ==============================
BASE_INSTRUCTION = """
You are a senior HR interviewer and talent evaluator.

Analyze the interview transcript carefully and provide professional, concise, and structured output.
Avoid vague statements. Be precise and realistic.
"""


# ==============================
# SUMMARY PROMPT
# ==============================
def build_summary_prompt(transcript: str) -> str:
    return f"""
{BASE_INSTRUCTION}

TASK:
Provide a concise executive summary (5-6 lines).

GUIDELINES:
- Focus on skills, experience, and communication
- Keep it professional

TRANSCRIPT:
{transcript}
"""


# ==============================
# STRENGTHS PROMPT
# ==============================
def build_strength_prompt(transcript: str) -> str:
    return f"""
{BASE_INSTRUCTION}

TASK:
List key strengths of the candidate.

FORMAT:
- Bullet points
- Max 5 points

TRANSCRIPT:
{transcript}
"""


# ==============================
# WEAKNESSES PROMPT
# ==============================
def build_weakness_prompt(transcript: str) -> str:
    return f"""
{BASE_INSTRUCTION}

TASK:
Identify weaknesses or areas of improvement.

FORMAT:
- Bullet points
- Max 5 points
- Be realistic, not harsh

TRANSCRIPT:
{transcript}
"""


# ==============================
# RECOMMENDATION PROMPT
# ==============================
def build_recommendation_prompt(transcript: str) -> str:
    return f"""
{BASE_INSTRUCTION}

TASK:
Provide final hiring recommendation.

OPTIONS:
- Best Fit
- Good Fit
- Partial Fit

Also give 1-line justification.

FORMAT:
Recommendation: <value>
Reason: <short reason>

TRANSCRIPT:
{transcript}
"""


# ==============================
# OPTIONAL: FULL JSON PROMPT
# ==============================
def build_full_analysis_prompt(transcript: str) -> str:
    return f"""
{BASE_INSTRUCTION}

TASK:
Analyze the transcript and return structured JSON.

FORMAT:
{{
  "summary": "...",
  "strengths": ["...", "..."],
  "weaknesses": ["...", "..."],
  "recommendation": "Best Fit / Good Fit / Partial Fit"
}}

STRICT RULE:
Return ONLY valid JSON.

TRANSCRIPT:
{transcript}
"""