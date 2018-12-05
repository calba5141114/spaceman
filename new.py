
import random


challngwords = ["wierd", "lateral", "diagnol",
                "unilateral", "ellipse", "eclipse", "dependencies"]
normiewords = ["cat", "mat", "rat", "pat", "eat",
               "bike", "kite", "cactus", "deli", "sandwich"]
# secret word
seckey = ""


def pick_rand(diff_level):
    try:
        if diff_level == "easy":
            return random.choice(normiewords)
        elif diff_level == "hard":
            return random.choice(challngwords)
    except Exception as e:
        print(e)


def pick_diff():
    ''' gets difficulty from user'''

    # getting user input
    try:
        diff_level = input(
            "Type game difficulty (easy or hard): ")
    except Exception as e:
        print(e)

    # checking to see if user is choosing easy or hard and relooping if they haven't
    if diff_level.lower() not in ("easy", "hard"):
        print("You cannot choose that option")
        pick_diff()
    else:
        return diff_level


def start_disp(seckey):
    init_slate = ""
    for letters in seckey:
        init_slate += "_"

    return init_slate


def display(display_text):
    print(display_text)


def game_loop(seckey):
    guesses = 7
    incorrect_bank = "Guessed: "
    guessed_words = []
    actual_word_list = []
    blank_board = start_disp(seckey)

    for letter in blank_board:
        guessed_words.append("_")
    blank_board = ""

    for letter in seckey:
        actual_word_list.append(letter)

    for items in guessed_words:
        blank_board += " _ "
    print(blank_board)

    while guesses != 0 and guessed_words != actual_word_list:

        try:
            guess = input("Guess a letter: ")
            display_word = ""
            if len(guess) > 1 or guess.isalpha() == False:
                print("Must be alphabetical or one char ")
            else:

                if guess in seckey:
                    index = seckey.find(guess)
                    guessed_words[index] = guess
                    for items in guessed_words:
                        display_word += " " + items
                    print(display_word)
                else:
                    guesses -= 1
                    incorrect_bank += guess
                    print("Thats wrong!")
                    print("You have {} incorrect guesses left".format(str(guesses)))
                    print(incorrect_bank)

        except EOFError as e:
            print("Wanna give me an {} !!!?? take it then".format(e))
            for range in random.randint(1, 30):
                print(e)

    if(guessed_words == actual_word_list):
        print("You won")
    else:
        print("You lost")
        print("The right answer was: {} ".format(seckey))


def test():
    difficulty = pick_diff()
    seckey = pick_rand(difficulty)
    game_loop(seckey)


if __name__ == "__main__":
    test()
