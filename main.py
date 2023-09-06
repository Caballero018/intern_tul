#!/usr/bin/python3
"""
Module containing test cases of the highestValuePalindrome function
"""
from highestValuePalindrome import highestValuePalindrome


if __name__ == "__main__":
    """ Tests """

    # Case 0
    print("-" * 20, "Test 0", "-" * 20)
    print("highestValuePalindrome('3943', 4, 1) == '3993':")
    print("-" * 48)
    print("Output: {}".format(highestValuePalindrome('3943', 4, 1) == '3993'))

    # Case 1
    print()
    print("-" * 20, "Test 1", "-" * 20)
    print("highestValuePalindrome('092282', 6, 3) == '992299':")
    print("-" * 48)
    print("Output: {}".format(
        highestValuePalindrome('092282', 6, 3) == '992299')
        )

    # Case 2
    print()
    print("-" * 20, "Test 2", "-" * 20)
    print("highestValuePalindrome('0011', 4, 1) == '-1':")
    print("-" * 48)
    print("Output: {}".format(highestValuePalindrome('0011', 4, 1) == '-1'))
