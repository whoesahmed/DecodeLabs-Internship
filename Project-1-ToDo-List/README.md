# Project 1: To-Do List

**DecodeLabs Python Programming Internship – Project 1**

A simple command-line To-Do List that demonstrates the core concepts of Python Lists.

## Project Overview
This project is a command-line application that helps users manage a personal to-do list. It uses a Python list to store tasks and provides a menu-driven interface to add and display tasks. The program is designed to show how Python lists, loops, functions, and the `if __name__ == "__main__"` guard work together in a real project.

## Features
- Add tasks
- View all tasks (numbered)
- Exit cleanly

## Concepts Used
- Python Lists
- `.append()`
- `for` loops + `enumerate()`
- Functions
- `if __name__ == "__main__"`

## Example
```python
======= Welcome to your To-Do List =======

Choose an option (1: Add, 2: View, 3: Quit): 1
Enter a task: Open VS Code
Task added: Open VS Code
Choose an option (1: Add, 2: View, 3: Quit): 1
Enter a task: Start new Project
Task added: Start new Project
Choose an option (1: Add, 2: View, 3: Quit): 1
Enter a task: Test it and Push it
Task added: Test it and Push it
Choose an option (1: Add, 2: View, 3: Quit): 1
Enter a task: Take a break!
Task added: Take a break!
Choose an option (1: Add, 2: View, 3: Quit): 1
Enter a task: Start Coding where you left off...
Task added: Start Coding where you left off...
Choose an option (1: Add, 2: View, 3: Quit): 2
1. Open VS Code
2. Start new Project
3. Test it and Push it
4. Take a break!
5. Start Coding where you left off...
Choose an option (1: Add, 2: View, 3: Quit): 3
Goodbye! Your tasks are cleared from memory.
```

## How to Run
```bash

python main.py