import os
# def cwd():
#     cwd = os.getcwd()
#     print("The current working directory is:", cwd)
#     print("The directory contains the following files:")
#     print(os.listdir(cwd))
#
# def run():
#     print("Processing...")
#
# run()
# cwd()
import fileinput


def display_chars(file_path,num_chars):
    with open(file_path) as file:
        display_chars = file.read(num_chars)
        print(display_chars)






def display_lines():
    with open('libary.txt') as file:
        display_lines = file.readline()
        file.close()
        print(display_lines)
        return display_lines




def display_text(file_path):
    with open(file_path) as file:
        display_text = file.read()
        print(display_text)
        return display_text


def run_task2():
    display_chars('libary.txt', 5)
    display_lines()
    display_text('libary.txt')

run_task2()





