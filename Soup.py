# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
# import urllib2
import statistics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

class Soup :
    
    def analyze(self, doc, name) :

        page = doc
        soup = BeautifulSoup(page,features='lxml')
        
        
        yikesLength = soup.find_all('div', class_ ='GameLength')
        yikesResult = soup.find_all('div', class_ ='GameResult')
        
        BadLengths = [(i.contents) for i in yikesLength]
        BadResults = [(i.contents) for i in yikesResult]
        BadJoined = tuple(zip(BadLengths,BadResults))
        
        Goods=[]
        for i  in (BadJoined) :
            badTime = i[0]
            badResult = str(i[1])
            minute = int(badTime[0].split(' ')[0].replace('m',''))
            second = (float(badTime[0].split(' ')[1].replace('s','')))/60
            time = minute + second
            if 'Victory' in badResult :
                result = 1
            elif 'Defeat' in badResult :
                result = 0
            else :
                result = 2
            Goods.append((time, result))
        Data = [i for i in Goods if i[1] !=2] 
        
        #Defeat = 0
        #Victory = 1
        winTimes = [i[0] for i in Data if i[1] == 1]
        winMean = statistics.mean(winTimes)
        
        loseTimes = [i[0] for i in Data if i[1] == 0]
        loseMean = statistics.mean(loseTimes)
        
        print('\nThe average game length for '+str(name) +' in a victory is ' + str(winMean) + ' minutes')
        print('The average game length for ' +str(name) +' in a loss is ' + str(loseMean) +' minutes')
        
        x = np.array([[i[0] for i in Data]]).reshape(-1,1)
        y = np.array([[i[1] for i in Data]]).reshape(-1)
        
        model = LogisticRegression(solver='liblinear', random_state = 0, C=10.0).fit(x,y)
        intercept = model.intercept_
        coefficient = model.coef_
        score = model.score(x,y)
        print('The model intercept is ' + str(intercept))
        print('The model coefficient is ' + str(coefficient))
        print('The model accuracy is ' + str(score))
        print(classification_report(y,model.predict(x)))
        e=2.71828
        
        for z in range(3,11) :
            print('The estimated probability of player '+str(name)+' winning a ' + str(5*z) +' minute game is ' +str((1/(1+e**(intercept + (5*z)*coefficient)))))
        
        cm = confusion_matrix(y, model.predict(x))
        
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(cm)
        ax.grid(False)
        ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
        ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
        ax.set_ylim(1.5, -0.5)
        for i in range(2):
            for j in range(2):
                ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
        plt.show()

