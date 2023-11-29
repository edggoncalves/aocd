import re


# your code goes here
def search(tag: str):
    pattern = '[A-Z][A-Z][0-9][0-9]'
    if len(tag) == 4 and re.search(pattern, tag):
        print('Searching')
    else:
        print('Wrong format')


Id = input()
search(Id)

"""
All the products in online shop have their own ID. Every ID consists of 4 symbols:
The first symbol: an uppercase character
The second symbol: an uppercase character
The third symbol: a digit
The forth symbol: a digit

Write a program for a search tool, that will take the ID as input and output "Searching" if the format is correct, and "Wrong format", if it's not.

Sample Input
LG17

Sample Output
Searching
"""
