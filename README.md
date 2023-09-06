# Palindrome Exercise

![Palindrome](readmeImages/palindrome.jpg)

## Exercise

Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider **0**'s left of all higher digits in your tests. For example **0110** is valid, **0011** is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.

## Why did I choose this exercise?

I chose this exercise because it represents a stimulating challenge that will allow me to apply my skills, learn and demonstrate my ability to solve complex problems.

## How did I solve it?

Divide the code into 3 phases:

1. In case the **string** is not a palindrome, I made a loop where the first iteration points to the beginning and end of the string until it reaches the center. This is used so that in the event that the value of these spaces in memory are different, it is changed to the greater value of the two. Depending on the number of changes available. Example:

    ~~~
    list[i] = 6
    list[j] = 8
    list[i] = list[j] = max(list[i], list[j]) # 8
    ~~~

2. In case the **string** is a palindrome, I made a loop where the first iteration points to the beginning and end of the string until it reaches the center. This is used to change the value by digit **'9'** of both memory spaces. Depending on the number of changes available. Example:

    ~~~
    list[i], list[j] = 9, 9
    ~~~

3. In the case that the palindrome has gone through both processes and there are still changes to be made despite being a palindrome, returns the string even if there are still changes (k)

## How to run this code?

### Steps:

1. Give execute permission to **main.py**, so it can be executed as a script

    ~~~
    ./main
    ~~~

    This will run 3 tests, where True is that it was successful and False is that it was not.

    **STDOUT:**
    ~~~
        -------------------- Test 0 --------------------
        highestValuePalindrome('3943', 4, 1) == '3993':
        ------------------------------------------------
        Output: True

        -------------------- Test 1 --------------------
        highestValuePalindrome('092282', 6, 3) == '992299':
        ------------------------------------------------
        Output: True

        -------------------- Test 2 --------------------
        highestValuePalindrome('0011', 4, 1) == '-1':
        ------------------------------------------------
        Output: True
    ~~~
