"""
Build the arguments list
"""

import argparse

parser = argparse.ArgumentParser()

# Debugging shell argument
parser.add_argument('-bug', '--debug', help="Pring out the view_info dir_builder function", action="store_true")

# Set the interactive shell argument
parser.add_argument('-i', '--interactive', help="Use the interactive shell to build the directory", action="store_true")

# Set directory arguments
parser.add_argument('-pn', '--project_name', help='Name of project - this will be used for parent dir name')
parser.add_argument('-c', '--current', help="Build the project in the current directory", action="store_true")
parser.add_argument('-p', '--path', help="List the path to the directory that you want the project in.", default="")


# Set the project arguments
# These will be the default set by us. Users can add more which they can access from the interactive shell or edit this file.
parser.add_argument('-wb', '--web', help="Basic HTML, CSS, and JS project structure", action="store_const", const="web")
parser.add_argument('-nj', '--node', help="NodeJS project structure", action="store_const", const="node")
parser.add_argument('-wt', '--wp_theme', help="Directory structure for building a WordPress Theme", action="store_const", const="wp_theme")
parser.add_argument('-py', '--python', help="Base Python project structure", action="store_const", const="python")
parser.add_argument('-op', '--oopython', help="Object Oriented python project structure", action="store_const", const="oopython")
