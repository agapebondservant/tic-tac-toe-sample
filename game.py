#!/usr/bin/env python3

import random
import time

RED   = "\033[31m"
BLUE  = "\033[34m"
RESET = "\033[0m"

COLORS = {"X": RED, "O": BLUE}

WINS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def new_board():
    return [str(i + 1) for i in range(9)]


def colorize(cell):
    color = COLORS.get(cell)
    return "{}{}{}".format(color, cell, RESET) if color else cell


def display(board):
    print()
    for row in range(3):
        cells = [colorize(c) for c in board[row * 3:(row + 1) * 3]]
        print(" {} | {} | {} ".format(*cells))
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board, mark):
    return any(board[a] == board[b] == board[c] == mark for a, b, c in WINS)


def is_draw(board):
    return all(cell in ("X", "O") for cell in board)


def computer_move(board):
    available = [i for i, cell in enumerate(board) if cell not in ("X", "O")]
    for idx in available:
        board[idx] = "X"
        if check_winner(board, "X"):
            board[idx] = str(idx + 1)
            return idx
        board[idx] = str(idx + 1)
    return random.choice(available)


def get_move(board, player):
    while True:
        raw = input("Player {} — enter position (1-9): ".format(player)).strip()
        if raw.isdigit() and 1 <= int(raw) <= 9:
            idx = int(raw) - 1
            if board[idx] not in ("X", "O"):
                return idx
            print("That position is already taken.")
        else:
            print("Invalid input. Enter a number between 1 and 9.")


def play():
    players = ("X", "O")
    turn = 0

    board = new_board()
    print("\nTic-Tac-Toe")
    print("You are Player O. The computer plays X.")
    print("Positions are numbered 1–9, left to right, top to bottom.")
    display(board)

    while True:
        player = players[turn % 2]
        if player == "X":
            time.sleep(1)
            idx = computer_move(board)
            print("Computer chose position {}.".format(idx + 1))
        else:
            idx = get_move(board, player)
        board[idx] = player
        display(board)

        if check_winner(board, player):
            print("Player {} wins!".format(player))
            break
        if is_draw(board):
            print("It's a draw!")
            break

        turn += 1

    again = input("Play again? (y/n): ").strip().lower()
    if again == "y":
        play()


if __name__ == "__main__":
    play()
