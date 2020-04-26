import random as r
import string
import array as arr

"""Load FremchWords file"""
txt = open("FrenchWordset.csv", "r")
words = []
for i in txt:
    words.append(i.rstrip('\n'))
print(words)
