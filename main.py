import random

words = [[1, 'Bands', ['Beatles', 'RollingStones']], [
    2, 'Countries', ['UnitedStates', 'Germany']]]

# print words[0][2][0];
random_number = random.randint(0, 1)
category = words[random_number][1]

print "Your category is " + category + '\n'

try:
    word = words[random_number][2][random.randint(0, 1)]
    print "Your word has been chosen randomly"
    used_letters = []
    wrong_letters = []
except Exception as e:
    print e


def wrong_check():
    if len(wrong_letters) >= 7:
        print "You have failed"
        exit()


def input_data():
    input_x = raw_input('Enter A letter')
    validate(input_x)


def validate(letter):
    if len(letter) > 1:
        print "too long try less chars"
    elif len(letter) == 1:
        if letter in used_letters:
            print "try nbot reusing the same chars"
            input_data()
        elif letter in word:
            print "correct"
            used_letters.append(letter)
            print
        elif letter is not in word:
            print letter " Is not in the word"
            used_letters.append(letter)
            wrong_letters.append(letter)
            wrong_check()
