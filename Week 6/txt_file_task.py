import os
def cwd():
    cwd = os.getcwd()
    print("The current working directory is:", cwd)
    print("The directory contains the following files:")
    print(os.listdir(cwd))

def run():
    print("Processing...")

run()
cwd()





