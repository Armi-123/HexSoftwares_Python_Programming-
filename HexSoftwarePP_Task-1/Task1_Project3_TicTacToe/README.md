# 🎮 Tic-Tac-Toe Game using Python

## 📌 Project Overview

The Tic-Tac-Toe Game is a Python-based console application that allows a user to play against the computer. The game follows the traditional Tic-Tac-Toe rules where the player uses **"X"** and the computer uses **"O"**.

The computer makes moves automatically using Python's built-in **random** library. The game continues until either the player wins, the computer wins, or the match ends in a draw.

This project was developed as part of the **Hex Softwares Python Programming Internship**.

---

## 🎯 Objectives

* Develop a Tic-Tac-Toe game using Python.
* Implement Player vs Computer gameplay.
* Use Python's random module for computer moves.
* Detect winning combinations.
* Handle draw situations.
* Validate user inputs.
* Provide an interactive console-based gaming experience.

---

## 🎮 Game Features

### 👤 Player vs Computer

* Human player uses **"X"**.
* Computer uses **"O"**.

### 🎲 Random Computer Moves

* Computer automatically selects available positions.
* Randomized move generation using Python's random library.

### 🏆 Win Detection

* Checks all possible winning combinations.
* Declares the winner immediately when a winning pattern is found.

### 🤝 Draw Detection

* Detects when all positions are filled.
* Ends the game as a draw if no winner exists.

### ✅ Input Validation

* Prevents invalid position selection.
* Prevents selecting already occupied cells.
* Ensures smooth gameplay experience.

---

## 🛠️ Technologies Used

* Python 3
* Random Module
* Console-Based Interface

---

## 📈 Project Workflow

### 1. Initialize Game Board

* Create an empty 3×3 board.
* Display the board to the player.

### 2. Player Move

* Accept input between 1 and 9.
* Validate selected position.

### 3. Computer Move

* Select a random available position.
* Place **"O"** on the board.

### 4. Check Winner

* Verify rows, columns, and diagonals.
* Declare winner if conditions are met.

### 5. Check Draw

* If the board is full and no winner exists.
* Display draw message.

---

## 🎲 Board Positions

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

---

## 📷 Sample Output

```text
=== Tic Tac Toe ===

Enter position (1-9): 5

O |   |
--+---+--
  | X |
--+---+--

Enter position (1-9): 4

O |   |
--+---+--
X | X |
--+---+--
  |   | O

Enter position (1-9): 6

🎉 You Win!
```

---

## 🔍 Key Outcomes

* Successfully implemented Tic-Tac-Toe game logic.
* Integrated random computer moves.
* Implemented win and draw detection.
* Developed input validation mechanisms.
* Improved problem-solving and game development skills.

---

## 🎓 Learning Outcomes

Through this project, the following skills were developed:

* Python Programming
* Game Logic Development
* Conditional Statements
* Loops and Functions
* Random Module Usage
* Input Validation
* Problem Solving

---

## ✅ Conclusion

This project demonstrates the implementation of a Tic-Tac-Toe game using Python. The game allows users to play against a computer opponent while showcasing important programming concepts such as loops, functions, condition checking, randomization, and user interaction.

The project serves as an excellent example of beginner-friendly game development using Python.

---

## 📦 Requirements

No external libraries are required.

Uses only the **Python Standard Library**.

---

## 📂 Project Structure

```text
Task1_Project3_TicTacToe/
│
├── tic_tac_toe.py
├── screenshots/
│   └── Output.png
├── README.md
```

---

## 🚀 Run Project

```bash
python tic_tac_toe.py
```

---

## 👨‍💻 Author

**Armi Sherathiya**

Hex Softwares Python Programming Project