import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

game_over = False
display = ["_"] * len(chosen_word)
guessed_letters = []
print("Word to guess: " + "".join(display))

while not game_over:

    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("You can guess only a single letter at a time.")
        continue

    if guess in guessed_letters:
        print("You've  already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"The letter '{guess}' is not in the word. You lose a life!")
        if lives == 0:
            game_over = True
            print(f"The correct word was: {chosen_word}")
            print(f"****************************YOU LOSE****************************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print("Word to guess: " + "".join(display))
    print(stages[lives])