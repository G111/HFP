from random import randint
secret = randint(1, 10)

print("Welcome!")
g = input("Guess the number: ")
guess = int(g)
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
print("You won!")