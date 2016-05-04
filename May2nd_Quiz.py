def maxvalue(x):
    for i in range(1,8):
        print i
maxvalue(8)

list1 = [1,18,42,33,44]
list2 = [8,11,69,12,93]
def compare_lists(list1,list2):
    for x in list1:
        if x > list2[list1.index(x)]:
            print x
        else:
            print list2[list1.index(x)]
compare_lists(list1,list2)

def swapping_stars():
    height = 6
    width = 3
    for x in range (0, height):
        if x % 2 == 1:
            print "- * " * width
        else:
            print '* - ' * width
swapping_stars()
