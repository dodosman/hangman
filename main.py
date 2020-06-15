from words import words_list
import random


def get_word():
    word = random.choice(words_list)
    return word.upper()


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    print("Let's play hangman!")
    print(tries)
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("What letter do you think is in a covered word?: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already given letter: ", guess)
            elif guess not in word:
                print(guess," is not in concealed word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, " is in the correct word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed the word', guess)
            elif guess != word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print(tries)
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed it, the word has been", word)
    else:
        print("sorry, you run out of tries.The word was: ", word)


def main():
    word = get_word()
    play(word)
    while input("Do you wanna play again(Y/N?)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
