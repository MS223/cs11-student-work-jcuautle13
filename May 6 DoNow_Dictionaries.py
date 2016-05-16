my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print my_dictionary
print my_dictionary['dog']
print my_dictionary.get('dog')
print 'cat' in my_dictionary
print 'monkey' in my_dictionary


#1: Specific words inside the list "my_dictionary" such as "dog", "cat", and "monkey" are the ones that are being printed.
#2: my_dictionary is a list.
#3: print my_dictionary['chair']
#4: When you use "my_dictionary['kittens']", there will be an error because the computer does not understand the command. If the command was written "print my_dictionary["kittens"]", there would be no error and the computer will instead print out the word "kittens" from the list, "my_dictionary".
