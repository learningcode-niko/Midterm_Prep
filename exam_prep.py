# Choose type of the expression : int, float, bool, NoneType, String, List, Function_or_Method
# type()
from os import remove

print(type(2+3))
print(type(6/2))
print(type(2 != 3))
print(type(5 or 6))
print(type(print(2*2)))
print(type(print))
print(type("abc".find))
print(type("bubu"*2))
print(type(["abc", 2]))
print(type("abc"[2]))
print(type("abcabcabc".split("a")))

# What is the result of the following operations
#(2+3)
#(6/2)
#(2 != 3)
#(5 or 6)
#print(2*2)
#print
#("abc".find)
#("bubu"*2)
#["abc", 2]
#("abc"[2])
#("abcabcabc".split("a"))

# 3
a = 2
b = 3
c = "abc"
print(a,b,c)
print(a,b,c,sep=",")


# open-ended questions
# Write a function that takes the name of a text file as a parameter. Print out all the 3-letter words that start with B.
import requests
def download_book(url):
    """
    Download a book from a given url
    :param url: the url to download
    :return: None
    """
    response = requests.get(url)
    print(response.status_code)
    with open("book.txt", "w", encoding="utf-8") as file:
        file.write(response.text)

download_book("https://www.gutenberg.org/cache/epub/43/pg43.txt")

def find_words(book_filename):
    """
    Find 3 letter words starting with B inside the book
    :param book_filename: Name of File containing the Book
    :return: None
    """
    found_words = []
    special_characters = ",.;:?!-—/()”"
    with open(book_filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower()
            # sanitize line by removing punctuation
            for c in special_characters:
                line = line.replace(c, "")
            words = line.split()
            for word in words:
                if word not in found_words and len(word) >= 18:
                    found_words.append(word)
    print(len(found_words))
    print(found_words)

find_words("book.txt")


# Order of Prints
a=2
b=3
c="abc"
print(a,b,c)
print(a,b,c,sep=",")
a+=2
a==5
print(a)
print(c*(a-b))
d = c.find("b")
print(d)
print(d and b)
print(d == True)
e = str(a) + str(b) + str(c) + str(d)
print(e)
print(e[1::2])
print(e+e[::-1])

# Write a function that takes an integer as parameter and returns a list of all the
# divisors of that number:
# ex: 47 -> [1,47], 28 -> [1,2,4,7,14,28]

def Divisor_finder(number):
    '''
    Finds all divisors of a given number
    :param number: Number that you want to find divisors for
    :return: List of divisors
    '''
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    return divisors
print(Divisor_finder(20))
print(Divisor_finder(560))

# Write a function that forces the user to enter a multiple of 6 number. Use try,
# except to catch invalid inputs. Return that number

def Multiple_6(number):
    '''
    Allows only multiples of 6 to be entered.
    :param number: Potential multiple of 6
    :return: None
    '''

prompt = "Choose a number: "
number = float(input(prompt))
try:
    if number % 6 == 0:
        print(int(number), "is a multiple of 6")
    else:
        print(number, "is not a multiple of 6")
except TypeError:
    print("Please enter a number")
except ValueError:
    print("Please enter an number")

# Print the multiplication table 1-10 without duplicates (if a*b=c appears, then b*a=c should not)

for a in range(1, 11):
    for b in range(a, 11):
        print(a, "*", b, "=", a*b)

# Suppose you can only do additions. Write a program that reads two positive, integer numbers a and b. It
# computes a**b.

try:
    a = input("Give me a positive integer a: ")
    a = int(a)
    b = input("Give me a positive integer b: ")
    b = int(b)

    result = 1

    for i in range(b):
        temp = 0
        for j in range(result):
            temp += a
        result = temp

    print("The result of", a, "**", b, "is", result)

except ValueError:
    print("Please give me proper positive integers")

# Read an int number. Check if the number is a palindrome. (A palindrome number read backwards has the same
# value. Example of palindrome numbers: 123454321, 999, 1598951)

try:
    num = input("Give me an integer: ")
    int(num)   # check that it is a valid integer

    if num == num[::-1]:
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")

except ValueError:
    print("Please give me a proper integer")

#Create a guessing game:
#Generate a random number between 1 and 20.
#Let the user guess until correct.
#Tell them “Too high” or “Too low”.

import random

ans = random.randint(1, 20)

while True:
    guess = input("Guess a number between 1 and 20 (type quit to exit): ")

    if guess == "quit":
        break

    guess = int(guess)

    if guess == ans:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess > ans:
        print("Too high")
    else:
        print("Too low")

#Keeps asking the user for numbers
#Stops when the user types "quit"
#Prints:
#The largest number entered
#The smallest number entered
#The average

biggest = None
smallest = None
list_of_numbers = []

while True:
    number = input("Choose a number: ")
    if number == "quit":
        break

    number = float(number)

    list_of_numbers.append(number)
    if biggest == None or number > biggest:
        biggest = number
    if smallest == None or number < smallest:
        smallest = number
    print(biggest)
    print(smallest)
    print(sum(list_of_numbers)/len(list_of_numbers))

#Asks the user to enter a sentence.
#Ignores punctuation: .,!?
#Converts everything to lowercase.
#Counts how many times each word appears.
#Prints:
#The word that appears the most
#How many times it appears
#If two words are tied for most frequent, print:

punctuation = ".,!?;"
d = {}

sentence = input("Give a sentence: ")

for p in punctuation:
    sentence = sentence.replace(p, "")

sentence = sentence.lower()

words = sentence.split()

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)
