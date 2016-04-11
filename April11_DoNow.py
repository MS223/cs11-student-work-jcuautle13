import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    print z
mystery_function(1, 2)

# When I run this code, it doesn't print anything. All it says is that the "process finished with the exit code 0". I can't know what the result was because it litearlly didn't print out anything. obviously there's something wrong somewhere. around its code.
# I switched the key word "return" with "print" on line 9. 
