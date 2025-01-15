import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

placeholder = ""

for c in chosen_word:
    placeholder += "_"

print(f"Word to guess: {placeholder}")

game_over = False
lives = 6

print(f"**** Lives left: {lives} ****")

correct_letters = []

while not game_over:
    display = ""
    guessed_letter = input("Guess a letter: ").lower()
    present_in_word = False

    if guessed_letter in correct_letters:
        print("Letter already guessed")
        continue

    if guessed_letter not in chosen_word:
        print("Letter not in word")
        lives -= 1
        print(f"Lives left: {lives}")
    else:
        for c in chosen_word:
            if guessed_letter == c:
                display += c
                correct_letters.append(c)
                present_in_word = True
            elif c in correct_letters:
                display += c
            else:
                display += "_"
            
            if display == chosen_word:
                game_over = True
                print("You win!")
                break

    if lives == 0:
        game_over = True
        print(f"You lose! Correct word was: {chosen_word}")
        break

    print(display)