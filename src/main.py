"""
Main module for the Python Core Lessons Study CLI.

This file starts the command-line application. The project is divided into
separate modules for display, file handling, lesson data, and models.
"""

from display.ui import (
    clear_screen,
    pause,
    print_header,
    print_menu,
    print_section,
)
from file_handler.progress_manager import ProgressFile
from library.lessons_data import load_lessons
from datetime import datetime


DATA_FILE = "data/progress.json"


def menu_action(function):
    """Decorates menu actions with clean section formatting.

    Args:
        function (function): Function to be wrapped.

    Returns:
        function: Wrapped function with UI formatting.
    """
    def wrapper(*args, **kwargs):
        print_section()
        result = function(*args, **kwargs)
        print_section()
        return result

    return wrapper


class StudyApp:
    """Controls the Python Core Lessons Study CLI application.

    Attributes:
        lessons (list): List of Lesson objects.
    """

    def __init__(self):
        """Initializes the application and loads lesson data."""
        self.lessons = load_lessons()

    def lesson_generator(self):
        """Yields lessons one at a time.

        Yields:
            Lesson: A lesson object.
        """
        for lesson in self.lessons:
            yield lesson

    def recursive_countdown(self, number):
        """Demonstrates recursion with a clear base case.

        Args:
            number (int): Countdown starting number.
        """
        if number <= 0:
            print("Study session ready.")
            return

        print(f"Opening lesson in {number}...")
        self.recursive_countdown(number - 1)

    def find_lesson_by_id(self, lesson_id):
        """Finds a lesson by ID using linear search.

        Args:
            lesson_id (int): Lesson number.

        Returns:
            Lesson or None: Matching lesson object, or None.
        """
        for lesson in self.lessons:
            if lesson.lesson_id == lesson_id:
                return lesson
        return None

    def search_lesson(self, keyword):
        """Searches lessons by keyword using linear search.

        Args:
            keyword (str): Search keyword.

        Returns:
            list: Matching Lesson objects.
        """
        matches = []

        for lesson in self.lessons:
            if keyword.lower() in lesson.title.lower():
                matches.append(lesson)

        return matches

    def sorted_lessons(self):
        """Sorts lessons alphabetically by title.

        Returns:
            list: Sorted Lesson objects.
        """
        return sorted(self.lessons, key=lambda lesson: lesson.title)

    @menu_action
    def view_lessons(self):
        """Displays the available lesson list."""
        print("Available Lessons")
        print("-" * 44)

        for lesson in self.lesson_generator():
            print(f"{lesson.lesson_id}. {lesson.title}")

        print("\nTip: Choose option 2 to open and study a lesson.")

    @menu_action
    def study_lesson(self):
        """Lets the user select and study one lesson."""
        self.view_lessons()

        try:
            choice = int(input("\nChoose lesson number: "))
            lesson = self.find_lesson_by_id(choice)

            if lesson is None:
                print("Invalid lesson number.")
                return

            print()
            self.recursive_countdown(3)
            lesson.display()

            with ProgressFile(DATA_FILE) as progress:
                progress.add_record(
                    {
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "lesson": lesson.title,
                        "activity": "Studied lesson",
                        "score": None,
                    }
                )

        except ValueError:
            print("Invalid input. Please enter a number.")

    @menu_action
    def take_quiz(self):
        """Lets the user take a quiz for a selected lesson."""
        self.view_lessons()

        try:
            choice = int(input("\nChoose quiz lesson number: "))
            lesson = self.find_lesson_by_id(choice)

            if lesson is None:
                print("Invalid lesson number.")
                return

            score = lesson.take_quiz()
            total = len(lesson.quiz)

            print(f"\nFinal Score: {score}/{total}")

            with ProgressFile(DATA_FILE) as progress:
                progress.add_record(
                    {
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "lesson": lesson.title,
                        "activity": "Quiz",
                        "score": f"{score}/{total}",
                    }
                )

        except ValueError:
            print("Invalid input. Please enter a number.")

    @menu_action
    def search_lessons_menu(self):
        """Searches lessons from a keyword provided by the user."""
        keyword = input("Enter keyword: ").strip()

        if not keyword:
            print("Keyword cannot be empty.")
            return

        matches = self.search_lesson(keyword)

        if not matches:
            print("No lesson found.")
            return

        print("\nSearch Results")
        print("-" * 44)

        for lesson in matches:
            print(f"{lesson.lesson_id}. {lesson.title}")

    @menu_action
    def view_sorted_lessons(self):
        """Displays lessons sorted alphabetically."""
        print("Lessons Sorted A-Z")
        print("-" * 44)

        for lesson in self.sorted_lessons():
            print(f"{lesson.lesson_id}. {lesson.title}")

    @menu_action
    def view_progress(self):
        """Displays saved progress records."""
        with ProgressFile(DATA_FILE) as progress:
            records = progress.get_records()

        if not records:
            print("No progress records yet.")
            return

        print("Progress Records")
        print("-" * 44)

        for record in records:
            print(
                f"{record['date']} | {record['lesson']} | "
                f"{record['activity']} | Score: {record['score']}"
            )

    def run(self):
        """Runs the main application loop."""
        while True:
            clear_screen()
            print_header()
            print_menu()

            choice = input("Select an option: ").strip()

            if choice in ["1", "01"]:
                self.view_lessons()
                pause()

            elif choice in ["2", "02"]:
                self.study_lesson()
                pause()

            elif choice in ["3", "03"]:
                self.take_quiz()
                pause()

            elif choice in ["4", "04"]:
                self.search_lessons_menu()
                pause()

            elif choice in ["5", "05"]:
                self.view_sorted_lessons()
                pause()

            elif choice in ["6", "06"]:
                self.view_progress()
                pause()

            elif choice in ["7", "07"]:
                print("\nThank you for using Python Core Lessons Study CLI.")
                break

            else:
                print("\nInvalid option. Please choose from 1 to 7.")
                pause()


def main():
    """Creates and runs the application."""
    app = StudyApp()
    app.run()


if __name__ == "__main__":
    main()
