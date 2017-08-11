"""
In this time, you need to implement the solver of Lights Out the puzzle.

rule of the puzzle :

This puzzle uses 5x5 grid. Each panel has two state ( light on or off ).
if you click a panel, the panel and adjacent (4 directions) panels will flip. ( on <=> off )
The goal is all panels lights off.


Input: ON-state panels as a list of Integers.

Output: Clicked panels as a list of Integers.

Example:

wall_keeper([5, 7, 13, 14, 18]) == [2, 6, 7, 8, 10, 12, 15, 18, 24, 25]
1
How it is used: Get the puzzle's automatic answer.

Precondition:
all([1 <= p <= 25 for p in on_panels])
It does not have to be the shortest answer
"""

