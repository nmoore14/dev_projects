# System and OS imports
import sys
import os
import platform
import json

# Helper imports
from helpers import args_list

# Class imports

# Global variables
user_system = platform.system()
dir_structure = ''
dir_path = ''
interactive = False

# Set up the argument parser
parser = args_list.parser
args = parser.parse_args()

# To see all available args without typing --help or -h
# print("\n")
# print(args)
# print("\n")

for attr, value in args.__dict__.items():
    if value and value is not None:
        if attr == 'interactive' and value:
            print("Using interactive")
            interactive = True
            break
        else:
            if attr != 'path' and attr != 'current':
                dir_structure = value
            elif attr == 'path':
                dir_path = value
                print("\n" + attr + " => " + value + "\n")
            else:
                dir_path = os.getcwd()

if interactive == False:
    try:
        structure = open("assets/directories_json/" + dir_structure + ".json")
        data = json.load(structure)
        print(data)
        structure.close
    except:
        print("No structure named: " + dir_structure)
