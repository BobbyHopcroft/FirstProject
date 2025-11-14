

import matplotlib.pyplot as plt
import os
import random


# def display_line(x,y):
#     plt.plot(x,y)
#     plt.show()
#
# def run_task1():
#     x_values = [1,2,3,4,5]
#     y_values = [1,4,9,16,25]
#     display_line(x_values,y_values)
# run_task1()


# def small():
#     x = [3,4,4,3,3]
#     y = [3,3,4,4,3]
#     plt.plot(x,y,'o--r')
#
#
# def medium():
#     x = [2,5,5,2,2]
#     y = [2,2,5,5,2]
#     plt.plot(x,y,'o--g')
#
# def large():
#     x = [1,6,6,1,1]
#     y = [1,1,6,6,1]
#     plt.plot(x,y,'o-b')
#
# small()
# medium()
# large()
# plt.show()

# def coordinate():
#     x = input("Enter an X value")
#     y = input("Enter an Y value")
#     return x,y
#
# def path():
#     print("Retrieving Path...")
#     x_values = []
#     y_values = []
#     for _ in range(4):
#         data = coordinate()
#         x_values.append(data[0])
#         y_values.append(data[1])
#     return [x_values, y_values]
#
# def run_task3():
#     values = path()
#     plt.plot(values[0], values[1],'ro--')
#
# run_task3()
# plt.show()

def data():
    path = {}
    response1 = input("What line would you like? :, -- or -")
    response2 = input("What color would you like? r,g or b")
    response3 = input("What style of marker would you like? o,s or ^")
    path = {"line": response1, "color": response2, "style": response3}
    return path
def generate():
    response4 = int(input("How many lines would you like to display?"))
    for _ in range(response4):
        values = data()
        x = random.sample(range(1, 51), 5)
        y = random.sample(range(1, 51), 5)
        plt.plot(x,y,f"{values['line']}{values['color']}{values['style']}")

    plt.show()
def run():
    print("Running...")
    generate()
    print("Done!")
run()



