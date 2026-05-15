# Python Core Lessons Study CLI

## Project Title
Python Core Lessons Study CLI

## Student
Diaz, Angelo B.

## Brief Description
This project is a command-line interface application that helps users study intermediate Python programming lessons. The user can view lessons, study lesson content, take quizzes, search lessons, sort lessons, and track progress using a JSON file.

## Problem Solved
Students sometimes need a simple offline reviewer for programming topics. This CLI application provides a structured way to study, review, and test knowledge of intermediate Python concepts.

## Features
- View all available Python lessons
- Study at least 3 core intermediate Python lessons
- Take quizzes for every lesson
- Search lessons by keyword
- Sort lessons alphabetically
- Save and view study progress
- Handles invalid inputs
- Demonstrates recursion with a clear base case

## Intermediate Python Concepts Used
1. **Classes and Objects**
   - `Lesson` class represents each lesson.
   - `StudyApp` class controls the whole application.
   - `ProgressFile` class manages file handling.

2. **File Handling**
   - The application saves study and quiz progress in `data/progress.json`.
   - JSON is used to store data in a readable format.

3. **Data Structures**
   - Lists store lesson objects.
   - Dictionaries store quiz questions and progress records.

4. **Algorithms**
   - Linear search is used to find lessons by keyword and ID.
   - Sorting is used to display lessons alphabetically.

5. **Recursion and Base Case**
   - The `recursive_countdown()` method calls itself.
   - Base case: when the number becomes less than or equal to 0.

6. **Advanced Python Concepts**
   - Decorator: `menu_action`
   - Generator: `lesson_generator`
   - Context manager: `ProgressFile`

## Installation / Setup
1. Download or clone the repository.
2. Open the folder in VS Code or any terminal.
3. Make sure Python is installed.
4. Run the program using:

```bash
python src/main.py
```

## Requirements
No external libraries are required. This project uses only Python built-in modules.

## Sample CLI Usage

```text
PYTHON CORE LESSONS STUDY CLI
1. View Lessons
2. Study a Lesson
3. Take a Quiz
4. Search Lesson
5. View Sorted Lessons
6. View Progress
7. Exit
Choose an option: 1
```

```text
Available Intermediate Python Lessons:
1. Classes and Objects
2. File Handling with JSON
3. Data Structures and Searching
4. Recursion and Base Case
5. Generators and Comprehensions
```

```text
Choose an option: 3
Choose lesson quiz number: 1

Question 1: What is a class?
A. A blueprint for objects
B. A loop
C. A file
D. A number
Your answer: A
Correct!
```

## YouTube Video Demonstration

```text
YouTube Link: https://youtu.be/FlvLJeMwTcs?si=wIr9YZ01-q0ZwuCf
```
