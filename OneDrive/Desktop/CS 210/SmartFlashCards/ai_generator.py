import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import re

dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path=dotenv_path)

class AIGenerator:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key not found. Make sure .env exists and has OPENAI_API_KEY.")
        self.client = OpenAI(api_key=api_key)

    def generate(self, topic, difficulty):
        prompt = f"""
        Generate 3 educational flashcards for the topic '{topic}'.
        Difficulty: {difficulty}.
        Format the response EXACTLY as a JSON array like:
        [
          {{"question": "...", "answer": "..."}}
        ]
        Keep answers short.
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # smaller model to save tokens
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.choices[0].message.content.strip()

            # Extract JSON array even if GPT adds extra text
            match = re.search(r"\[.*\]", content, re.DOTALL)
            if match:
                return json.loads(match.group(0))
            else:
                print("Error: AI response invalid. Returning empty list.")
                print(content)
                return []

        except Exception as e:
            print("Error generating flashcards:", str(e))
            return []
