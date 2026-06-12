# Tic-Tac-Toe

A two-player command-line Tic-Tac-Toe game written in Python 3.

Positions are numbered 1–9, left to right, top to bottom:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## Run locally

Requires Python 3.

**Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate       # Windows
```

**Install dependencies and run:**

```bash
pip install -r requirements.txt
python game.py
```

**Deactivate when done:**

```bash
deactivate
```

## Run with Docker

**Build the image:**

```bash
docker build -t tic-tac-toe .
```

**Run the container** (interactive mode required for stdin):

```bash
docker run -it tic-tac-toe
```
