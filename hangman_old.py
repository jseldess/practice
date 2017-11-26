import random
from pynput.keyboard import Key, Controller

words = ["mama", "tortoise", "germany", "banana", "panda", "swimming", "seepferdchen"]

def play_hangman():
    solution = list(random.choice(words))
    right_guesses = ["_" for x in solution]
    wrong_guesses = []
    wrong_count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while len(alphabet) > 0:
        guess = raw_input("GUESS A LETTER: ")
        if len(guess) > 1 or guess.isalpha() is False:
            print("\nENTER A SINGLE LETTER OF THE ALPHABET.")
            print("Answer: " + " ".join(right_guesses) + "\n")
            continue
        elif guess not in alphabet:
            print("\nYOU ALREADY TRIED THAT LETTER. PICK ANOTHER.")
            print("Answer: " + " ".join(right_guesses) + "\n")
            continue
        elif guess in solution:
            count = solution.count(guess)
            index = solution.index(guess)
            right_guesses[index] = guess
            while count > 1:
                index = solution.index(guess, index + 1)
                right_guesses[index] = guess
                count -= 1
            if " ".join(right_guesses) != " ".join(solution):
                print("\nGOOD GUESS!\nAnswer: " + " ".join(right_guesses) + "\n")
                alphabet = alphabet.replace(guess, "")
                continue
            else:
                print("\nYOU DID IT!\nAnswer: " + " ".join(right_guesses) + "\n")
                break
        else:
            wrong_guesses.append(guess)
            alphabet = alphabet.replace(guess, "")
            wrong_count +=1
            if wrong_count == 1:
                print("""
                            ________________________________
                           |                      \         |
                           |                       \        |
                           |                        \       |
                           |                         \      |
                          _|_                         \     |
                         /   \                         \    |
                         \___/                          \   |
                                                         \  |
                                                          \ |
                                                           \|
                                                            |
                                                            |
                                                            |
                                                            |
                                                            |
                                                            |
                                                            |
                                                 ___________|
                                                 """)
                print("NOPE! TRY AGAIN. Wrong guesses: " + str(sorted(wrong_guesses)))
                print("Answer: " + " ".join(right_guesses) + "\n")
                continue
            if wrong_count == 2:
                print("""
                            ________________________________
                           |                      \         |
                           |                       \        |
                           |                        \       |
                           |                         \      |
                          _|_                         \     |
                         /   \                         \    |
                         \___/                          \   |
                           |                             \  |
                           |                              \ |
                           |                               \|
                           |                                |
                           |                                |
                                                            |
                                                            |
                                                            |
                                                            |
                                                            |
                                                 ___________|
                                                 """)
                print("NOPE! TRY AGAIN. Wrong guesses: " + str(sorted(wrong_guesses)))
                print("Answer: " + " ".join(right_guesses) + "\n")
                continue
            if wrong_count == 3:
                print("""
                            ________________________________
                           |                      \         |
                           |                       \        |
                           |                        \       |
                           |                         \      |
                          _|_                         \     |
                         /   \                         \    |
                         \___/                          \   |
                           |  /                          \  |
                           | /                            \ |
                           |/                              \|
                           |                                |
                           |                                |
                                                            |
                                                            |
                                                            |
                                                            |
                                                            |
                                                 ___________|
                                                 """)
                print("NOPE! TRY AGAIN. Wrong guesses: " + str(sorted(wrong_guesses)))
                print("Answer: " + " ".join(right_guesses) + "\n")
                continue
            if wrong_count == 4:
                print("""
                            ________________________________
                           |                      \         |
                           |                       \        |
                           |                        \       |
                           |                         \      |
                          _|_                         \     |
                         /   \                         \    |
                         \___/                          \   |
                        \  |  /                          \  |
                         \ | /                            \ |
                          \|/                              \|
                           |                                |
                           |                                |
                                                            |
                                                            |
                                                            |
                                                            |
                                                            |
                                                 ___________|
                                                 """)
                print("NOPE! TRY AGAIN. Wrong guesses: " + str(sorted(wrong_guesses)))
                print("Answer: " + " ".join(right_guesses) + "\n")
                continue
            if wrong_count == 5:
                print("""
                            ________________________________
                           |                      \         |
                           |                       \        |
                           |                        \       |
                           |                         \      |
                          _|_                         \     |
                         /   \                         \    |
                         \___/                          \   |
                        \  |  /                          \  |
                         \ | /                            \ |
                          \|/                              \|
                           |                                |
                           |                                |
                            \                               |
                             \                              |
                              \                             |
                                                            |
                                                            |
                                                 ___________|
                                                 """)
                print("NOPE! TRY AGAIN. Wrong guesses: " + str(sorted(wrong_guesses)))
                print("Answer: " + " ".join(right_guesses) + "\n")
                continue
            if wrong_count == 6:
                print("""
                            ________________________________
                           |                      \         |
                           |                       \        |
                           |                        \       |
                           |                         \      |
                          _|_                         \     |
                         /   \                         \    |
                         \___/                          \   |
                        \  |  /                          \  |
                         \ | /                            \ |
                          \|/                              \|
                           |                                |
                           |                                |
                          / \                               |
                         /   \                              |
                        /     \                             |
                                                            |
                                                            |
                                                 ___________|
                                                 """)
                print("SORRY, YOU LOSE.")
                break

while True:
    play_hangman()
    restart = raw_input("Want to play again? (y/n) ")
    if restart != "y":
        print("Bye!")
        break
    keyboard = Controller()
    with keyboard.pressed(Key.cmd):
      keyboard.press("r")
