# -*- coding: utf-8 -*-
from Selen import Selen
from Soup import Soup
import itertools
import threading
import time
import sys

selen = Selen()
soup = Soup()

name = input("Enter player name : ")
# name = 'Kreydawg'

def animated_loading() :
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.1)
        sys.stdout.flush() 

def process() :
    doc = selen.getPage(name)
    soup.analyze(doc, name)

the_process = threading.Thread(name='process', target=process)
the_process.start()
while the_process.isAlive():
    animated_loading()


    



