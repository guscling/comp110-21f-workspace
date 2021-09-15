"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth = int(input("Depth: "))
s: str = ""
i: int = 0
while depth > i:
    trees = i
    while trees == i:
        s = s + (TREE)
        trees = trees - 1
    i = i + 1
    print(s)