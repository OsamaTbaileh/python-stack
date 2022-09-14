# 1-Biggie Size
def BiggieSize (list):
    for i in range(len(list)):
        if list[i]>0:
            list[i]="big"
    return list
result= BiggieSize ([-1, 3, 5, -5])
print (result)                                         #make all positive nums in the list ="big"



# 2-Count Positives
def CountPositives (list):
    counter=0
    for x in range (len(list)):
        if list[x]>0:
            counter+=1
    list[len(list)-1]=counter
    return list
result= CountPositives ([1,6,-4,-2,-7,-2])
print (result) 



# 3-SumTotal
def SumTotal (list):
    sum=0
    for i in range (len(list)):
        sum = sum + list[i]
    return sum
result= SumTotal ([6,3,-2])
print (result) 



#4-Average
def Aferage (list):
    sum = 0
    for x in range (len(list)):
        sum = sum + list[x]
    Average = sum/len(list)
    return Average
result= Aferage ([1,2,3,4])
print (result) 



#5-Length
def Length(list):
    return len(list)
result= Length ([37,2,1,-9])
print (result) 



#6-Minimum
def Minimun (list):
    if len(list)==0:
        return False
    else:
        Minimum = list[0]
        for i in range (1,len(list)-1):
            if list[i]<Minimum:
                Minimum=list[i]
        return Minimum
result= Minimun ([37,2,1,-9])
print (result) 



#7-Maximum
def Maximum (list):
    if len(list)==0:
        return False
    else:
        Maximum = list[0]
        for i in range (1,len(list)-1):
            if list[i]>Maximum:
                Maximum=list[i]
        return Maximum
result= Maximum ([37,2,1,-9])
print (result) 



##8-Ultimate Analysis
def UltimateAnalysis (list):
    dictionary = {"sumtotal":0, "average":0, "minimum":list[0], "maximum":list[0],"length":len(list)}
    for x in range(len(list)):
        if list[x]> dictionary["maximum"]:
            dictionary["maximum"]=list[x]
        elif list[x]< dictionary["minimum"]:
            dictionary["minimum"]=list[x]

        dictionary["sumtotal"]+=list[x]
        dictionary["average"]= dictionary["sumtotal"]/len(list)
    return dictionary
result= UltimateAnalysis ([37,2,1,-9])
print (result) 




#9-ReverseList (method 1)
def ReverseList (list):
    list.reverse()
    return list
result= ReverseList ([37,2,1,-9])
print (result) 

# 9-ReverseList (method 2)
def ReverseList (list):
    for i in range (int(len(list)/2)):
        New =list[i]
        list[i]=list[len(list)-1]
        list[len(list)-1] = New
    return list
result= ReverseList ([37,2,1,-9])
print (result) 


