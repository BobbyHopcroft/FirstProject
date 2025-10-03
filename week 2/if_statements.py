print("What type of book is this?")

if input() =="adventure": print("I like adventure books!")

print("Finished reading book.")


print("Please enter the activity to be performed")

if input() == "Calculations": print("Performing calculations...")
else: print("Performing activity")

print("Activity complete")

print("Towards what direction should I go (Up, down, left, right)?")
direction = input()
if direction == "up": print("I am going up")
elif direction == "down": print("I am going down")
elif direction == "left": print("I am going left")
elif direction == "right": print("I am going right")

number = int(input("Enter a number: "))
mod = number % 2
if mod > 0:
    print("The number is an odd number.")
else:
    print("The number is an even number.")

    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    if number1 > number2: print("The second number is smaller")
    elif number1 < number2: print("The second number is larger")
    elif number1 == number2: print("Both are equal!")


