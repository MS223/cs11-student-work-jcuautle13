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

def add(action,day):
    days_of_the_week[day].append(action)

def get(day):
    print days_of_the_week[day]

def choice():
    user_choice = raw_input("How can I help you?") #Working on this function
