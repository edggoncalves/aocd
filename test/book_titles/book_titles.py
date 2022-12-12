"""
You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be:H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Harry Potter
The Hunger Games
Pride and Prejudice
Gone with the Wind

Your program should output:
H12
T16
P19
G18

Hint:
The readlines() method, which returns a list containing the lines of the file.
Also, all lines, except the last one, contain a \n at the end, which should not be included in the character count.
"""


def main():
    with open('books.txt', 'r') as f:
        books = f.read().splitlines()

    for i in books:
        print(f'{i[0]}{len(i)}')


def __init__():
    if __name__ == '__main__':
        main()

main()
