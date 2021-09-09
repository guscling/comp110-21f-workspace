what = input("What beat do you want to repeat? ")
times =  input("How amny times do you want me to repeat it? ")
beat = str(what + (" ")) * (int(times))
if int(times) < 1:
    print("No beat...")
print(beat)