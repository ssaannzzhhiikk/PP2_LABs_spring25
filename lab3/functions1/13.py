import random


n = random.randint(1, 20)
print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
num = int(input())
c = 1

while True:
    if n == num:
        print(f"Good job, {name}! You guessed my number in {c} guesses!")
        break
    if num > n:
        print("Your guess is too high")
        c+=1
    if num < n:
        print("Your guess is too low")
        c+=1
    print("Take a guess")
    num = int(input())

