# Project 2: Expense Tracker

**DecodeLabs Python Programming Internship – Project 2**  
**Intern:** Anwaar Ahmed Junaid

A simple command-line Expense Tracker that demonstrates the core concept of **Accumulators** and mathematical operations in Python.

## Features
- Add expense amounts continuously
- Keep a running total using the Accumulator pattern
- Handle invalid inputs gracefully
- Exit cleanly using a sentinel value (`done`)
- Display final total spent

## Concepts Used
- Accumulator pattern (`total += amount`)
- Type conversion (`float()`)
- `while` loop
- `try-except` for error handling
- Sentinel value to stop the program
- `if __name__ == "__main__"`

## How to run

```bash
python main.py
```

Then enter expenses one at a time, and type `done` when finished.

## Example

```
======= Expense Tracker =======
Enter your expenses one by one.
Type 'done' when you are finished.

Enter Expense Amount: 100
Added: 100.00 | Current Total: 100.00
Enter Expense Amount: 50
Added: 50.00 | Current Total: 150.00
Enter Expense Amount: abc
Invalid input. Please enter a number or type 'done'.
Enter Expense Amount: done

======= Summary =======
Total Spent: 150.00
```