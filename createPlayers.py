#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:17:51 2020

@author: makishimizu
"""

import pandas as pd

playerArr = []

players = pd.DataFrame([["Matt",[2, 3,4, 5,6, 23, 45, 67],8, None, None],
                        ["Clementine",[123 ,781 ,563 ,612, 330, 923, 859],7 ,None, None],
                        ["Charles",[2, 3,4, 5,6, 23, 45, 67, 502, 146, 934,124,34],13, None, None]]
                       ,columns=["Name","FrenchWords","FrenchCount","JapaneseWords","JapaneseCount"])




playersfr = players.sort_values(["FrenchCount"], ascending=False)
playersfr = playersfr[["Name","FrenchCount"]]
playersfr = playersfr.reset_index(drop=True)

#print("Player","          " , "Score")
for i in range (0,playersfr["Name"].size):
 #print(playersfr["Name"][i],"          " ,playersfr["FrenchCount"][i])
 playerArr.append([playersfr["Name"][i],playersfr["FrenchCount"][i]])
 
    
"""
for i in playerArr:
    print(i[0],i[1])
print(playersfr)
"""
#print (players.head())

players.to_csv("players.csv")

player = pd.DataFrame([["Sam",None,None,[50,769,342,234,645,267,93],7]],columns=["Name","FrenchWords","FrenchCount","JapaneseWords","JapaneseCount"])
players = pd.concat([players,player],ignore_index=True)
print(players)