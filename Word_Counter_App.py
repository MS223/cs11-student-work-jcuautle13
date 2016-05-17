text_input = raw_input("Paste your text here").lower().split(" ")
words = raw_input("What are the words that you are looking for?")
words = words.replace(","," ")
dictionary = {}
dictionary["word count"] = text_input.count(words)
for x in text_input:
    dictionary[x] = dictionary.pop(x,0) + 1
print dictionary
