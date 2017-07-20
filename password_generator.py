#!/usr/bin/python3

import random

fo = open("final.txt", "r")
list_words = []
for word in fo:
    word = word.rstrip('\n')
    # print("{}".format(type(word)))
    list_words.append(word)
password = ""

for i in range(0, 4):
    index = len(list_words)
    while index >= len(list_words):
        index = random.SystemRandom().getrandbits(14)
    password += str(list_words[index]) + " "

print("Password: {}".format(password))
