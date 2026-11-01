import os
import random
import wordlist
import art


end_of_game = False


chosen_word = random.choice(wordlist.word_list)
word_length = len(chosen_word)
lives = 6
print(art.logo_hangman)
print(f'Pssst, the solution is {chosen_word}.')
print(art.stages_hangman[lives])
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
        print(art.stages_hangman[lives])
        if lives == 0:
            print("You lose.")
            end_of_game = True
            break
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")
