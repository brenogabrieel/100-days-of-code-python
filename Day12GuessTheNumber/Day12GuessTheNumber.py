import random
import art

print(art.logo_guessthenumber)
end_of_game = False
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
correct_number = random.randrange(1, 100)
guesses_easy = 5
guesses_hard = 10
print(f"Pssst, the correct answer is {correct_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while not end_of_game:
    if difficulty == "easy":
        guesses = 10
        guess_make = int(input("Make a guess: "))
        if guess_make != correct_number:
            guesses_easy -= 1
            if guess_make > correct_number:
                print("Too high.\nGuess again.")
            elif guess_make < correct_number:
                print("Too low.\nGuess again.")
        elif guess_make == correct_number:
            print(f"You got it! the answer was {correct_number}.")
            end_of_game = True
            break
        print(f"You have {guesses_easy} attempts remaining to guess the number.")
    elif difficulty == "hard":
        guess_make = int(input("Make a guess: "))
        if guess_make != correct_number:
            guesses_hard -= 1
            if guess_make > correct_number:
                print("Too high.\nGuess again.")
            elif guess_make < correct_number:
                print("Too low.\nGuess again.")
        elif guess_make == correct_number:
            print(f"You got it! the answer was {correct_number}.")
            end_of_game = True
            break
        print(f"You have {guesses_hard} attempts remaining to guess the number.")

