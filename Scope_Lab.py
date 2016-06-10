a = [1, 2, 4]
b = a

# input: a list of ints
# output: an int
my_list = [1, 2, 3, 4, 5]
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    a_list[4] = 100
update_list(my_list)
print(my_list)
# The variable "b" will not affect "a" because both variables are presented as a global and local variable. Outside of the function, "b" is equal to "a". But inside the function, "b" is equal to "a_list[4]" and 100. I changed the variable "b = 100" and replaced it with "a_list[4] = 100". I forgot to mention that I put the list "my_list" before the function and called on the function with "update_list(my_list)."



var_1 = "kittens" #Global
var_2 = "cookies" #Global
# input: a string
# output: a string
def my_function(my_favorite_things): #Parameter is local
    song_lyrics = "rain drops on roses," #Local
    combined_song = song_lyrics + my_favorite_things #Local
    return combined_song #Local
# input: a string
# output: a string
def my_function_2(item, item2): #Parameter is global
    full_lyrics = item + "on " + item2 #Local
    full_song = my_function(full_lyrics) #Local
    return full_song #Local
my_song = my_function_2(var_1, var_2) #Global



var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the ") + var_1
    else:
        print("My favorite pet is the ") + var_2


print_out_my_favorite(var_1)
print(var_2)


my_num= 4
def multiply_num(multiplier):
    my_num= 
    print my_num
multiply_num(3)
