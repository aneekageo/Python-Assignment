from colorama import Back, Fore, Style
import random
import pathlib

words = pathlib.Path("word_list.txt").read_text(encoding="utf-8").strip().split('\n')
check = pathlib.Path("wordle.txt").read_text(encoding="utf-8").strip().split('\n')

word = random.choice(words)

def color_background(word, target_letter, background_color):
    return "".join([f"{Back.__dict__[background_color]}{Fore.WHITE}{char}{Style.RESET_ALL}"
                    if char.lower() == target_letter.lower() else char for char in word])

print("Randomly chosen word:", word)

chances = 6
while chances > 0:
    print("###### YOU HAVE {0} CHANCES LEFT #######".format(chances))
    guess = input("Enter a 5-letter guess: ")
    chances -= 1

    if len(guess) != 5:
        print("Please guess a 5-letter word")
    elif word not in check:
        print("Enter a valid word from wordle.txt")
    elif guess == word:
        print("You guessed the correct word!")
        break
    else:
        for letter in guess:
            if letter.lower() == word[guess.find(letter)].lower():
                print(color_background(guess, letter, 'GREEN'))
            elif letter.lower() in word.lower():
                print(color_background(guess, letter, 'YELLOW'))
            else:
                print("Letter {0} not found in the word".format(letter))
