# -*- coding: utf-8 -*-
"""
Created on Fri May  5 01:25:08 2017
@author: Tapan Patel
"""
import glob
from bs4 import BeautifulSoup
import os
import gc
import pickle

gc.enable()
data_dict=dict()
final_dict=dict()

os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/WD/data")
errfls=0
iosurllist=[]
andurllist=[]
for folders in glob.iglob('*'):
    print (folders)
    #os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/pokemon_5378 (2)/data/" + folders)
    os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/WD/data/" + folders)
    for filename in glob.iglob('*.html'):        
        
        with open(filename,encoding="utf8") as f:
            
            if 'android' in filename:
                 try:
                    soupA = BeautifulSoup(f , 'lxml' )
                    # getting url
                    a1 = soupA.find_all("img",{"class":"screenshot"})
                    urla1= a1[0]['src']
                    urla2= a1[1]['src']
                    urla3= a1[2]['src']
                    urla4= a1[3]['src']
                    urla5= a1[4]['src']
                    andurllist.append(urla1)
                    andurllist.append(urla2)
                    andurllist.append(urla3)
                    andurllist.append(urla4)
                    andurllist.append(urla5)
                 except:
                    errfls+=1 
                    print (filename)
                    continue
            elif 'ios' in filename:
                try:
                    soupI = BeautifulSoup(f , 'lxml' )
                    I1 = soupI.find_all("img",{"itemprop":"screenshot"})
                    urlI1= I1[0]['src']
                    urlI2= I1[1]['src']
                    urlI3= I1[2]['src']
                    urlI4= I1[3]['src']
                    urlI5= I1[4]['src']
                    iosurllist.append(urlI1)
                    iosurllist.append(urlI2)
                    iosurllist.append(urlI3)
                    iosurllist.append(urlI4)
                    iosurllist.append(urlI5)
                    print(".",sep=' ', end='')
                except:
                    errfls+=1 
                    print (filename)
                    continue
                
    
    
print (errfls)

os.chdir("C:/Users/Tapan Patel/Desktop/Sem2 Spring 2017/1) Data Science INSY-5378-001/PROJECTS/Project 2/WD")
with open('Androidurllist.pickle', 'wb') as outfile:
    pickle.dump(andurllist,outfile)
with open('Iosurllist.pickle', 'wb') as outfile2:
    pickle.dump(iosurllist,outfile2)
print("Done________________________________________________________________________")