from termcolor import colored
from consolemenu import *
from consolemenu.items import *
import random
import sys

menu = ConsoleMenu("Welcome to the terminal menu", "Version 1.0")

menu_item = MenuItem("Start Program")

function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
     

command_item = CommandItem("Run a console command",  "break")

selection_menu = SelectionMenu(["TBA", "TBA", "TBA"])


submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

menu.show()