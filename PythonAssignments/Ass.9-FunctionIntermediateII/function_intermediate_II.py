# 1- Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# solution:
x [1][0]= 5
print(x)

students [1]['last_name']='Bryant'
print (students)

sports_directory ["soccer"][0]="Andres"
print (sports_directory)

z [0]["y"]=30
print (z)



# 2- Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# solution:
def iterateDictionary(some_list):
    for x in range (len(some_list)):
        for key, val in some_list[x].items():
            print (key, "-", val)
result = iterateDictionary(students)


# 3- Get Values From a List of Dictionaries
# solution:
def iterateDictionary2(name, some_list):
    for x in range (len(some_list)):
        for key, val in some_list[x].items():
            if key==name:
                print (val)
result = iterateDictionary2('first_name', students)



# # 4- Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# # solution:
def printInfo(some_dict):
    for k in some_dict:
        print (len(some_dict[k]), k)
        for x in range (len(some_dict[k])):
            print (some_dict[k][x])
result = printInfo (dojo)

# # amother silution that didnt work:
# def printInfo(some_dict):
#     for key, val in some_dict.items():
#         print len(val)
#         print (key)
#         print (val)        
# printInfo(dojo)