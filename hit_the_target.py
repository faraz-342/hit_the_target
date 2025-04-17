import random

target = random.randint(1, 100)
rounds = 0
attempts = 0

while rounds < 5:
    userChoice = input("Guess the target or Quit: ")
    if userChoice == "Q":
        break
    if not userChoice.isdigit():
        print("Enter a valid choice")
        continue
    
    userChoice = int(userChoice)
    attempts += 1
    if userChoice == target:
        print("Success: Correct Guess!!")
        rounds += 1
        target = random.randint(1, 100)  # Reset target for next round
    elif userChoice < target:
        print("Your number was too small. Take a bigger guess.")
    else:
        print("Your number was too big. Take a smaller guess.")

print("----GAME OVER----")
print("Number of valid attempts:", attempts)
print("Number of rounds played:", rounds)
