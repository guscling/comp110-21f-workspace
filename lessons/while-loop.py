counter: int = 0
maximum: int = int(input("count up to what?"))
while counter <= maximum:
    counter_sqaured: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_sqaured))
    counter = counter + 1
print("Done")