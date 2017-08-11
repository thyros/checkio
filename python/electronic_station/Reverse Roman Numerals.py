"""
In the CheckiO mission Roman Numerals you have to convert a decimal number into its
representation as a roman number. Here you have to do the same but the other way around.

You are given a roman number as a string and your job is to convert this
number into its decimal representation.

A valid roman number, in the context of this mission, will only contain roman numerals as per
the below table and follows the rules of the substractive notation.
Check this Wikipedia article for more details about how to form roman numerals.

Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)
Input: A roman number as a string.

Output: The decimal representation of the roman number as an int.

Example:

reverse_roman('VI') == 6
reverse_roman('LXXVI') == 76
reverse_roman('CDXCIX') == 499
reverse_roman('MMMDCCCLXXXVIII') == 3888

Precondition:
len(roman_string) > 0
all(char in "MDCLXVI" for char in roman_string) == True
0 < reverse_roman(roman_string) < 4000
"""

def reverse_roman(roman_string):
    roman_numbers = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], \
                     ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], \
                     ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
    result = 0
    while roman_string:
        for roman_number in roman_numbers:
            if roman_string.startswith(roman_number[0]):
                result += roman_number[1]
                roman_string = roman_string[len(roman_number[0]):]
                break
    return result

if __name__ == '__main__':
    assert reverse_roman('I') == 1
    assert reverse_roman('VI') == 6
    assert reverse_roman('LXXVI') == 76
    assert reverse_roman('CDXCIX') == 499
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888
    print("all done")