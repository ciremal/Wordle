import random
from colorama import init, Fore

init()


def main():
    wordbank = ['clone']
    tries = 0
    chosen_word = random.choice(wordbank)

    while tries < 6:
        print(Fore.WHITE + "", end="")
        guess = input("Please enter word: ")
        guessed_word = ["_", "_", "_", "_", "_"]
        if guess != chosen_word:
            for letter in range(5):
                if chosen_word[letter] == guess[letter]:
                    guessed_word[letter] = chosen_word[letter]
            for i in range(len(guessed_word)):
                print(Fore.GREEN + guessed_word[i], end='')
            print()

            tries += 1
        else:
            print("You win!")
            break

    if tries == 6:
        print("You lose! The word was", chosen_word)


if __name__ == "__main__":
    main()
