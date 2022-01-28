
# Imports 

from winreg import SetValue
from termcolor import colored
from consolemenu import *
from consolemenu.items import *
import time 
import sys
import random


# Intro Options

print("")

print(colored('Welcome', 'cyan'))

time.sleep(1)

print(colored('Choose your option', 'yellow'))

# Menu Questions & Options

d1a = input("Do you want to: \n A) Start Display. B) End Program. [A/B]? : ")

if d1a == "A":
    print(colored('Program Started, please hold', 'cyan'))

    time.sleep(2)

    print(colored('Please enter access code.', 'yellow'))

# Correct Code 

    val = input("Code: ")
    if val == "123":
        print(colored('Correct Code, Logging in', 'cyan'))
        

        time.sleep(2)

        
        print(colored('Welcome to the Display Menu. This is currently a work in progress.', 'blue'))
        time.sleep(1)
        print(colored('This is just a test, ill work on a better version later', 'yellow'))

        # Wrong Code 
        
    else:
        print(colored('Wrong Code, Closing Prompt.', 'red'))

        

    

         
 

elif d1a == "B":
    print(colored('Ending Program.', 'red'))
    


