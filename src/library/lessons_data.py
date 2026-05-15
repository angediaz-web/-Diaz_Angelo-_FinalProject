"""
Lesson library for the Python Core Lessons Study CLI.

This module stores all lesson content and quiz data.
"""

from models.lesson import Lesson


def load_lessons():
    """Creates the lesson objects used by the application.

    Returns:
        list: List of Lesson objects.
    """
    return [
        Lesson(
            1,
            "Classes and Objects",
            """
Classes and objects are one of the most important concepts in Python programming.

A class is a blueprint for creating objects. An object is an actual instance
created from a class.

Attributes are variables that belong to an object, while methods are functions
inside a class that define object behavior.

Object-Oriented Programming helps organize code, reduce repetition, and make
larger programs easier to maintain.
""",
            """class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, I am {self.name} and I am {self.age} years old."

student = Student("Angelo", 20)
print(student.introduce())""",
            [
                {
                    "question": "What is a class?",
                    "choices": ["A. Blueprint for objects", "B. A loop", "C. A file", "D. A number"],
                    "answer": "A",
                },
                {
                    "question": "What is an object?",
                    "choices": ["A. Instance of a class", "B. A folder", "C. A keyword", "D. A string only"],
                    "answer": "A",
                },
            ],
        ),

        Lesson(
            2,
            "File Handling with JSON",
            """
File handling allows programs to save and load data permanently.

JSON means JavaScript Object Notation. It is commonly used to store structured
data such as dictionaries and lists.

In this application, JSON is used to save study progress and quiz scores inside
the progress.json file.
""",
            """import json

data = {"name": "Angelo", "score": 95}

with open("record.json", "w") as file:
    json.dump(data, file, indent=4)

with open("record.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)""",
            [
                {
                    "question": "What is JSON used for?",
                    "choices": ["A. Storing data", "B. Drawing images", "C. Playing music", "D. Deleting Python"],
                    "answer": "A",
                },
                {
                    "question": "Which function writes data to JSON?",
                    "choices": ["A. json.dump()", "B. json.read()", "C. json.stop()", "D. json.input()"],
                    "answer": "A",
                },
            ],
        ),

        Lesson(
            3,
            "Data Structures and Searching",
            """
Data structures help organize and manage data.

Python includes lists, tuples, dictionaries, and sets. Lists store ordered items,
while dictionaries store key-value pairs.

Searching is an algorithm used to find information. This project uses linear
search, which checks each lesson one by one until a match is found.
""",
            """lessons = ["Classes", "Files", "Algorithms"]
target = "Files"

for lesson in lessons:
    if lesson == target:
        print("Lesson found!")""",
            [
                {
                    "question": "Which data structure stores key-value pairs?",
                    "choices": ["A. Dictionary", "B. List", "C. Tuple", "D. String"],
                    "answer": "A",
                },
                {
                    "question": "What does linear search do?",
                    "choices": ["A. Checks items one by one", "B. Deletes files", "C. Creates objects", "D. Stops loops"],
                    "answer": "A",
                },
            ],
        ),

        Lesson(
            4,
            "Recursion and Base Case",
            """
Recursion happens when a function calls itself.

A recursive function must have a base case. The base case is the condition that
stops recursion. Without it, the function may continue forever and cause an error.

This project uses a recursive countdown before opening a lesson.
""",
            """def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)

countdown(5)""",
            [
                {
                    "question": "What is recursion?",
                    "choices": ["A. Function calling itself", "B. File writing", "C. Sorting only", "D. A variable"],
                    "answer": "A",
                },
                {
                    "question": "What is the base case?",
                    "choices": ["A. Condition that stops recursion", "B. A folder", "C. A JSON file", "D. A class name"],
                    "answer": "A",
                },
            ],
        ),

        Lesson(
            5,
            "Generators and Comprehensions",
            """
Generators produce values one at a time using the yield keyword.

They are useful because they save memory, especially when working with large data.

Comprehensions are shorter ways to create lists, dictionaries, or sets.
""",
            """def even_numbers(limit):
    for number in range(1, limit + 1):
        if number % 2 == 0:
            yield number

squares = [x ** 2 for x in range(1, 6)]

print(list(even_numbers(10)))
print(squares)""",
            [
                {
                    "question": "What keyword is used by generators?",
                    "choices": ["A. yield", "B. returnonly", "C. stop", "D. close"],
                    "answer": "A",
                },
                {
                    "question": "What is a list comprehension?",
                    "choices": ["A. Short way to create lists", "B. A file", "C. A folder", "D. A database"],
                    "answer": "A",
                },
            ],
        ),
    ]