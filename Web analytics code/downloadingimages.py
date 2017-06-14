# -*- coding: utf-8 -*-
"""
Created on Fri May 05 19:56:11 2017

@author: Tapan Patel
"""

import pickle
import os
import urllib
counter=0
os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/WD")
   
with open('ANDuniqueimages.pickle', 'rb') as infile:
    aset=pickle.load(infile)
    print (type(aset))
    print ("Total Unique Screenshots for android are :- " + str(len(aset)))
    os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/WD/Android Images")
    for urls in aset:
        urllib.urlretrieve(urls, "AND-"+str(counter)+".jpg")
        counter+=1
        print(counter)

os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/WD")
counter=0        
with open('IOSuniqueimages.pickle', 'rb') as infile2:
    Iset=pickle.load(infile2)
    print (type(Iset))
    print ("Total Unique Screenshots for android are :- " + str(len(Iset)))
    os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/WD/IOS Images")
    for urls in Iset:
        urllib.urlretrieve(urls, "IOS-"+str(counter)+".jpg")
        counter+=1
        print(counter)