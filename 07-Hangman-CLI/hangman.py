import requests
url = "https://random-word-api.herokuapp.com/word"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        word = data[0]
    else:
        print("Failed to fetch data. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)

#word = "watermelon"
guess_count = 6
guess = ''
guessed_letters = ''

print("HANGMAN\nYour number of guesses is:", guess_count)

while guess_count > 0:
    fail = 0
    for char in word:
        if char in guess:
            print(char, end=' ')
        else:
            print('_', end=' ')
            fail += 1
    print()
    if fail == 0:
        print("The word is:", word)
        break
    print("Guessed characters:", sorted(guessed_letters))
    fail_guess = input("Enter your guess: ")

    if len(fail_guess) != 1 :
        print("Please enter a single letter.")
        continue

    if fail_guess in guessed_letters:
        print("You have already guessed this letter. Try another one.")
        continue

    guessed_letters += fail_guess
    guess += fail_guess  # Add the guessed character to the list of guesses

    if fail_guess not in word:
        guess_count -= 1
        print("Wrong Guess!")
        print("Number of chances left:", guess_count)
print("The word is:",word)
print("Game Over")

