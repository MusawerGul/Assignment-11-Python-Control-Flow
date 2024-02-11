'''1. To-Do List: Develop a program that allows the user to add tasks to a to-do list. Use if statements to categorize tasks as urgent, important, or less important based on their due date and priority.

todo_list = []

def add_task(task, due_date, priority):
    todo_list.append((task, due_date, priority))

task = input("Enter the task: ")
due_date = input("Enter the due date: ")
priority = input("Enter the priority (urgent, important, less important): ")

add_task(task, due_date, priority)

print("To-Do List:")
for task in todo_list:
    print("- Task:", task[0])
    print("  Due Date:", task[1])
    print("  Priority:", task[2])'''

'''2. Pomodoro Timer: Create a program that implements the Pomodoro Technique (25 minutes work, 5 minutes break). Use a loop and if statements to track time intervals and notify the user when to switch between work and breaks.

import time

def pomodoro_timer():
    work_duration = 25 * 60  
    break_duration = 5 * 60 
    cycles = 4

    for cycle in range(cycles):
        print("Cycle", cycle + 1, " - Work")
        time.sleep(work_duration)
        print("Time's up! Take a break.")
        time.sleep(break_duration)
    
    print("Congratulations! You've completed", cycles, "cycles.")

pomodoro_timer()'''

'''3. Meeting Scheduler: Design a program that helps users find a common meeting time among a group. Use if-else statements to check for available time slots in each user's calendar and suggest suitable meeting times.'''

def find_common_time(users):
    common_time_slots = []
    for user in users:
        available_time_slots = user["available_time_slots"]
        if not common_time_slots:
            common_time_slots = available_time_slots
        else:
            common_time_slots = [slot for slot in common_time_slots if slot in available_time_slots]
    if common_time_slots:
        print("Common meeting time slots:")
        for slot in common_time_slots:
            print(slot)
    else:
        print("No common meeting time slots found.")

# Example usage
users = [
    {
        "name": "Musawer",
        "available_time_slots": ["9:00 AM - 10:00 AM", "2:00 PM - 3:00 PM"]
    },
    {
        "name": "Musaib",
        "available_time_slots": ["9:30 AM - 10:30 AM", "3:00 PM - 4:00 PM"]
    },
    {
        "name": "Suhaib",
        "available_time_slots": ["10:00 AM - 11:00 AM", "4:00 PM - 5:00 PM"]
    }
]

find_common_time(users)
