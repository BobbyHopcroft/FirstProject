remove = int(input("How many apples should I remove?"))
removed = 0

while removed < remove:
    print("Removed apple")
    removed = removed + 1

obstacles_avoided = int(input("How many obstacles must I avoid?"))
obstacles = 0
obstacles2 = 0

while obstacles < obstacles_avoided:
    obstacles2 = obstacles2 + 1
    print("Avoiding...Done!: ",obstacles2," obstacles avoided.")
    obstacles = obstacles + 1

bars_charged = int(input("How many bars should be charged?"))
bars = 0
while bars_charged > bars :
    bars = bars + 1
    print("Charging..." + "I" * bars)

if bars_charged == bars :
    print("The battery is fully charged")

letter = str(input("What is your phrase?"))
letter_count = len(letter)
i = 0
while i < letter_count :
    print("Hi " * letter_count)
    i = i + letter_count








