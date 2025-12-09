class QuizEngine:
    def __init__(self, manager):
        self.manager = manager

    def start_quiz(self):
        if not self.manager.data:
            print("No flashcards to quiz. Create some first!")
            return

        topic = input("Enter topic to quiz: ")
        if topic not in self.manager.data:
            print("Topic not found!")
            return

        cards = self.manager.data[topic]
        score = 0

        for card in cards:
            print("\nQ:", card["question"])
            answer = input("Your answer: ").strip().lower()
            correct = card["answer"].strip().lower()

            if answer == correct:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. Correct answer: {card['answer']}")

        print(f"\nYour score: {score}/{len(cards)}")
