#!/usr/bin/env python
# coding: utf-8

# In[24]:


import random as r
import string
import array as arr

"""Gameplay, 2 modes
mode 1: Quickplay / practice?. Choose your language then get started guessing! When you can get through all 
            the words correctly, you have won! If you quit the game, your progress will be lost. 
mode 2: Save Game: You will be able to save your progress, or come back to an existing profile. You can do a
            practice mode containing all words, or test your skills!

"""



"""Load FrenchWords file"""
def loadFrench():
    txt = open("FrenchWordset.csv", "r")
    words = []
    for i in txt:
        words.append(i.rstrip('\n'))
    #print(words)
    """Create the array"""
    wordslist = []
    count = 0
    for i in words:
        a,b = i.split(",")
        wordslist.append([count,a,b])
        count+=1
    #print(wordslist)

    

    ###Picking a random word
def selectWord():
    while 1:
        randPick = r.randint(0,len(wordslist)-1)
        if randPick not in usedCorr:
            return randPick
    return -1
    
    #print(randPick)
    ###definition matching 
    





def practice():
    while 1:
        language = input("Pick a language! (French) \n")
        if language == "French":
            loadFrench()
            break
        else:
            print("Sorry, that isn't an option. Please Pick a supported language")
            continue
    
    usedCorr = []
    while 1:
        pick = selectWord()
        row = wordslist[pick]
        guess = input("What is %s in English? \n"%row[1])
        if guess == row[2]:
            print("Correct!")
            usedCorr.append(pick)
            print(usedCorr)
            if len(usedCorr) is 10:
                print("Congratulations! You have won, good job. \n")
                break
            continue
        else:
            print("Sorry, the word means %s \n"%row[2])
            continue
        
        
practice()


#def playGame():
    

"""

def play():
    

    
    
while 0:
    game = input("What gamemode would you like to play? Practice or Save? \n")
    if game == 'practice' or 'Practice':
        print('\n Okay! Let\'s begin! \n')
        playGame()
        continue
    elif game == 'n':
        print("\n Okay, maybe later! \n")
        continue
    elif game == 'exit':
        print("\n Bye bye! \n")
        break
    else:
        print("\n Sorry, I didnt catch that \n")
        continue


"""





    


# In[ ]:





# In[ ]:




