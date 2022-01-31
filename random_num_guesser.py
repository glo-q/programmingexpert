import random

first = input("Enter the start of the range: ")
while not first.isdigit():
    print("Please enter a valid number.")
    first = input("Enter the start of the range: ")
second = input("Enter the end of the range: ")
while not second.isdigit() or int(second) < int(first) or int(first) == int(second):
    print("Please enter a valid number.")
    second = (input("Enter the end of the range: "))

random_num = random.randint(int(first), int(second))

game = None
i = 0
while game != random_num:
    guess = input("Guess a number: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    i += 1
    game = int(guess)

if i == 1:
    print(f"You guessed the number in {i} attempt")
else:
    print(f"You guessed the number in {i} attempts")
