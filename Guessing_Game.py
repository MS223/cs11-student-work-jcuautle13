username = raw_input("What's your name?").capitalize()
upper_bound = input("What's the biggest number you want to guess?")
guess = input("What's your guess?")
counter = 1
import random
random_number = random.randint(1,upper_bound)
while guess != random_number:
    if guess > random_number:
        print "Sorry, " + str(username) + ", your guess is too high!"
        counter = counter + 1
    else:
        print "Sorry, " + str(username) + ", your guess is too low!"
        counter = counter + 1
    guess = input("Guess again?")
    if guess == random_number:
        print "You're right!"

print str(random_number) + " is the answer!!!!!"
print "It took you " + str(counter) + " attempts to get the right answer."
