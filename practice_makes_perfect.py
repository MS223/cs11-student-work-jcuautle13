def is_even(x):
    if (x % 2 == 0):
        print True
    else:
        print False
is_even(2) # I got True
is_even(3) # I got False


def is_int(x):
    if x == int(x):
        print True
    else:
        print False
is_int(7.5) # I got False
is_int(2) # I got True
