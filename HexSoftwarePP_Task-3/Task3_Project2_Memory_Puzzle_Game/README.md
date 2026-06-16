# 🧩 Memory Puzzle Game Using Python

## 📌 Project Overview

The Memory Puzzle Game is a console-based Python application where players test their memory skills by matching pairs of hidden cards.

The game randomly shuffles card pairs and displays them face down. The player selects two positions at a time. If both cards match, they remain visible; otherwise, they are hidden again.

The objective is to find all matching pairs using the fewest possible moves.

This project was developed as part of the **Hex Softwares Python Programming Internship**.

---

## 🎯 Objectives

* Develop a Memory Puzzle Game using Python.
* Implement random card shuffling.
* Match hidden card pairs.
* Track player moves.
* Measure game completion time.
* Improve logical thinking and memory skills.
* Provide an interactive console-based gaming experience.

---

## 🎮 Game Features

### Random Card Arrangement

* Cards are shuffled every time the game starts.
* Each game provides a different experience.

### Pair Matching Logic

* Players select two positions.
* Matching cards remain visible.
* Non-matching cards are hidden again.

### Move Counter

* Counts total moves taken by the player.

### Time Tracking

* Records total time taken to complete the puzzle.

### Input Validation

* Prevents invalid inputs.
* Prevents selecting the same position twice.
* Prevents selecting already matched cards.

---

## 🛠️ Technologies Used

* Python 3
* Random Module
* Time Module
* Console-Based Interface

---

## 📈 Project Workflow

### 1. Initialize Cards

* Create pairs of cards.
* Shuffle cards randomly.

### 2. Display Positions

* Show card positions from 1 to 8.

### 3. Player Selection

* User selects two positions.

### 4. Match Verification

* Compare selected cards.
* Display match or mismatch result.

### 5. Update Board

* Keep matched cards visible.
* Hide unmatched cards.

### 6. Game Completion

* Continue until all pairs are matched.
* Display total moves and time taken.

---

## 🎲 Board Layout

### Positions

```text
1 2 3 4
5 6 7 8
```
### Hidden Board

```text
* * * *
* * * *
```
---

## 📷 Sample Output

```text
===== MEMORY PUZZLE GAME =====

Positions:
1 2 3 4
5 6 7 8

Board:
* * * *
* * * *

Enter first position (1-8): 1
Enter second position (1-8): 6

A * * *
* A * *

✅ Match Found!

...

🎉 Congratulations!
You matched all pairs.

Total Moves: 10
Time Taken: 45.23 seconds
```
---

## 🔍 Key Outcomes

* Successfully implemented memory matching logic.
* Integrated random card generation.
* Added move counting functionality.
* Implemented game completion detection.
* Added time tracking feature.
* Improved problem-solving and game development skills.

---

## 🎓 Learning Outcomes

Through this project, the following skills were developed:

* Python Programming
* Game Development Basics
* Randomization Techniques
* Time Tracking
* Conditional Statements
* Loops and Functions
* Input Validation
* Logical Thinking
* Problem Solving

---

## ✅ Conclusion

This project demonstrates the implementation of a Memory Puzzle Game using Python. The game challenges users to match hidden card pairs while tracking moves and completion time.

The project highlights important Python concepts such as loops, lists, condition checking, randomization, time measurement, and user interaction, making it an excellent beginner-friendly game development project.

---

## 📦 Requirements

No external libraries are required.

Uses only Python Standard Library modules:

* random
* time

---

## 📂 Project Structure

```text
Task3_Project2_Memory_Puzzle_Game/
│
├── memory_puzzle.py
├── README.md
├── requirements.txt
│
└── screenshots/
    └── output.png
```

---

## 🚀 Run Project

```bash
python memory_puzzle.py
```

---

## 👨‍💻 Author

**Armi Sherathiya**

Hex Softwares Python Programming Project