import random

words = [[1, 'Bands', ['Beatles', 'RollingStones']], [
    2, 'Countries', ['UnitedStates', 'Germany']]]

# print words[0][2][0];
random_number = random.randint(0, 1)
category = words[random_number][1]

print "Your category is " + category + '\n'

try:
    word = words[random_number][2][random.randint(0,1)]
    print "Your word has been chosen randomly"
    used_letters = []
    wrong_letters = []
except Exception as e:
    print e

def wrongCheck():
    if len(wrong_letters) >= 7:
        print "You have failed"
        exit()

def validate(letter):
    if len(letter) > 1:
        print "too long try less chars"
    elif len(letter) == 1:
        if letter in word:
            print "correct"
            used_letters.append(letter)


    