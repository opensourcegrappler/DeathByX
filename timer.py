#!/usr/bin/python

#imports
from __future__ import print_function
import time
import math
import pygame

#load beep sound, pygame allows sound to play asynchronously
pygame.mixer.init()
pygame.mixer.music.load("beep-09.mp3")

#setup counters
mins=0.0
sec_tenths=0.0
reps=0

#run forever
while True:

    #current round
    rnd=mins
    #calculate interval between reps for current round
    intvl=round(60.0/(mins+1.0),1)

    #does this even work properly?
    modulo =  round(sec_tenths-(intvl*math.floor(sec_tenths/intvl)),1)

    #play beep on interval, one decimal point only so occasional rounding error occurs
    if modulo==intvl or modulo==0.0:
        #play beep
        pygame.mixer.music.play()
        #print your current score
        print("Rounds %02d: Reps %02d | Time %02d:%04.1f\r"%(rnd,reps+1,mins,sec_tenths))
        #increment reps
        reps+=1
    else:
        #wait for time to elapse
        time.sleep(0.1)

    #increment timer    
    sec_tenths+=0.1

    #if end of round, reset the counters
    if round(sec_tenths%60.0,1)==0.0:
        sec_tenths=0.0
        mins+=1
        reps=0
