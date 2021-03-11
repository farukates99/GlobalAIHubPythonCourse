oddnumbers = [1,3,5,7,9]
evennumbers = [0,2,4,6,8]
numbers = oddnumbers + evennumbers  #merge two list

numbers= [i*2 for i in numbers ]    # multiply all values of the new list by 2
for item in numbers:
    print (type(item))          # data type of the all values in the new list
