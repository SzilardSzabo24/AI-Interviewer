from interviewer import AIInterviewer

def main():
    topic = input("Enter interview topic: ")
    interviewer = AIInterviewer(topic)
    interviewer.run()

if __name__ == "__main__":
    main()