"""Counting letters in a string."""

__author__ = "730398806"


# Begin your solution here...
from typing import Counter


search = input("What letter do you want to search for?: ")
word = input("Enter a Word: ")
counter: int = 0
if search in word:
    counter = counter + 1
print("Count: " + str(counter))