#!/usr/bin/python3

import random

def ageCheck(age):
    if age > 30:
        print("you are too old\n")
        return False
    elif age<1:
        print("you are not born yet\n")
        return False
    elif age <15:
        print ('you are too young\n')
        return False
    else:
        print("you are the right age\n")
        return True

def getJokes():
    j = open("jokefile.txt")
    jj = j.read()
    jokelist=jj.split("\n%\n")
    j.close()
    return jokelist

jokes = getJokes()

def printJoke(a):
    if ageCheck(a):
        print(random.choice(jokes))

if __name__ == '__main__':
    userage = input("How old are you? ")
    printJoke(eval(userage))
