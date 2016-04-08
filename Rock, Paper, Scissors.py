import random
list = ['rock', 'paper', 'scissors']
choice = random.choice(list)
print "rock, paper, scissors.. SHOOT!"
user = raw_input("user: ")
print "Computer: " + choice
while user == choice:
    print "Tie"
    print "rock, paper, scissors.. SHOOT!"
    user = raw_input("User: ")
    choice = random.choice(list)
    print "Computer: " + choice
if user == "rock" and choice == "scissors" or user == "paper" and choice == "rock" or user == "scissors" and choice == "paper":
    print "Nice"
    print "rock, paper, scissors.. SHOOT!"
    user = raw_input("User: ")
    choice = random.choice(list)
    print "Computer: " + choice
else:
    print "You suck and you don't deserve to walk among the Earth."

# Why doesn't the else want to print? What am I doing wrong? 
