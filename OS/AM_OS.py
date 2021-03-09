from tkinter import messagebox as mb
import time
from time import sleep
import sys
from tkinter import *
import os
import pyfiglet
import random
from pyfiglet import Figlet
from tqdm import tqdm, trange
import progressbar

print('WELCOME TO AM OS 0.0')

time.sleep(1.5)

AM_OS = pyfiglet.figlet_format("AM OS")
print(AM_OS)

time.sleep(1.5)
        
for i in range(1):
    x=input("Your Family Name: ")
    
for i in range(1):
    y=input("Your Name: ")

def verify(): 
      
    widgets = ['Checking: ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start() 
      
    for i in range(25): 
        time.sleep(0.1) 
        bar.update(i) 
          
verify()

print('')
print('')

print('Is Your Name ' + x + ' ' + y + '?')

answer = input()

def log(): 
      
    widgets = ['Logging in as ' + x + ' ' + y + ': ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start() 
      
    for i in range(50): 
        time.sleep(0.1) 
        bar.update(i) 

if answer == 'Yes' or 'yes' or 'Ye' or 'ye' or 'y' or 'Y' or 'YES':
   print('')
   log()
   print('')
   print('')
   print('Login Complete.')
   print('')
   
elif answer == 'No' or 'no' or 'n' or 'N' or 'NO':
    print('')
    print('Please, Restart The Program')
    print('')
    os._exit(0)

user = x + (' ') + y
   
print('Importing data...')
print('')

for i in trange(100): 
   time.sleep(0.1)
   
print('')
print('Done!')
print('')

print('Checking System...')
print('')

for i in tqdm([1,2,3,4,5]): 
   time.sleep(0.3)
   
print('')
print('Done!')
print('')

print('Checking Apps...')
print('')

for i in trange(500): 
   time.sleep(0.01)
   
print('')
print('Done!')
print('')

print('Checking Profile Data...')
print('')

for i in trange(250): 
   time.sleep(0.1)
   
print('')
print('Done!')
print('')

print('Checking For Updates...')
print('')

for i in tqdm([1,2,3,4,5,6,7,8,9,10]): 
   time.sleep(1.5)
   
print('')
print('Done!')
print('')

time.sleep(1)

enjoy = Figlet(font='univers')
your = Figlet(font='univers')
stay = Figlet(font='univers')
print(enjoy.renderText('ENJOY'))
time.sleep(0.5)
print(your.renderText('YOUR'))
time.sleep(0.5)
print(stay.renderText('STAY!'))
time.sleep(1.5)

import Startup

print('This OS Is Still In Development')
