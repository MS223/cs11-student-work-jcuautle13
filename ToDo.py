action = raw_input("What would you like to do?")
day = raw_input("What day?").capitalize()
days_of_the_week = {
    "Monday":[],
    "Tuesday":[],
    "Wednesday":[],
    "Thurday":[],
    "Friday":[],
    "Saturday":[],
    "Sunday":[],
}

# Currently working on a loop function

days_of_the_week[day] = action
print days_of_the_week
