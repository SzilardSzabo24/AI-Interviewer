import json
import os
from datetime import datetime

def save_interview(topic, answers, summary):

    os.makedirs("interviews", exist_ok=True)

    data = {
        "topic": topic,
        "timestamp": str(datetime.now()),
        "responses": answers,
        "summary": summary
    }

    filename = f"interviews/interview_{datetime.now().timestamp()}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)