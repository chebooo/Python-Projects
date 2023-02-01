import random

def choose_word():
  # This function chooses a random word from a list of words
  words = ["hangman", "python", "code", "game"]
  return random.choice(words)

def play_hangman():
  # This is the main game loop
  word = choose_word()
  word_letters = set(word)
  alphabet = set("abcdefghijklmnopqrstuvwxyz")
  used_letters = set()
  tries = 6

  while True:
    # Print the current state of the game
    print("Word: ", end="")
    for letter in word:
      if letter in used_letters:
        print(letter, end="")
      else:
        print("_", end="")
    print("\n")
    print("Tries: ", tries)

    # Get the player's next guess
    print("Available letters: ", "".join(alphabet - used_letters))
    guess = input("Please enter your next guess: ")
    guess = guess.lower()

    # Check if the input is valid
    if not guess in alphabet:
      print("Invalid input, please try again.")
      continue
    elif guess in used_letters:
      print("You have already used that letter, please try again.")
      continue

    # Update the game state
    used_letters.add(guess)
    if guess in word_letters:
      print("Good guess!")
      if not word_letters - used_letters:
        print("You win!")
        break
    else:
      print("Sorry, that letter is not in the word.")
      tries -= 1
      if not tries:
        print("You lose! The word was " + word)
        break

# Start the game
play_hangman()
