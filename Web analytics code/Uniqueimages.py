# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:41:07 2017

@author: Tapan Patel
"""
import os
import pickle

os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/WD")
   
with open('Androidurllist.pickle', 'rb') as infile:
    aset=set(pickle.load(infile))
    print (type(aset))
    print ("Total Unique Screenshots for android are :- " + str(len(aset)))
with open('ANDuniqueimages.pickle', 'wb') as outfile:
    pickle.dump(aset,outfile,protocol=2)

with open('Iosurllist.pickle', 'rb') as infile:
    aset=set(pickle.load(infile))
    print (type(aset))
    print ("Total Unique Screenshots for IOS are :- " + str(len(aset)))
with open('IOSuniqueimages.pickle', 'wb') as outfile:
    pickle.dump(aset,outfile,protocol=2)