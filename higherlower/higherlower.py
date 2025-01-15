import random
from art import logo, vs
from data import data

def format_output(c1, c2, score):
    print("\n" * 20)
    print(logo)
    if score > 0:
        print(f"Correct! Current score: {score}")
    print(f"Compare A: {c1['name']}, a {c1['description']}, from {c1['country']}")
    print(vs)
    print(f"Against B: {c2['name']}, a {c2['description']}, from {c2['country']}")

def play_game(score, prev_ch):
    if prev_ch:
        choice1 = prev_ch
    else:
        choice1 = random.choice(data)
    choice2 = random.choice(data)
    if choice1["follower_count"] > choice2["follower_count"]:
        answer = "a"
        prev_ch = choice1
    else:
        answer = "b"
        prev_ch = choice2
    format_output(choice1, choice2, score)
    return [answer, prev_ch]

game_over = False
score = 0
prev_choice = None

while not game_over:
    answer, prev_choice = play_game(score, prev_choice)
    user_choice = input(f"Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == answer:
        score += 1
    else:
        game_over = True
        print("\n" * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")