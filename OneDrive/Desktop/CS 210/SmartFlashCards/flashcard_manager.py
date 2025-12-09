import json

class FlashcardManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.load()

    def load(self):
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except:
            return {}

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def save_flashcards(self, topic, flashcards):
        self.data[topic] = flashcards
        self.save()

    def review(self):
        if not self.data:
            print("No flashcards yet!")
            return

        for topic, cards in self.data.items():
            print(f"\n--- {topic} ---")
            for card in cards:
                print(f"Q: {card['question']}")
                print(f"A: {card['answer']}\n")
