'''1. Calorie Counter: Write a program that asks the user for their age, weight, and activity level, then calculates their daily calorie goal based on recommended guidelines. Use if-else statements to adjust the goal based on the user's activity level.'''

age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))
activity_level = input("Enter your activity level (low, medium, high): ")
calorie_goal = 0

if age <= 30:
    calorie_goal = weight * 35
elif age <= 60:
    calorie_goal = weight * 30
else:
    calorie_goal = weight * 25
    
if activity_level == "low":
    calorie_goal *= 1.2
elif activity_level == "moderate":
    calorie_goal *= 1.55
elif activity_level == "high":
    calorie_goal *= 1.9

print("Your daily calorie goal is:",calorie_goal)

'''2. Sleep Tracker: Create a program that asks the user for their bedtime and wake-up time, then calculates their total sleep 
duration. Use if statements to determine if they met the recommended sleep amount and provide feedback accordingly.'''

bedtime = input("What time do you usually go to bed? (in HH:MM format): ")
wake_up_time = input("What time do you usually wake up? (in HH:MM format): ")

bedtime_hours, bedtime_minutes = map(int, bedtime.split(":"))
wake_up_hours, wake_up_minutes = map(int, wake_up_time.split(":"))

sleep_duration_hours = wake_up_hours - bedtime_hours
sleep_duration_minutes = wake_up_minutes - bedtime_minutes

if sleep_duration_hours >= 7:
    print("That's great! You're getting enough sleep.")
else:
    print("Try to get at least 7 hours of sleep for optimal health.")

print("Your total sleep duration is {} hours and {} minutes.".format(sleep_duration_hours, sleep_duration_minutes))

'''3. Hydration Helper: Design a program that prompts the user for their weight and desired level of hydration (e.g., light, moderate, intense exercise). Use nested if-else statements to suggest the amount of water they should drink throughout the day.'''

weight = float(input("What is your weight in kilograms? "))
exercise_level = input("What is your desired level of hydration (light, moderate, intense)? ")

if exercise_level == "light":
    water_intake = weight * 0.03
elif exercise_level == "moderate":
    water_intake = weight * 0.04
elif exercise_level == "intense":
    water_intake = weight * 0.05
else:
    print("Invalid exercise level. Please choose from light, moderate, or intense.")
    exit()

print("To stay hydrated, you should drink approximately {:.2f} liters of water throughout the day.".format(water_intake))

