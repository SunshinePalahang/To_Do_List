from datetime import datetime
from bst_demo import BSTDemo, Node

def get_job_input_details():
    start_time = input("Enter the time in hh:mm format, example 18:30 or 6:30-> ")
    while True:
        try:
            datetime.strptime(start_time, '%H:%M')
        except ValueError:
            print("Incorrect time format, should be hh:mm")
            start_time = input("Enter the time in hh:mm format, ex 18:30 or 6:30-> ")
        else:
            break
    duration_of_job = input("Enter the duration of the task in minutes, ex 60-> ")
    while True:
        try:
            int(duration_of_job)
        except ValueError:
            print("Please enter a number for number of minutes")
            duration_of_job = input("Enter the duration of the task in minutes, ex 60-> ")
        else:
            break
    job_name = input("Enter the name of the task (case sensitive)-> ")
    return start_time, duration_of_job, job_name

def search_job():
    start_time = input("Enter the time in hh:mm format, example 18:30 or 6:30-> ")
    while True:
        try:
            datetime.strptime(start_time, '%H:%M')
        except ValueError:
            print("Incorrect time format, should be hh:mm")
            start_time = input("Enter the time in hh:mm format, ex 18:30 or 6:30-> ")
        else:
            break
    return start_time
   
my_tree = BSTDemo()

with open("Modified-Job-Scheduler/data.txt") as f:
    for line in f:
        my_tree.insert(line)

while True:
    print("Please choose an option from the list below:")
    print("Press 1 to view today's scheduled tasks")
    print("Press 2 to add a task to today's schedule")
    print("Press 3 to remove a task from the schedule")
    print("Press 4 to search a task from the schedule")
    print("Press 5 to set status of a task")
    print("Press 6 to quit")
    selection = input("Enter your choice-> ")
    try:
        entry = int(selection)
    except ValueError:
        print("Please enter a number between 1 to 6")
        continue
    if int(selection) == 1:
        my_tree.in_order()
    elif int(selection) == 2:
        print("You have chosen to add a task to the schedule")
        start_time, duration_of_job, job_name = get_job_input_details()
        line = start_time+","+duration_of_job+","+job_name
        num = my_tree.length()
        my_tree.insert(line)
        if num == my_tree.length()-1:
            with open("Modified-Job-Scheduler/data.txt", "a+") as to_write:
                to_write.write(line+"\n")
        input("Press any key to continue... ")
    elif int(selection) == 3:
        print("You have chosen to remove a task from the schedule")
        start_time, duration_of_job, job_name = get_job_input_details()
        key_to_find = datetime.strptime(start_time, '%H:%M').time()
        result = my_tree.find_val(key_to_find)
        if result:
            if result.name_of_job == job_name and result.duration == duration_of_job:
                print("Removing task:")
                print(result)
                my_tree.delete_val(key_to_find)
                print("Task successfully removed")
                with open("Modified-Job-Scheduler/data.txt", "r") as f:
                    lines = f.readlines()
                with open("Modified-Job-Scheduler/data.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != start_time+","+duration_of_job+","+job_name:
                            f.write(line)
                input("Press any key to continue... ")
            else:
                print("The name and/or duration of task did not match, delete failed")
                input("Press any key to continue... ")
        else:
            print("Task not found")
            input("Press any key to continue... ")
    #add search feature
    elif int(selection) == 4:
        print("You have chosen to search a task from the schedule")
        start_time= search_job()
        key_to_find = datetime.strptime(start_time, '%H:%M').time()
        result = my_tree.find_val(key_to_find)
        if result:
            print("Searching task:")
            print(result)
            with open("Modified-Job-Scheduler/data.txt", "r") as f:
                lines = f.readlines()
            input("Press any key to continue... ")
        else:
            print("Task not found")
            input("Press any key to continue... ")     
    #add set status feature       
    elif int(selection) == 5:
        print("You have chosen to set a status a task from the schedule")
        start_time, duration_of_job, job_name = get_job_input_details()
        key_to_find = datetime.strptime(start_time, '%H:%M').time()
        result = my_tree.find_val(key_to_find)
        if result:
            if result.name_of_job == job_name and result.duration == duration_of_job:
                print("Searching task:")
                print(result)
                status = input("Accomplished? (y/n): ")
                print(result, "DONE")
                my_tree.delete_val(key_to_find)
                print("Task successfully accomplished!")
                with open("Modified-Job-Scheduler/data.txt", "r") as f:
                    lines = f.readlines()
                with open("Modified-Job-Scheduler/data.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != start_time+","+duration_of_job+","+job_name:
                            f.write(line)
                input("Press any key to continue... ")
            else:
                print("The name and/or duration of task did not match, delete failed")
                input("Press any key to continue... ")
        else:
            print("Task not found")
            input("Press any key to continue... ")            
    elif int(selection) == 6:
        print("Exiting program...")
        break
    else:
        print("Please enter a number between 1 to 6")