# 🤖 Artificial Intelligence Lab Practicals

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-PrashilD15%2FAI-181717?logo=github)](https://github.com/PrashilD15/AI)

This repository contains clean, well-documented Python implementations of core **Artificial Intelligence (AI)** algorithms and laboratory practicals.

---

## 📑 Table of Contents

| # | Practical Name | Algorithm / Approach | File |
|---|---|---|---|
| **1** | [Vacuum Cleaner Agent](#practical-1--vacuum-cleaner-agent) | Simple Reflex Agent | [`practical_01_vacuum_cleaner_agent.py`](practical_01_vacuum_cleaner_agent.py) |
| **2** | [Tower of Hanoi](#practical-2--tower-of-hanoi-bfs) | Breadth-First Search (BFS) | [`practical_02_tower_of_hanoi_bfs.py`](practical_02_tower_of_hanoi_bfs.py) |
| **3** | [8-Puzzle Problem](#practical-3--8-puzzle-a-search) | A* Search (Manhattan Distance) | [`practical_03_8_puzzle_astar.py`](practical_03_8_puzzle_astar.py) |
| **4** | [Alpha-Beta Pruning](#practical-4--minimax-with-alpha-beta-pruning) | Minimax with Alpha-Beta Pruning | [`practical_04_minimax_alpha_beta.py`](practical_04_minimax_alpha_beta.py) |
| **5** | [Sudoku Solver](#practical-5--sudoku-solver-bfs) | Breadth-First Search (BFS) | [`practical_05_sudoku_solver_bfs.py`](practical_05_sudoku_solver_bfs.py) |
| **6** | [8-Queens Problem](#practical-6--8-queens-backtracking) | Backtracking | [`practical_06_8_queens_backtracking.py`](practical_06_8_queens_backtracking.py) |
| **7** | [Rule-Based Chatbot](#practical-7--rule-based-chatbot) | Regex & Pattern Matching | [`practical_07_rule_based_chatbot.py`](practical_07_rule_based_chatbot.py) |
| **8** | [Tic-Tac-Toe AI](#practical-8--tic-tac-toe-minimax) | Minimax Algorithm (Game Playing) | [`practical_08_tic_tac_toe_minimax.py`](practical_08_tic_tac_toe_minimax.py) |

---

## 🚀 Practicals Overview

### Practical 1 – Vacuum Cleaner Agent
- **Description:** Simulates an intelligent reflex agent operating in a two-room environment (`A` and `B`). The agent senses the state of its current room (`Clean`/`Dirty`) and decides whether to suck dirt or move to the adjacent room until both rooms are clean.
- **Run:**
  ```bash
  python practical_01_vacuum_cleaner_agent.py
  ```

---

### Practical 2 – Tower of Hanoi (BFS)
- **Description:** Finds the optimal, shortest sequence of moves to transfer $N$ disks from the source peg to the destination peg using **Breadth-First Search (BFS)** state space exploration.
- **Run:**
  ```bash
  python practical_02_tower_of_hanoi_bfs.py
  ```

---

### Practical 3 – 8-Puzzle (A* Search)
- **Description:** Solves the sliding 8-puzzle game using the **A\* Search algorithm** guided by the admissible **Manhattan Distance heuristic** ($h(n)$) to guarantee the minimum number of steps to reach the goal state.
- **Run:**
  ```bash
  python practical_03_8_puzzle_astar.py
  ```

---

### Practical 4 – Minimax with Alpha-Beta Pruning
- **Description:** Evaluates a game decision tree using the **Minimax algorithm** enhanced with **Alpha-Beta pruning** to eliminate unpromising branches and optimize adversarial decision-making.
- **Run:**
  ```bash
  python practical_04_minimax_alpha_beta.py
  ```

---

### Practical 5 – Sudoku Solver (BFS)
- **Description:** Solves a $9 \times 9$ Sudoku grid using **Breadth-First Search (BFS)** to explore valid number placements across rows, columns, and $3 \times 3$ sub-grids.
- **Run:**
  ```bash
  python practical_05_sudoku_solver_bfs.py
  ```

---

### Practical 6 – 8 Queens (Backtracking)
- **Description:** Places 8 non-attacking queens on an $8 \times 8$ chessboard using depth-first **backtracking**, ensuring no two queens share the same row, column, or diagonal.
- **Run:**
  ```bash
  python practical_06_8_queens_backtracking.py
  ```

---

### Practical 7 – Rule-Based Chatbot
- **Description:** An interactive conversational chatbot that parses user utterances using regular expressions (`re`) and replies with contextual responses or dynamic string interpolations.
- **Run:**
  ```bash
  python practical_07_rule_based_chatbot.py
  ```

---

### Practical 8 – Tic-Tac-Toe (Minimax)
- **Description:** An unbeatable Tic-Tac-Toe console game where the user plays against an AI agent powered by the **Minimax algorithm**, anticipating every prospective outcome.
- **Run:**
  ```bash
  python practical_08_tic_tac_toe_minimax.py
  ```

---

## 🛠️ Prerequisites & Setup

1. **Python 3.8+** installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/PrashilD15/AI.git
   cd AI
   ```
3. Run any practical script directly with Python:
   ```bash
   python practical_01_vacuum_cleaner_agent.py
   ```

---

## 👤 Author
- **Prashil Dalvi** ([@PrashilD15](https://github.com/PrashilD15))
