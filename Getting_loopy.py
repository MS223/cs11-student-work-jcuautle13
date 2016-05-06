def fruit_pluralizer(fruit):
    for n in fruit:
        if n[:len(n)-1]== 'y':
            print n[:len(n)-1] + 'ies'
        else:
            print n[:len(n)-1] + 's'


fruit = raw_input("Give me a fruit.")
