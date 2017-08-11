"""
“Looking at the sky, he suddenly saw that it had become black. Then white again, but with great rippling circles. The circles were vultures wheeling around the sun. The vultures disappeared, to be replaced by checkers squares ready to be played on. On the board, the pieces moved around incredibly rapidly, winning dozens of games every minute. They were scarcely lined up before they started rushing at each other again, banging into each other, forming fighting combinations, wiping the other side out in the wink of an eye. Then the squares scattered, giving way to the grille of a crossword puzzle, and here, too, words flashed, drove each other away, clustered, were erased. They were all very long words, like Catalepsy, Thunderbird, Superrequeteriquísímo and Anticonstitutionally.”
― Jean-Marie G. Le Clézio, The Book of Flights

A crossword is a word puzzle that normally takes the form of a square or a rectangular grid of white and black shaded squares. The goal is to fill the white squares with letters, forming words or phrases, by solving clues which lead to the answers. In languages that are written left-to-right, the answer words and phrases are placed in the grid from left to right and from top to bottom. The shaded squares are used to separate the words or phrases.

We will solve a few crosswords which have a lattice-like structure, with a higher percentage of shaded squares, leaving up to half the letters in an answer unchecked. For example, if the top row has an answer running all the way across, there will be no across answers in the second row. Your program receives a crossword pattern without clues and numbers, and it should determine word positions itself with the following rules:
- If a cell is placed in the most left column or neighbour left cell is shaded, and the neighbouring right cell is empty, then this cell is the beginning of left-to-right word;
- If a cell is placed in the top row or the neighbouring upward cell is shaded, and neighbour down cell is empty, then this cell is the beginning of up-to-down word.
All words have a length greater than or equal to 3 letters. All empty cells should filled in.

You are given a crossword as a sequence of strings, where "X" is a shaded cell and "." is an empty cell. You are also given the predefined list of words in lowercase. (You can find it here or in the default code). This list is the same for all crosswords and contains about 1500 nouns. You should use only the given words.

You don't need to find all of the possible solutions. It will be enough to find any solution which fills the crossword puzzle and contains the correct words.

crossword

Input: Two arguments. A crossword as a tuple of strings and the words as a tuple of strings.

Output: Any solved variant of the crossword as a tuple/list of strings.

Example:

solver(('.XXX.', '...X.', '.X.X.', '.....'))

1
2
How it is used: This is a classic constraint satisfaction problem and can save you time with the daily crosswords.

Precondition:
3 < len(crossword) ≤ 10
all(3 < len(row) ≤ 10 and len(row) == len(crossword[0]) for row in crossword)


"""