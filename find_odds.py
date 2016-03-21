Write a for loop to print only the odd numbers from this list
list = [3,4,7,13,54,32,653,256,1,41,65,83,92,31]

def find_odds(input):
    for x in input:
        if x % 2 == 1:
            print input

# To exceed standards, create functions to ADD all of the odd numbers in a list. Then create a function to add all of the even numbers in a list. Test your functions using a randomly generated list of numbers.
def odd_sum(input):
def even_sum(input):

# Test your code
import random
my_randoms = random.sample(range(100), 15)
