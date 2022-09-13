def countdown(num):
    list=[]
    for x in range (num, -1, -1):
        list.append(x)
    return list
result= countdown(5)
print (result)



def printandreturn (list):
    if len(list)==2:
        print (list[0])
        return list[1]
    else:
        print "enter a list with 2 elemnts"
result= printandreturn([9,5])
print (result)



def firstPlusLength(list):
    return list[0]+ len(list)
result= firstPlusLength([0,1,2,3,4])
print (result)



def ValuesGreaterthanSecond (list):
    if len(list)<2:
        return False
    else:
        newList=[]
        for num in range (len(list)):
            if list[num]>list[1]:
                newList.append(list[num])
        print (len(newList))
    return newList
result= ValuesGreaterthanSecond([9,5,1,2,7,8])
print (result)



def ThisLengthThatValue (length, value):
    newList=[]
    for x in range(0, length, 1):
        newList.append(value)
    return newList
result= ThisLengthThatValue (5, 2)
print (result)

#tried another solution:
# def ThisLengthThatValue (length, value):
#     list=[]
#     (list.append(value))*length
#     return list
# result= ThisLengthThatValue (3,2)
# print (result)
