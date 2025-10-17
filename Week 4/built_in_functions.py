#print("Program started")
#character = str(input("Please enter a standard character"))
#character2 = ord(character)
#if len(character) == 1: print("The ASCII code for: ", character, "is: ",character2)
#else: print("Too many characters")
#print("Program Ended")


print("Program started")
number = int(float(input("Please enter an ASCII code:")))
number2 = abs(number)
if number2 in range(32,127):
    number3 = chr(number2)
    print("The character represented by the ASCII code: ", number2, "is: ",number3)
else: print("Number not in range")
print("Program ended")


