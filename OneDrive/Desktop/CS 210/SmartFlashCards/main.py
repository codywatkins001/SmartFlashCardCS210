from flashcard_manager import FlashcardManager
from quiz_engine import QuizEngine
from ai_generator import AIGenerator

import os
print("Loaded API?", os.getenv("OPENAI_API_KEY"))

def main():
    manager = FlashcardManager("data/flashcards.json")
    quiz = QuizEngine(manager)
    ai = AIGenerator()

    while True:
        print("\n=== Smart Flashcards ===")
        print("[1] Create flashcards with AI")
        print("[2] Review flashcards")
        print("[3] Take a quiz")
        print("[4] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            topic = input("Enter a topic to study: ")
            difficulty = input("Select difficulty [beginner/intermediate/advanced]: ")
            cards = ai.generate(topic, difficulty)
            manager.save_flashcards(topic, cards)
            print(f"Saved {len(cards)} flashcards for topic: {topic}")

        elif choice == "2":
            manager.review()

        elif choice == "3":
            quiz.start_quiz()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
