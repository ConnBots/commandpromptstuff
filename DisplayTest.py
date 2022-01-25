
# Imports 

from termcolor import colored
from simple_term_menu import TerminalMenu
import time 
import sys
import random

# Intro Options

print(colored('Hi', 'cyan'))

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

        # Wrong Code 
        
    else:
        print(colored('Wrong Code, Closing Prompt.', 'red'))

    

         
 

elif d1a == "B":
    print(colored('Ending Program.', 'red'))
    
    



