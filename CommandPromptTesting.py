from termcolor import colored
import time

print(colored('Hey!', 'red'), colored('This is a test', 'green'))

time.sleep(2)

print(colored('This should send after 2 seconds.', 'cyan'))

time.sleep(2)

print(colored('See, you waited 2 seconds for it to send', 'blue'))

time.sleep(1)

print(colored('This program will now end in', 'red'))

time.sleep(1)

print(colored('3', 'red'))

time.sleep(1)

print(colored('2', 'red'))

time.sleep(1)

print(colored('1', 'red'))

time.sleep(1)