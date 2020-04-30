#!/usr/bin/env python
# coding: utf-8

# In[56]:


import random as r
import string
import array as arr
global guessesRem

""" Load words into an array called 'words' """
txt = open("hangmanWords.txt", "r")
words = []
for i in txt:
    words.append(i.rstrip('\n'))
#print(words)


#alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']



"""
def correct(guess):
    
    print("")
    
def incorrect(guess):
    print("")

def checkLetter(guess):
    

    
def checkInput(guess):
    if !string.isalpha(guess):
        print("This is not a letter")
    if len(guess) > 1:
        print("You can only enter one letter")
    else:
        guess = string.lower(guess)
        
 """

def printMan(guessesRem):
    print (image[8 - guessesRem])

def printWord(guessed, word):
    for i in range(0,len(word)-1):
        if word[i] in guessed:
            print(" %c "%word[i] , end =" ")
        else:
            print(" _ " , end =" " )  
    print("\n")
        
    
z = """
        _|_____
         |     |
         |     O
         |    \|/
         |     |
         |    / \\
     ____|_____
        
    """

y = """
        _|_____
         |     |
         |     O
         |    \|/
         |     |
         |    /
     ____|_____
        
    """
x = """
        _|_____
         |     |
         |     O
         |    \|/
         |     |
         |    
     ____|_____
        
    """
w = """
        _|_____
         |     |
         |     O
         |    \|/
         |     
         |    
     ____|_____
        
    """
v = """
        _|_____
         |     |
         |     O
         |     |/
         |     
         |    
     ____|_____
        
    """
u = """
        _|_____
         |     |
         |     O
         |     |
         |     
         |    
     ____|_____
        
    """
t = """
        _|_____
         |     |
         |     O
         |    
         |     
         |    
     ____|_____
        
    """
s = """
        _|_____
         |     |
         |     
         |    
         |     
         |    
     ____|_____
        
    """
image = [s,t,u,v,w,x,y,z]

def playGame(word):
    """Picks a random word, 'word', from 'words' """
    numWords = len(words)
    pick = r.randint(0,numWords-1)
    word = words[pick]
    wordLength = len(word)
    #print(word)
    unique = len(list(set(word)))
    guessesRem = 8
    allGuesses = [""]
    correctGuesses = [""]
    unknown = unique
    temp = unknown
    print ("Your word has %d letters \n "%unknown)
    while temp > 0 :
        print("_ ", end='')
        temp -= 1
    print("\n")

    while 1:
        guess = input("Make your guess \n")
        #Check only one letter is given
        if guess.lower() is word:
            print("Congratulations! You guessed correctly, the word was %s"%word)
            break
        if not guess.isalpha():
            print("This is not a letter \n")
            continue
        elif len(guess) > 1:
            print("You can only enter one letter \n")
            continue
        elif guess.lower() in allGuesses:
            print("You have already guessed this letter \n")
            continue
        else:
            guess = guess.lower()
            allGuesses.append(guess)
            if guess in word:
                print("Correct! \n")
                correctGuesses.append(guess)
                printMan(guessesRem)
                printWord(correctGuesses, word)
                unknown -=1
                if len(correctGuesses) == unique:
                    print("Congratulations! You have won the game!")
                    printWord(correctGuesses, word)
                    break
                else:
                    continue
                
            else:
                print("Too bad! Make another guess! \n")
                guessesRem -= 1 
                if guessesRem == 1:
                    printMan(guessesRem)
                    print("Sorry, you lost! The word was %s \n Better luck next time!"%word)
                    break
                else:
                    printMan(guessesRem)
                    printWord(correctGuesses, word)
                    continue
            
        



# Begin 

while 1:
    play = input("Whould you like to start a game? y/n \n")
    if play == 'y':
        print('\n Okay! Let\'s begin! \n')
        playGame(word)
        continue
    elif play == 'n':
        print("\n Okay, maybe later! \n")
        continue
    elif play == 'exit':
        print("\n Bye bye! \n")
        break
    else:
        print("\n Sorry, I didnt catch that \n")
        continue


#print ("you entered", play)





# In[ ]:





# In[ ]:




