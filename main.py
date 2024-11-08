import random


def ask_user():
    print("Welcome to the random number guessing game.\n")
    guessed_number = input("Please guess a number between 1 and 100: ")
    print(f"You guessed: {guessed_number}")
    return guessed_number
def number_generator():
    random_number = random.randint(0, 100)
    if random_number == guessed_number:
        print(f"Your guess was correct! The secret number was: {random_number} !\n")
        return random_number
    else:
        print(f"The secret number was: {random_number}. Go again!\n")
        
guessed_number = ask_user()
random_number = number_generator()

while guessed_number != random_number:
    ask_user()
    number_generator()