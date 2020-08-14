#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:17:51 2020

@author: makishimizu
"""

import pandas as pd



players = pd.DataFrame([["Matt",[2, 3,4, 5,6, 23, 45, 67],8, None, None]],columns=["Name","FrenchWords","FrenchCount","JapaneseWords","JapaneseCount"])

print (players)



players.to_csv("players.csv")