from gpt4all import GPT4All
from prompts import QUESTION_PROMPT, SUMMARY_PROMPT
from storage import save_interview

MODEL_PATH = "orca-mini-3b-gguf2-q4_0.gguf"


class AIInterviewer:

    def __init__(self, topic):
        self.topic = topic
        self.questions = []
        self.answers = []

        print("Loading Orca Mini model...")
        self.model = GPT4All(MODEL_PATH)

    def ask_llm(self, prompt):

        with self.model.chat_session():
            response = self.model.generate(
                prompt,
                max_tokens=300,
                temp=0.6,
                top_k=40,
                top_p=0.9
            )

        return response.strip()

    def generate_questions(self):

        output = self.ask_llm(
            QUESTION_PROMPT.format(topic=self.topic)
        )

        self.questions = [
            line for line in output.split("\n")
            if line.strip().startswith(tuple("12345"))
        ]

    def conduct_interview(self):

        print("\n=== Interview Start ===\n")

        for question in self.questions[:5]:
            print(question)
            answer = input("Your answer: ")

            self.answers.append({
                "question": question,
                "answer": answer
            })

    def summarize(self):

        transcript = "\n".join(
            f"Q: {qa['question']}\nA: {qa['answer']}"
            for qa in self.answers
        )

        return self.ask_llm(
            SUMMARY_PROMPT.format(transcript=transcript)
        )

    def run(self):

        self.generate_questions()
        self.conduct_interview()

        summary = self.summarize()

        save_interview(
            self.topic,
            self.answers,
            summary
        )

        print("\n=== Interview Summary ===")
        print(summary)