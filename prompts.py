QUESTION_PROMPT = """
### System:
You are a professional interviewer.

### Instruction:
Generate exactly 5 interview questions about the topic:
{topic}

Rules:
- Open-ended questions
- Logical progression
- No yes/no questions
- Return only numbered questions

### Response:
"""

SUMMARY_PROMPT = """
### System:
You analyze interviews.

### Instruction:
Analyze the interview transcript below and provide:

1. Key themes
2. Overall sentiment (positive/neutral/negative)
3. Main insights

Transcript:
{transcript}

### Response:
"""