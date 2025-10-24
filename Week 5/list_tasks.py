#def directions():
    #steps = ["Move forward", "Move Backward", "Move Left", "Move Right"]
    # steps.append("Move forward")
    # steps.append("Move Backward")
    # steps.append("Move Left")
    # steps.append("Move Right")
    #return steps

#def run_task():
    #steps = directions()
    #print(steps)

#if __name__ == "__main__":
    #un_task()

#def movements():
    #path = ["Move forward",10,"Move backward",5,"Move left",3,"Move right",1]
    #return path

#def run_task2():
    #print("Moving...")
    #path = movements()
    #for index in range(0, len(path),2):
        #dir = path[index]
        #steps = path[index+1]
        #print(f"{dir} for {steps} steps")

#if __name__ == "__main__":
    #run_task2()

def directions():
    steps = ["Move Forward", "Move Backward", "Move left", "Move right"]
    return steps
def menu():
    print("Please select a direction:")
    steps = directions()
    for index in range(len(steps)):
        print(f"{index}: {directions}")

def run_task3():
    menu()

    if __name__ == "__main__":
       run_task3()







