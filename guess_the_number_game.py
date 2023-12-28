import random

def compareValues(n1, n2):
    if(n1 < n2): return True
    return False

print("Welcome to \"Guess the number game !!\"\n")
print("In this game, you can try to guess the number between minimum and maximum values that you have chosen.\n")

isReady = False
while (isReady == False):
    userReady = input("Are you ready ? y/n ")
    if userReady == "y":
        isReady = True

maxValue = int(input("Type maximum integer value: "))
minValue = int(input("Type minimum integer value: "))

isMinValid = compareValues(minValue, maxValue)
while (isMinValid == False):
    newMinValue = int(input("Please type minimum value smaller than maximum you have entered: "))
    if(compareValues(newMinValue, maxValue) == True): isMinValid = True

answer = random.randint(minValue, maxValue)
tryLimit = 3

for i in range(3):
    guessValue = int(input("Guess the number: "))
    if(guessValue == answer):
        print("Correct !!")
        break
    else:
        tryLimit -= 1
        if tryLimit == 0:
            print("You lose...")
        else: print("It doesn't seem to be the same...\nYou can try more " + str(tryLimit) + " times.")






