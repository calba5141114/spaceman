import random

# List of words and categories to pick from
words = [[1, 'Bands', ['Beatles', 'RollingStones']], [
    2, 'Countries', ['UnitedStates', 'Germany']]]

# Initializing neccessary arrays
used_letters = []
wrong_letters = []

# Random Index
random_number = random.randint(0, 1)

# Initializing and Assigning a variable for a category and word
category = words[random_number][1]
word = words[random_number][2][random.randint(0, 1)]
print "Your category is " + category + '\n'
print "Your word has been chosen randomly"

# Checking the wrong letters list and exiting the program loop if this condition is true


def wrong_check():

    if len(wrong_letters) >= 7:
        print "You have failed"
        exit()

# the actual validation of a letter
# @Dylan add more if statemnts

def validate(letter):

    if len(letter) > 1:

        print "too long try less chars"
        input_data()

    elif len(letter) == 1:

        if letter in used_letters:

            print "try not reusing the same chars."
            input_data()

        elif letter in word:

            print "correct"
            used_letters.append(letter)

        elif letter not in word:

            print letter + " Is not in the word"
            used_letters.append(letter)
            wrong_letters.append(letter)
            wrong_check()
            input_data()

# collects and validates code.


def input_data():

    input_x = raw_input('Enter A letter')
    validate(input_x)

input_data()