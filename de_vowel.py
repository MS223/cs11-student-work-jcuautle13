vowels = ['a','e','i','o','u']
sentence = raw_input("Give me a sentence!").lower() #This will prevent any problems with capitalized sentences.
for x in sentece:
    if x in vowels:
        sentence = sentence.replace(x,'') # This replaces the "x"'s with " '' "
print sentence # Prints out the sentence without
