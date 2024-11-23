# Problem Set 2, hangman.py
# Name: Brandon Tan
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"
vowels = ("a", "e", "i", "o", "u")
dashes = "--------------"


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    count_of_letter_guessed = 0
    for letter in letters_guessed:
        if letter in secret_word:
            count_of_letter_guessed += secret_word.count(letter)

    if count_of_letter_guessed == len(secret_word):
        return True
    return False


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_progress = len(secret_word) * "*"
    for letter_guess in letters_guessed:
        if letter_guess in secret_word:
            """
            letters_found: To find the indexes that the letter has occurred in the secret word in a list format
            For each of the indexes that the letter appeared in, 
            replace the '*' with the letter_guess based on the index
            """
            letters_found = [i for i, val in enumerate(secret_word) if val == letter_guess]
            for letter_found in letters_found:
                word_progress_list = list(word_progress)
                word_progress_list[letter_found] = letter_guess
                word_progress = ''.join(word_progress_list)
            continue
    return word_progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    available_letters_list = list(string.ascii_lowercase)
    for letter in set(letters_guessed):
        available_letters_list.remove(letter)
    return ''.join(available_letters_list)


def letter_in_secret_word(letter, secret_word, word_progress, letter_guessed):
    """
    Check if the letter guessed is in secret word and print the respective statement
    Determine the number of guesses to be subtracted or not

    returns: the number of guess whether it has been subtracted or not
    """
    if letter in list(secret_word):
        print("Good guess: %s" % word_progress)
        return 0
    if letter_guessed.count(letter) > 1:
        print("Oops! You've already guessed that letter: %s" % word_progress)
        return 0
    else:
        print("Oops! That letter is not in my word: %s" % word_progress)
        if letter in vowels:
            return 2
        else:
            return 1


def prompt(secret_word, with_help):
    letter_guessed = list()
    guess = 10
    while not has_player_won(secret_word, letter_guessed) and not(guess <= 0):
        print(dashes)
        print("You have %s guesses left." % guess)
        print("Available letters: %s" % get_available_letters(letter_guessed))
        user_input = input("Please guess a letter:").lower()
        guess = hangman_permutation(guess, letter_guessed, secret_word, user_input, with_help)

    print(dashes)
    if has_player_won(secret_word, letter_guessed):
        return guess
    if guess <= 0:
        print("Sorry, you ran out of guesses. The word was %s." % secret_word)


def hangman_permutation(guess, letter_guessed, secret_word, user_input, with_help):
    if validate_user_input(user_input, with_help, guess):
        if with_help is True and user_input == "!":
            user_input = with_help_method(secret_word, get_available_letters(letter_guessed))
            guess -= 3
        letter_guessed.append(user_input)
        guess -= letter_in_secret_word(user_input, secret_word, get_word_progress(secret_word, letter_guessed),
                                       letter_guessed)
    else:
        word_progress = get_word_progress(secret_word, letter_guessed)
        if user_input == "!":
            print("Oops! Not enough guesses left: %s" % word_progress)
        else:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet: %s" % word_progress)
    return guess


def validate_user_input(user_input, with_help, guess):
    if user_input.isalpha():
        return True
    if with_help is True and user_input == "!":
        if guess < 3:
            return False
        return True


def with_help_method(secret_word, choose_from):
    while True:
        new = random.randint(0, len(choose_from) - 1)
        revealed_letter = choose_from[new]
        if revealed_letter in secret_word:
            print("Letter revealed: %s" % revealed_letter)
            return revealed_letter


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print("Welcome to Hangman!")
    print("I am thinking of a word that is %s letters long." % (len(secret_word)))
    guess = prompt(secret_word, with_help)
    if guess is not None:
        score_calculation(guess, secret_word)


def score_calculation(guess, secret_word):
    score = guess + len(set(secret_word)) * 4 + 3 * len(secret_word)
    print("Congratulations, you won!")
    print("Your total score for this game is: %s" % score)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

