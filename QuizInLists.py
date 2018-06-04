def proc(mylist):
    mylist = mylist + [6, 7]
    return mylist


list1 = [1,2,3,4,5]
print list1

proc(list1)
print list1

list1 += [6,7]
print list1
