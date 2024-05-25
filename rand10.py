import random


def rand7():
    return random.randint(1, 7)


def rand10():
    return rand7()


def call(par):
    for i in range(50):
        print(rand10() * par)


call(2)
