import os

#user_Input = input("Enter the file you would like to run: ")

def openFile():
    try:
        os.startfile("E:\Steam\steam.exe")
        print("Opening application... \n|Please Wait|")

    except:
        print("Unhandled Exception")

openFile()
print("Operation Complete")