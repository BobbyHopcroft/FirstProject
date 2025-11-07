# def observed():
#     observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
#     return observations
#
# def run_task1():
#     print(observed())
#
# run_task1()
import fileinput


# def observed_items():
#     observations = []
#     for i in range(7):
#         observation = input("Please enter an observation")
#         observations.append(observation)
#     return observations
# def run_task2():
#     print("Counting observations...")
#     observations = observed_items()
#     count1 = set()
#     for item in observations:
#         item_count = (item, observations.count(item))
#         count1.add(item_count)
#     for item, total in count1:
#         print(f"{item} observed {total} times")
#
#
# run_task2()

def observed_items():
    observations = []
    for i in range(5):
        observation = input("Please enter an observation")
        observations.append(observation)
    return observations

def remove_observations(observations):
    print("Do you wish to remove observations?")
    if input("yes") == "yes":
        input("What observation do you want to be removed?")
        observations.remove(input)

def run_task3():
    observed_items()
    remove_observations(observed_items())
    print("Counting observations...")
    observations = observed_items()
    count1 = set()
    for item in observations:
        item_count = (item, observations.count(item))
        count1.add(item_count)
    for item, total in count1:
        print(f"{item} observed {total} times")
run_task3()









