"""This program performs simple boolean operations on inputed integers"""

__author__ = "730398806"

left = input("Left-hand side: ")
right = input("Right-hand side: ") 
left_int = int(left)
right_int = int(right)
print((left) + (" < ") + (right) + (" is ") + str(left_int < right_int))
print((left) + (" >= ") + (right) + (" is ") + str(left_int >= right_int))
print((left) + (" == ") + (right) + (" is ") + str(left_int == right_int))
print((left) + (" != ") + (right) + (" is ") + str(left_int != right_int))