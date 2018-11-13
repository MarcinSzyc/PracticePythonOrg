"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

word = input("Please provide your text here: ")

if word.lower() == word[::-1].lower():
    print('Your word {} is a palindrome'.format(word))
else:
    print('Word {} is not a palindrome'.format(word))