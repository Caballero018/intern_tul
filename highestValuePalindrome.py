"""
Module to calculate the largest possible palindrome with limited changes.
"""


def highestValuePalindrome(s: str, n: int, k: int) -> str:
    """
    Finds the largest palindrome obtainable from a given string 's',
    making a maximum of 'k' digit shifts

    Keyword arguments:
    s (str): a string representation of an integer
    n (int): the lenght of the integer string
    k (int): the maximum number of changes allowed

    Return:
    string: a string representation of the highest value achievable or '-1'
    """
    if n < 0 or n > 10 ** 5 or k < 0 or k > 10 ** 5 or not s.isdigit() \
            or type(s) != str or type(n) != int or type(k) != int:
        return '-1'

    if n <= k:
        return '9' * n

    if k == 0 and s == s[::-1]:
        return ''.join(s)
    elif k == 0:
        return '-1'

    """
    Process that checks if the given string is different from its
    inverse form and if so, changes the value of the space in memory
    of 's[i]' or 's[j]' to the greater value of one of the two
    """
    s = list(s)
    indexList = []

    if s != s[::-1] and k > 0:
        for i in range(n // 2):
            if k == 0:
                break

            j = n - 1 - i
            if i >= j:
                break
            if k > 0 and i < j:
                if s[i] != s[j]:
                    indexList.append(i)
                    s[i] = s[j] = max(s[i], s[j])
                    k -= 1

    """
    Process that, in case the list is a palidrome, replaces its digits
    with '9' according to the number of changes available (k)
    """
    if s == s[::-1] and k > 0:
        for i in range(n // 2):
            if k == 0:
                break

            j = n - 1 - i
            if i >= j:
                break
            if k > 0 and i < j:
                if s[i] != '9':
                    if i in indexList:
                        k += 1
                        indexList.remove(i)
                    if k > 1:
                        s[i], s[j] = '9', '9'
                        k -= 2
                    if i + 1 == j - 1 and k > 0 and s[i + 1] != '9':
                        s[i + 1] = '9'
                        k -= 1

    if s == s[::-1] and k > 0:
        return ''.join(s)

    if k == 0 and s == s[::-1]:
        return ''.join(s)

    return '-1'
