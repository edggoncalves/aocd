"""
The provided code uses recursion to calculate the sum of all items in the input list.

Change the code to calculate and output the sum of the squares of all the list items.


def calc(list):
    if len(list)==0:
        return 0
    else:
        return list[0] + calc(list[1:]) 

list = [1, 3, 4, 2, 5]
x = calc(list)
print(x)
"""

def calc(i):
    if len(i) == 0:
        return 0
    else:
        return (i[0] ** 2) + calc(i[1:])

i = [1, 3, 4, 2, 5]
x = calc(i)

print(x)
