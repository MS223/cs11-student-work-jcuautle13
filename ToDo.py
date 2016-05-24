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


def add():
    action = ""
    while action != "nothing":
        action = raw_input("What are you doing?")
        if action == "nothing":
         return None
        day = raw_input("What day?").capitalize()
        days_of_the_week[day].append(action)
        print days_of_the_week
add()

def get(day):
    print days_of_the_week[day]

def choice():
    user_choice = raw_input("How can I help you?")
    if user_choice == "get":
        day = raw_input("What day?").capitalize()
        get(day)
    if user_choice == "add":
        add()
choice()
