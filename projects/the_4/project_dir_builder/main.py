# System and OS imports
import sys
import os
import platform

# Helper imports
from helpers import args_list

# Class imports

# Global variables
user_system = platform.system()

# Set up the argument parser
parser = args_list.parser
args = parser.parse_args()


print(user_system)
