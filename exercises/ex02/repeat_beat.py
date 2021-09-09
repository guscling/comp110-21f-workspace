"""Repeating a beat in a loop."""

__author__ = "730398806"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
if times < 1:
    print("No beat...")
i: int = 0
s: str = ""
while i < times:
    if i < times -1:
        s = s + (beat) + " "
        i = i + 1
    else: 
        s = s + (beat)
        i = i + 1
print(s)