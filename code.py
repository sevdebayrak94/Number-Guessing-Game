import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
GAME_CONTINUE = True
easy_level_attemt = 10
hard_level_attemt = 5
actual_number = random.randint(1,100)
#Function to check user guess against actual answer

def compare(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high")
    elif user_guess < actual_answer:
        print("Too low")
    else:
        print("Bingo")
        exit()

def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        return easy_level_attemt
    else:
        return hard_level_attemt

turns = set_difficulty()
while GAME_CONTINUE:
    print(f"You have {turns} attempts remaining to guess the number")
    turns -= 1
    user_guess = int(input("Make a guess: "))
    compare(user_guess, actual_number)
    if turns == 0:
        GAME_CONTINUE = False