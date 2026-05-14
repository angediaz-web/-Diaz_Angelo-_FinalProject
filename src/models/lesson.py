"""
Lesson model for the Python Core Lessons Study CLI.

This module contains the Lesson class used to represent one programming lesson.
"""


class Lesson:
    """Represents one intermediate Python lesson.

    Attributes:
        lesson_id (int): Unique lesson ID.
        title (str): Lesson title.
        content (str): Lesson explanation.
        code_example (str): Sample lesson code.
        quiz (list): List of quiz dictionaries.
    """

    def __init__(self, lesson_id, title, content, code_example, quiz):
        """Initializes a Lesson object.

        Args:
            lesson_id (int): Unique lesson ID.
            title (str): Lesson title.
            content (str): Lesson explanation.
            code_example (str): Sample code.
            quiz (list): Quiz question dictionaries.
        """
        self.lesson_id = lesson_id
        self.title = title
        self.content = content
        self.code_example = code_example
        self.quiz = quiz

    def display(self):
        """Displays the full lesson content."""
        print(f"\nLesson {self.lesson_id}: {self.title}")
        print("─" * 54)
        print(self.content)
        print("\nSample Code")
        print("─" * 54)
        print(self.code_example)

    def take_quiz(self):
        """Runs the lesson quiz.

        Returns:
            int: Number of correct answers.
        """
        score = 0

        for index, item in enumerate(self.quiz, start=1):
            print(f"\nQuestion {index}: {item['question']}")

            for choice in item["choices"]:
                print(choice)

            answer = input("Your answer: ").strip().upper()

            if answer == item["answer"]:
                print("Correct.")
                score += 1
            else:
                print(f"Incorrect. Correct answer: {item['answer']}")

        return score
