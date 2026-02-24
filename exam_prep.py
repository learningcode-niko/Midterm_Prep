# Choose type of the expression : int, float, bool, NoneType, String, List, Function_or_Method
# type()
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
(2+3)
(6/2)
(2 != 3)
(5 or 6)
print(2*2)
print
("abc".find)
("bubu"*2)
["abc", 2]
("abc"[2])
("abcabcabc".split("a"))

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
