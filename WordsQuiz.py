#!/usr/bin/env python
# coding: utf-8

# In[57]:


import random as r
import string
import array as arr

"""Gameplay, 2 modes
mode 1: Quickplay / practice?. Choose your language then get started guessing! When you can get through all 
            the words correctly, you have won! If you quit the game, your progress will be lost. 
mode 2: Save Game: You will be able to save your progress, or come back to an existing profile. You can do a
            practice mode containing all words, or test your skills!

"""
"""
Enter a username and If it matches one from before, we can continue
quit by printing QUIT 
...
high score will print at end 
save users to a file, uname, correct words - lang, etc 

"""
#maybe 
wordsToWin = 10 #number correct to win
chances = 20 #tries until turn over 
wordslist = []
usedCorr = []
allPlayers = [] #save to csv ?
"""Load FrenchWords file"""
def loadFrench():
    txt = open("FrenchWordset.csv", "r")
    words = []
    for i in txt:
        words.append(i.rstrip('\n'))
    #print(words)
    """Create the array"""

    count = 0
    for i in words:
        a,b = i.split(",")
        wordslist.append([count,a,b])
        count+=1
    #print(wordslist)

    
class Player:
    def __init__(self, pname, french = False):
        self.name: pname
        self.fr: french
        
    known: ''

    

    ###Picking a random word
def selectWord():
    while 1:
        randPick = r.randint(0,len(wordslist)-1)
        if randPick not in usedCorr:
            return randPick
    return -1
    
    #print(randPick)
    ###definition matching 
    
def toString(arr):
    st = ''
    for i in range(0 , len(arr)-1):
        st = st + str(arr[i]) + ' '
    if(len(arr) > 1):
        st = st + str(arr[-1])
    return st 
        
    
#Remember to write a sorting algorithm 
def sort(names, lscores):
    for i in range(0,len(names)-1):
        t = lscores[i]
        s = lscores[i+1]
       
        
#Reads file of current users and prints scores in order of how many each player got correct
def displayScores():
    names = []
    lscores = []
    f = open('players.txt', 'r')
    for i in f:
        n, scores = i.split(',')
        names.append(n)
        scores = [int(s) for s in scores.split(' ')]
        lscores.append(scores)
    #print(names + lscores)
    sort(names, lscores)
    for j in range(0, len(names)):
        print("%i. %s with %i correct" %(j+1,names[j],len(lscores[j])))
    f.close()




def play():
    displayScores()
    player = input("What shall I call you? \n")
    if player in allPlayers:
        print("Welcome back %s! \n"%player)
        ##Need to load data into usedCorr for words already used correctly 
    else:
        #a new player
        print("Hello %s! \n"%player)
        
         
        
    while 1:
        language = input("Pick a language! (French) \n")
        if language == "French":
            loadFrench()
            user = Player(player, True)
            allPlayers.append(user)
            break
        else:
            print("Sorry, that isn't an option. Please Pick a supported language")
            continue
    

    while 1:
        pick = selectWord()
        row = wordslist[pick]
        guess = input("What is %s in English? \n"%row[1])
        if guess == row[2]:
            print("Correct!")
            usedCorr.append(pick)
            print(usedCorr)
            if len(usedCorr) is wordsToWin:
                print("Congratulations! You have won, good job. \n")
                sCorr = toString(usedCorr)
                f = open("players.txt","a")
                f.write('\n' + player+ ',' + sCorr)
                f.close()
                displayScores()
                break
            continue
        elif guess == 'QUIT':
            sCorr = toString(usedCorr)
            print(sCorr + '.')
            f = open("players.txt","a")
            f.write('\n' + player + ',' +  sCorr)
            f.close()
            displayScores()
            print("See you again soon! \n")
            
            break
        else:
            print("Sorry, the word means %s \n"%row[2])
            continue
        
        
play()


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




