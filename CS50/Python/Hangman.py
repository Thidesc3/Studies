import random
def generate_word():
    # Generate a random number between 1 and 26 to determine the letter of the word
    num = random.randint(1, 26)
    # Convert the number to a letter of the alphabet (A-Z)
    letter = letters[num]
    # Return the letter as a string
    return letter

def guess_letter():
    # Get the letter the player wants to guess from the input() function
    guess = input("Guess a letter: ")
    # Check if the letter is in the word
    if guess in word:
        # If the letter is in the word, reveal its position and update the word
        position = word.find(guess)
        print(f"{guess} is in the {position} position!")
        word = word[:position] + word[position+1:]
    else:
        # If the letter is not in the word, add a part to the hangman figure
        hangman_figure += "__"
        print("Sorry, that letter is not in the word.")

def main():
    # Create the word for the player to guess
    word = generate_word()
    # Initialize the hangman figure
    hangman_figure = ""
    # Loop until the player has correctly guessed the word or the hangman figure is complete
    while True:
        # Ask the player to guess a letter
        guess = input("Guess a letter: ")
        # Check if the letter is in the word and update the word if it is, or add a part to the hangman figure if it is not
        if guess_letter():
        # If the letter is in the word, update the word and ask the player to guess another letter.
            print("Correct!")
        else:
            # Otherwise, add a part to the hangman figure.
            hangman_figure += "__"
            print("Sorry, that letter is not in the word.")
# Ask the player to play again if they want to continue
play_again = input("Do you want to play again? (y/n): ")
if play_again.lower() == "y":
    # Loop back to the beginning and start a new game.
    main()
else:
    # Otherwise, exit the program.
    print("Goodbye!")
