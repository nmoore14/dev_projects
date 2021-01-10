import os

user_Input = input("Enter the Directory of the apllication you would like to run: ")

def openFile():
    try:
        os.startfile(user_Input)
        print("Opening application... \n|Please Wait|")

    except:
        print("Unhandled Exception")

openFile()
print("Operation Complete")