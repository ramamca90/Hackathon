# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:15:52 2017

@author: user
"""
import pandas as pd

loadboard = pd.read_excel("C:\\Users\\user\\Desktop\\loadBoard.xlsx")

print ("HI ..Please provide your load details ")
pickup_selected=input("Please give the pick up location")
pickup_destination=input("Please give the destination location")

print (loadboard[(loadboard.PICKUP == pickup_selected.upper() )
       & (loadboard.DELIVERY == pickup_destination.upper() )] )








