vowels = ['a','e','i','o','u']
string = raw_input("Give me a sentence.")

def de_vowel(string):
    for x in string:
        if x in vowels:
