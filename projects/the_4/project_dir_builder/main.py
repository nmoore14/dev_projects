# System and OS imports
import sys
import os
import platform
import json

# Helper imports
from helpers import args_list, dir_builder

# Class imports

# Global variables
user_system = platform.system()
dir_structure = ''
dir_path = ''
project_name = ''
debugging = False

interactive = False

# Set up the argument parser
parser = args_list.parser
args = parser.parse_args()

# To see all available args without typing --help or -h
print("\n")
print(args)
print("\n")

for attr, value in args.__dict__.items():
    if value and value is not None:
        if attr == 'interactive' and value:
            print("Using interactive")
            interactive = True
            break
        else:
            if attr != 'path' and attr != 'current' and attr != 'project_name':
                dir_structure = value
            elif attr == 'debug' and value:
                print("Debugging set")
                debugging = True
            elif attr == 'project_name':
                project_name = value
            elif attr == 'path':
                dir_path = value
                print("\n" + attr + " => " + value + "\n")
            else:
                dir_path = os.getcwd()

if interactive == False:
    if debugging:
        try:
            print("Debugging...")
            structure = open("assets/directories_json/" + dir_structure + ".json")
            data = json.load(structure)
            dir_structure = data['structure']
            new_project = dir_builder.Dir_Builder(dir_path, project_name, dir_structure, user_system)
            new_project.view_info()
            structure.close()
        except:
            print("Can't debug info passed...look somewhere else.")
    else:
        try:
            structure = open("assets/directories_json/" + dir_structure + ".json")
            data = json.load(structure)
            dir_structure = data['structure']
            new_project = dir_builder.Dir_Builder(dir_path, project_name, dir_structure, user_system)
            new_project.build_project()
            structure.close
        except:
            print("No structure named: " + dir_structure)
else:
    print("Coming soon...")

