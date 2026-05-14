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

A class is considered a blueprint or template for creating objects. It defines
what attributes and methods an object should have. An object is the actual
instance created from a class.

Attributes are variables that belong to the object, while methods are functions
inside the class that define the behavior of the object.

Object-Oriented Programming (OOP) helps programmers organize code into reusable
and manageable structures. It also improves readability and maintainability.

For example:
- A Student class may contain attributes such as name and age.
- A Student class may also contain methods such as introduce() or study().

The __init__() method is called the constructor. It automatically runs whenever
an object is created from a class.

Benefits of using classes and objects:
1. Code reusability
2. Better organization
3. Easier debugging
4. Scalability for larger applications

Real-life Example:
A car can be considered a class.
Different cars such as Toyota, Honda, or Ford are objects created from that
class.
""",
            """class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

student1 = Student("Angelo", 20)
print(student1.introduce())""",
            [
                {
                    "question": "What is a class in Python?",
                    "choices": [
                        "A. A blueprint for objects",
                        "B. A loop",
                        "C. A text file",
                        "D. A keyword",
                    ],
                    "answer": "A",
                },
                {
                    "question": "What is the purpose of __init__()?",
                    "choices": [
                        "A. To stop the program",
                        "B. To initialize object attributes",
                        "C. To create loops",
                        "D. To sort lists",
                    ],
                    "answer": "B",
                },
                {
                    "question": "What is an object?",
                    "choices": [
                        "A. An instance of a class",
                        "B. A Python library",
                        "C. A file",
                        "D. A loop condition",
                    ],
                    "answer": "A",
                },
            ],
        ),
        Lesson(
            2,
            "File Handling with JSON",
            """
File handling allows programs to store data permanently even after the program
stops running.

Python provides built-in functions such as open(), read(), and write() for file
operations.

JSON stands for JavaScript Object Notation. It is a lightweight format used to
store and exchange data.

JSON is commonly used because:
1. It is human-readable
2. It is easy to store dictionaries and lists
3. Many programming languages support it

The json module in Python provides:
- json.dump() to write Python data into a JSON file
- json.load() to read JSON data from a file

The with open() statement is important because it automatically closes the file
after use. This prevents resource leaks and makes file handling safer.

Real-life Example:
Applications such as games or student systems save user progress into JSON
files so the information remains available later.
""",
            """import json

student_data = {
    "name": "Angelo",
    "score": 95,
    "subject": "Python"
}

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

with open("student.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)""",
            [
                {
                    "question": "What does JSON stand for?",
                    "choices": [
                        "A. Java Standard Output Network",
                        "B. JavaScript Object Notation",
                        "C. Java Source Open Network",
                        "D. Joined Simple Object Name",
                    ],
                    "answer": "B",
                },
                {
                    "question": "Which function writes data into a JSON file?",
                    "choices": [
                        "A. json.dump()",
                        "B. json.read()",
                        "C. json.close()",
                        "D. json.stop()",
                    ],
                    "answer": "A",
                },
                {
                    "question": "Why is with open() useful?",
                    "choices": [
                        "A. It automatically closes files",
                        "B. It deletes files",
                        "C. It creates classes",
                        "D. It sorts dictionaries",
                    ],
                    "answer": "A",
                },
            ],
        ),
        Lesson(
            3,
            "Data Structures and Searching",
            """
Data structures are used to organize and manage data efficiently.

Python provides several built-in data structures:
1. Lists
2. Tuples
3. Dictionaries
4. Sets

Lists store multiple items in order and allow modification.
Dictionaries store data using key-value pairs.

Algorithms are step-by-step procedures used to solve problems.
One common algorithm is linear search.

Linear search works by checking items one by one until the target item is found.
Although simple, it is effective for small datasets.

Sorting is another important operation.
Sorting organizes data in ascending or descending order.

Real-life Example:
A school system may search for a student name from a list of enrolled students.
""",
            """lessons = ["Classes", "Files", "Algorithms", "Recursion"]

target = "Algorithms"

for lesson in lessons:
    if lesson == target:
        print("Lesson found!")
        break""",
            [
                {
                    "question": "Which data structure stores key-value pairs?",
                    "choices": [
                        "A. List",
                        "B. Dictionary",
                        "C. Tuple",
                        "D. String",
                    ],
                    "answer": "B",
                },
                {
                    "question": "What does linear search do?",
                    "choices": [
                        "A. Finds data step-by-step",
                        "B. Deletes variables",
                        "C. Creates classes",
                        "D. Stops recursion",
                    ],
                    "answer": "A",
                },
                {
                    "question": "Why is sorting useful?",
                    "choices": [
                        "A. It organizes data",
                        "B. It closes files",
                        "C. It removes objects",
                        "D. It creates generators",
                    ],
                    "answer": "A",
                },
            ],
        ),
        Lesson(
            4,
            "Recursion and Base Case",
            """
Recursion is a programming technique where a function calls itself repeatedly.

A recursive function must always contain a base case.
The base case is the condition that stops the recursion.
Without a base case, the function may continue forever and cause an error.

Recursion is useful for solving problems that can be divided into smaller
subproblems.

Examples of recursion include:
1. Factorial computation
2. Fibonacci sequence
3. Countdown timers
4. Tree traversal algorithms

Advantages of recursion:
- Cleaner code for repetitive problems
- Easier implementation for mathematical concepts

Disadvantages of recursion:
- May consume more memory
- Can become difficult to debug if overly complex

Real-life Example:
A countdown timer repeatedly decreases numbers until it reaches zero.
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
                    "choices": [
                        "A. A function calling itself",
                        "B. A file handler",
                        "C. A Python library",
                        "D. A sorting method",
                    ],
                    "answer": "A",
                },
                {
                    "question": "What is the purpose of a base case?",
                    "choices": [
                        "A. To stop recursion",
                        "B. To open files",
                        "C. To sort lists",
                        "D. To create dictionaries",
                    ],
                    "answer": "A",
                },
                {
                    "question": "What may happen without a base case?",
                    "choices": [
                        "A. Infinite recursion",
                        "B. Faster execution",
                        "C. Automatic sorting",
                        "D. File corruption",
                    ],
                    "answer": "A",
                },
            ],
        ),
        Lesson(
            5,
            "Generators and Comprehensions",
            """
Generators are special functions that use the yield keyword.

Unlike normal functions that return all values at once, generators produce
values one at a time. This saves memory and improves efficiency.

List comprehensions provide a shorter and cleaner way to create lists.

Generators are useful when handling large amounts of data because they generate
items only when needed.

Advantages of generators:
1. Memory efficient
2. Faster for large datasets
3. Cleaner iteration

Advantages of comprehensions:
1. Shorter syntax
2. Easier readability
3. Faster execution in many cases

Real-life Example:
A streaming application loads videos one at a time instead of loading
everything at once.
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
                    "question": "What keyword is used in generators?",
                    "choices": [
                        "A. stop",
                        "B. yield",
                        "C. close",
                        "D. delete",
                    ],
                    "answer": "B",
                },
                {
                    "question": "What is the advantage of generators?",
                    "choices": [
                        "A. Memory efficiency",
                        "B. Automatic sorting",
                        "C. File deletion",
                        "D. Infinite loops",
                    ],
                    "answer": "A",
                },
                {
                    "question": "What does a list comprehension do?",
                    "choices": [
                        "A. Creates lists in a shorter way",
                        "B. Stops recursion",
                        "C. Creates files",
                        "D. Deletes objects",
                    ],
                    "answer": "A",
                },
            ],
        ),
    ]
