"""
Our Robo-Trio need to train for future journeys and treasure hunts.
Stephan has built a special flat model of a pyramid.
Now the robots can train for speed gold running.
They start at the top of the pyramid and must collect gold in each room,
choose to take the left or right path and continue down to the next level.
To optimise their gold runs, Stephan need to know the maximum amount of gold that
can be collected in one run.

Consider a tuple of tuples in which the first tuple has one integer and each
consecutive tuple has one more integer then the last. Such a tuple of tuples would look
like a triangle. You should write a program that will help Stephan find the highest
possible sum on the most profitable route down the pyramid. All routes down the pyramid
involve stepping down and to the left or down and to the right.

Tips: Think of each step down to the left as moving to the same index location or
to the right as one index location higher. Be very careful if you plan to use recursion here.

Input: A pyramid as a tuple of tuples. Each tuple contains integers.

Output: The maximum possible sum as an integer.

How it is used: This is a classical problem which shows you how to use dynamic programming.
This concept is a core component of many optimisation tasks.

Precondition: 0 < len(pyramid) <= 20
all(all(0 < x < 10 for x in row) for row in pyramid)
"""


"""
1
2 3
4 5 6
7 8 9 0

                1
       3                  4
   7       [8       9]         10
14    [15 16 17]   [17 18 19]    10
"""

def count_gold(golden_pyramid):
    counts = []
    for row in golden_pyramid:
        if len(row) == 1:
            counts = [row]
        else:
            new_counts = []
            for i, value in enumerate(row):
                print(str(i) + " len(counts): " + str(len(counts)))
                current = []

                if i >= 1:
                    for l in counts[i - 1]:
                        current.append(l + value)

                if i < len(counts):
                    for r in counts[i]:
                        current.append(r + value)

                print(current)

                new_counts.append(current)

            counts = new_counts
        print(counts)

    m = 0
    for x in counts:
        m = max(m, max(x))
    return m

if __name__ == '__main__':

    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18
    print ("all done")
