"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking
the spaces in a 3x3 grid. The player who succeeds in placing three respective marks in a horizontal,
vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results.
You are given a result of a game and you must determine if the game ends in a win or a draw as well
as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins.
If the game is a draw, return "D".

x-o-referee

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Example:

checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"

How it is used: The concepts in this task will help you when iterating data types.
They can also be used in game algorithms, allowing you to know how to check results.

How to use TryIt:

Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
"""

import pprint

def check_position(game_result, position):
    winner = ' '
    for square in position:
        current = game_result[square[1]][square[0]]
        if current == '.':
            return ' '
        elif winner == ' ':
            winner = current
        elif winner != current:
            return ' '
    return winner

def checkio(game_result):
    winning_positions = [[(i, j) for j in range(3)] for i in range(3)] + \
        [[(j, i) for j in range(3)] for i in range(3)] + \
        [[(j, j) for j in range(3)]] + \
        [[(j, 2 - j) for j in range(3)]]

    for position in winning_positions:
        pprint.pprint(position)
        winner = check_position(game_result, position)
        if winner != ' ':
            print(winner)
            return winner

    return "D"

if __name__ == '__main__':
    assert checkio([
        "...",
        "XXX",
        "OO."]) == "X", "Xs wins"

    print ("all done")
