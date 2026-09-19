# 581-Project-1: Minesweeper

A single-player Minesweeper game built in Python with **pygame** for **EECS 581** at the **University of Kansas**.

The player uncovers cells on a 10×10 grid, using the numbers to figure out where the mines are, and flags cells they think hide a mine. **Uncover every safe cell to win. Uncover a mine and you lose.**

---

## Table of Contents

- [Team](#team)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Current Status](#current-status)
- [Testing](#testing)
- [Sources and Attribution](#sources-and-attribution)

---

## Team

| Name | Role |
|---|---|
| Zachary McCauley | Game Logic |
| Emilia Davis | User Interface / Board Display |
| Eliza Malyshev | Meeting Documentation and Input Processing |
| Daniel Harris | Passing Input Between UI and Game Logic |
| Adira Mongar | Project Manager and Jira Organizer |
| Ryan Graham | Assistance and Integration |
| Jett Viduya | Testing and README |

---

## Requirements

- **Python 3.10 or newer** (the code uses `match` statements)
- **pygame-ce**

Install pygame-ce:

```bash
pip install pygame-ce
```

> On Windows, if `pip` isn't recognized, use `py -m pip install pygame-ce`.

---

## How to Run

1. Download or clone this repository.
2. Open a terminal **inside the project folder** (the one containing `UI Display.py` and `SpriteSheet.png`).
3. Run:

```bash
python "UI Display.py"
```

> **Windows:** you can also use `py "UI Display.py"`. The quotes are needed because the file name has a space.

> **Note:** Run the game from the project folder. Launching it from a different folder (including VS Code's Run button when a parent folder is open) currently crashes with `FileNotFoundError: SpriteSheet.png`.

---

## How to Play

| Action | Control |
|---|---|
| Uncover a cell | **Left-click** |
| Place / remove a flag | **Right-click** |
| Chord (open all neighbors of a number whose flags are all placed) | **Left-click** an uncovered number |
| Quit | Close the window |

**Rules**

- Your **first click is always safe**, because mines are placed after it.
- A number shows how many of the **8 surrounding cells** contain mines.
- Opening a cell with no nearby mines **automatically opens the area around it**.
- Flagged cells **can't be uncovered** until the flag is removed.
- Columns are labeled **A–J** and rows **1–10**.

---

## Project Structure

```
581-Project-1/
├── UI Display.py               # pygame window, drawing and mouse input (run this file)
├── minesweeper.py              # Game logic: the Minesweeper class
├── SpriteSheet.png             # Cell, flag, mine and number sprites
├── testmine.py                 # Text-based version used during development
├── Minesweeper Test Report.pdf # Manual test results and bug list
├── Meeting Notes.pdf           # Team meeting log
└── Kami Export - 581_P1_*.pdf  # Grid and schema planning documents
```

---

## How It Works

| Component | File | What it does |
|---|---|---|
| **Board / Game Logic** | `minesweeper.py` | Stores two 10×10 grids: a hidden one with the mines and adjacent-mine counts, and a visible one tracking covered, uncovered and flagged cells. Handles mine placement, digging, flood-fill, flagging, chording and the win check. |
| **User Interface** | `UI Display.py` | Every frame, asks the game what each cell should look like and draws the matching sprite, plus the A–J / 1–10 labels. |
| **Input Handler** | `UI Display.py` | Converts a mouse click's pixel position into a row and column, then calls `dig()` for a left-click or `flag()` for a right-click. |

**Data flow:**

```
Mouse click → converted to row/column → Game Logic updates the board → UI redraws the board
```

---

## Current Status

**Working**

- 10×10 board with A–J / 1–10 labels
- Random mine placement with a safe first click
- Correct numbers, recursive opening of empty areas, flagging and chording
- Win and loss detection
- No crashes found during stress testing (rapid clicking)

**In Progress**

- Letting the player choose the mine count (10–20)
- Remaining-mines counter
- Status indicator ("Playing", "Game Over: Loss", "Victory")
- Revealing all mines on a loss instead of closing the window
- Ignoring clicks on the row/column labels
- Completing prologue comments in every file

---

## Testing

All testing so far has been done by playing the game by hand against a checklist built from the project requirements. Results and current bugs are in the [Minesweeper Test Report](Minesweeper%20Test%20Report.pdf).

---

## Sources and Attribution

- [pygame-ce documentation](https://pyga.me/docs/)
- Parts of this README and the test report were drafted with help from Claude (Anthropic AI assistant) and reviewed by the team.
- Each source file lists any additional sources in its prologue comment.
