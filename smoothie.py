import time

def make_smoothie():
    juice = input("What juice would you like? ")
    time.sleep(1)
    fruit = input("OK - and what about the fruit? ")
    time.sleep(1)
    print("Thanks. Let's go!")
    time.sleep(1)
    print("Crushing the ice...")
    time.sleep(3)
    print("Blending the " + fruit)
    time.sleep(3)
    print("Now adding in the " + juice + " juice")
    time.sleep(2)
    print("Finished! There is your " + fruit + " and " + juice + " smoothie")


print("Welcome to smoothie-matic 2.0")
another = "Y"
while another == "Y":
    make_smoothie()
    another = input("How about another(Y/N)? ")
print("Thank you for using smoothie-matic!")