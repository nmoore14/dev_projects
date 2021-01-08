import os


running = True

print("(1)Add applications:", "\n(2)Launch applications:", "\n(3) Exit")
user_input = input("Select one of the following: ")
apps = []# populate this list with exe files


while running:
    user_input

    if user_input == 1:
        print("Select the apps you would like to add to your list")
        #find a way to open file explorer
    elif user_input == 2:
        print("Launching Selected Applications")    
    else:
        print("End Program")
        running = False
