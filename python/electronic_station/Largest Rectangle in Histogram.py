"""
You have a histogram. Try to find size of the biggest rectangle you can build out
of the histogram bars.

Input: List of all rectangles heights in histogram

Output: Area of the biggest rectangle

Example:

checkio([5]) == 5
checkio([5, 3]) == 6
checkio([1, 1, 4, 1]) == 4
checkio([1, 1, 3, 1]) == 4
checkio([2, 1, 4, 5, 1, 3, 3]) == 8

How it is used: There is no way the solution you come up with will be any useful in a real life. Just have some fun here.

Precondition:
0 < len(data) < 1000
"""


"""
  x
  x
  x
xxxx
= 1 * 4 = 4

  x
  x
xxxx
= 4 * 1 = 4

   x
  xx
  xx xx
x xx xx
xxxxxxx
= 2 * 4 = 8


x
xx
xxx
xxxx
= 2 * 3 = 3 * 2 = 6

   x
  xx
 xxx
xxxx
= 3 * 2 = 2 * 3 = 6
"""


def checkio(histogram):
    biggest = 0
    for left in range(0, len(histogram)):
        height = histogram[left]
        for right in range(left, len(histogram)):
            right_value = histogram[right]
            if right_value < height:
                height = right_value

            area = height * (right - left + 1)
            if area > biggest:
                biggest = area

    return biggest

if __name__ == '__main__':
    assert checkio([5]) == 5
    assert checkio([5, 3]) == 6
    assert checkio([1, 1, 4, 1]) == 4
    assert checkio([1, 1, 3, 1]) == 4
    assert checkio([2, 1, 4, 5, 1, 3, 3]) == 8
    print("all done")
