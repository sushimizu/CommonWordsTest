#!/usr/bin/env python
# coding: utf-8

# In[57]:


import random as r
import string
import array as arr
import pandas as pd

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
wordsListJ = []
usedCorrJ = []
allPlayers = [] #save to csv ?
selectedLanguage = None
playerData = pd.read_csv("players.csv")

"""Load FrenchWordset file"""
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

"""Load JapaneseWordset file"""
def loadJapanese():
    txt = open("JapaneseWordset.csv", "r")
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
    #No longer in use 
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


def displayScoresFr(playerData):
    #players = playerData.sort_values(["FrenchCount"], ascending=False)
    playersfr = playerData.sort_values(["FrenchCount"], ascending=False)
    playersfr = playersfr[["Name","FrenchCount"]]
    playersfr = playersfr.reset_index(drop=True)
    print("\n High Scores: \n")
    print("Player","          " ,"Score")
    if playersfr["Name"].size < 5:
        for i in range (0,playersfr["Name"].size):
         print(playersfr["Name"][i], "          ", playersfr["FrenchCount"][i])
    else:
        for i in range(0,4):
            print(playersfr["Name"][i], "          ", playersfr["FrenchCount"][i])
     
def displayScoresJp(playerData):
    #players = playerData.sort_values(["FrenchCount"], ascending=False)
    playersjp = playerData.sort_values(["JapaneseCount"], ascending=False)
    playersjp = playersjp[["Name","JapaneseCount"]]
    playersjp = playersjp.reset_index(drop=True)
    print("\n High Scores: \n")
    print("Player","          " ,"Score")
    if playersjp["Name"].size < 5:
        for i in range (0,playersjp["Name"].size):
         print(playersjp["Name"][i], "          ", playersjp["JapaneseCount"][i])
    else:
        for i in range (0,4):
         print(playersjp["Name"][i], "          ", playersjp["JapaneseCount"][i])


""" Add players to database edit if new languages added"""
def addPlayerFr(playerData,name,frArr, frCount):
    player = pd.DataFrame([[name,frArr,frCount,None,None]],columns=["Name","FrenchWords","FrenchCount","JapaneseWords","JapaneseCount"])
    newPlayer = pd.concat([playerData,player],ignore_index=True)
    return newPlayer
    
def addPlayerJp(playerData,name,JpArr, JpCount):
    player = pd.DataFrame([[name,None,None,JpArr,JpCount]],columns=["Name","FrenchWords","FrenchCount","JapaneseWords","JapaneseCount"])
    newPlayer = pd.concat([playerData,player],ignore_index=True)
    return newPlayer
    
    
def play():
    #displayScoresFr()
    playerName = input("What shall I call you? \n")
    if playerName in allPlayers:
        print("Welcome back %s! \n"%playerName)
        #load from players.csv
        ##Need to load data into usedCorr for words already used correctly 
    else:
        #a new player
        print("Hello %s! \n"%playerName)
        
         
        
    while 1:
        language = input("Pick a language! (French, Japanese) \n")
        if language == "French":
            loadFrench()
            selectedLangauge = "French"
            #user = Player(player, True)
            #allPlayers.append(user)
            break
        elif language == "Japanese":
            loadJapanese()
            selectedLanguage = "Japanese"
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
                f.write('\n' + playerName+ ',' + sCorr)
                f.close()
                displayScores()
                break
            continue
        elif guess == 'QUIT':
            sCorr = toString(usedCorr)
            print(sCorr + '.')
            f = open("players.txt","a")
            f.write('\n' + playerName + ',' +  sCorr)
            f.close()
            if selectedLangauge == "French":
                newPlayerData = addPlayerFr(playerData,playerName, usedCorr, len(usedCorr))
                displayScoresFr(newPlayerData)
            elif selectedLangauge == "Japanese":
                newPlayerData = addPlayerJp(playerData,playerName, usedCorr, len(usedCorr))
                displayScoresJp(newPlayerData)
            print("See you again soon! \n")
            newPlayerData.to_csv("players.csv",index=False)
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





    








