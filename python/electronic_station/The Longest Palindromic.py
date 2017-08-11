"""
Write a function that finds the longest palindromic substring of a given string.
Try to be as efficient as possible!

If you find more than one substring you should return the one which is closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.

Precondition: 1 < |text| <= 20
The text contains only ASCII characters.
"""

"""
abbac

"""

def is_palindrom(text):
    for i in range(0, len(text) / 2):
        if text[i] != text[-i - 1]:
            return False
    return True

def checkio(palindrom):
    longest = ""
    for i in range(0, len(palindrom)):
        for j in reversed(range(i + 1, len(palindrom) + 1)):
            a = palindrom[i:j]
            if is_palindrom(a):
                if len(a) > len(longest):
                    longest = a
                break;

    return len(longest)

if __name__ == '__main__':
    assert checkio('test') == 1
    assert checkio('abbc') == 2
    assert checkio('bcbd') == 3
    assert checkio('abcdcbb') == 5
    print ("all done")
