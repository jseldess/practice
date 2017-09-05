import random

def play_hangman():
    while len(alphabet) > 0:
        guess = raw_input("\nGUESS A LETTER: ")
        check_guess(guess)

def check_guess(guess):
    if len(guess) > 1 or guess.isalpha() is False:
        print("ENTER A SINGLE LETTER OF THE ALPHABET.\n")
    elif guess not in alphabet:
        print("YOU ALREADY TRIED THAT LETTER. PICK ANOTHER.\n")
    elif guess in solution:
        fill_correct_answer(guess)
    else:
        reject_wrong_answer(guess)

def fill_correct_answer(guess):
    global right_guesses, alphabet
    count = solution.count(guess)
    index = solution.index(guess)
    right_guesses[index] = guess
    while count > 1:
        index = solution.index(guess, index + 1)
        right_guesses[index] = guess
        count -= 1
    if " ".join(right_guesses) != " ".join(solution):
        print("\nGOOD GUESS!\nAnswer: " + " ".join(right_guesses))
        alphabet.replace(guess, "")
    else:
        print("\nYOU DID IT!\nAnswer: " + " ".join(right_guesses))
        alphabet = ""

def reject_wrong_answer(guess):
    global wrong_count, alphabet
    wrong_guesses.append(guess)
    alphabet.replace(guess, "")
    wrong_count += 1
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
        print("NOPE! TRY AGAIN. Wrong guesses:" + str(sorted(wrong_guesses)))
        print("Answer: " + " ".join(right_guesses) + "\n")
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
        print("NOPE! TRY AGAIN. Wrong guesses:" + str(sorted(wrong_guesses)))
        print("Answer: " + " ".join(right_guesses))
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
        print("NOPE! TRY AGAIN. Wrong guesses:" + str(sorted(wrong_guesses)))
        print("Answer: " + " ".join(right_guesses))
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
        print("NOPE! TRY AGAIN. Wrong guesses:" + str(sorted(wrong_guesses)))
        print("Answer: " + " ".join(right_guesses))
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
        print("NOPE! TRY AGAIN. Wrong guesses:" + str(sorted(wrong_guesses)))
        print("Answer: " + " ".join(right_guesses))
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
        alphabet = ""

while True:
    words = ["telephone", "whale", "pancakes", "beach", "dancer"]
    solution = list(random.choice(words))
    right_guesses = ["_" for x in solution]
    wrong_guesses = []
    wrong_count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    play_hangman()
    restart = raw_input("\nWant to play again? (y/n)\n")
    if restart != "y":
        break
