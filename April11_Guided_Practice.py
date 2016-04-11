def print_only(x):
   y = x * 2
   print y
# When I ran this code, it didn't print anything. 

def return_only(x):
   y = x * 2
   return y
# The only difference between this function and the first one is that this one says "return y" rather than "print y". Also, when defining the function, the first one says "print only" and the other says "return only". They both don't print out anything on PyCharm.

print "running print_only ..."
print_only(7)
# I added this with the function whose definition was "print_only" because this new piece has the same name for its definition. 

print "running return_only ..."
return_only(7)
# 
