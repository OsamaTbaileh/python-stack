# first = "osama"
# last = "ammar"
# print (f"my name is {first} {last}")

# first="osama"
# last="ammar"
# print ("my name is {} {}".format(first, last))

# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27

# name="osama"
# print(name.title())

# osama=["oss","ammar",12,55]
# print(osama[0])

# osama ={"first":"osama", "last":"ammar"}
# osama["first"]="ahmad"
# osama ["hobbies"]=["orange","blue"]
# # print (osama)
# w = osama.pop("first")
# print (w)
# print (osama)

# for osama in range (0,5,1):
#     print(osama)

# koko=["osama","ammar",666]
# for x in range (0,len(koko),1):
#     print (koko[x])

# mimi =["osama", "ammar", 777]
# for x in mimi:
#     print (x)

# dic ={ "name":"osama", "age":55 , "last":True}
# for x in range (0,len(dic),1):
#      print (dic[x])

# dic = { "name": "osama", "age": "55", "last": "True" }
# for x in dic:
#     print(X)

# my_dict = { "name": "Noelle", "language": "Python" }
# for k in my_dict:
#     print(k)
# # output: name, language

# just = {"name": "osama", "last":"ammar", "momo": "frizby"}
# for h in just:
#     print (h)

# just = {"name": "osama", "last":"ammar", "momo": "frizby"}
# for so in just.values():
#     print(so)

# just = {"name": "osama", "last":"ammar", "momo": "frizby"}
# for so,ll in just.items():
#     print(so,"=",ll)


# jiji=0
# while jiji<8:
#     print (jiji)
#     jiji+=1

# for x in "String":
#     if x=="i":
#         break
#     print("gg")


#     function buildPalindrome(st) {
#     var i = 0;
#     var aux;
#     while(st != st.split('').reverse().join('')){
#         aux = st.split('')
#         aux.splice(st.length-i, 0 ,st[i])
#         st = aux.join('');
#         i++;
#     }
#     return st;
# }
# var x =buildPalindrome("osama");

# osama = { "first":"jojo", "last":"hoho", "age":55}
# for x in osama:
#     print (x)  or print (osama[x])

# for key in osama.keys()
#     print (ket)

# for val in osama.values()
#     print (val)

# for x, y in osama.items():
#     print (key,"=",val)

# def ultimate_analysis(array):
#     myDictonary = {'sumTotal': 0, 'average': 0, 'minimum': array[0], 'maximun': array[0], 'length': len(array)}
#     for val in array:
#         if myDictonary['minimum']<val:
#             myDictonary['minimum'] = val
#         if myDictonary['maximun']>val:
#             myDictonary['maximun'] = val
#         myDictonary['sumTotal']+= val
#         myDictonary['average']=myDictonary['sumTotal']/len(array)
#     return myDictonary
# print(ultimate_analysis([1,2,1,2,4,0]))
# print(ultimate_analysis([1,0]))
# print(ultimate_analysis([15,4,1,0]))

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(some_dict):
#     for key, val in some_dict.items():
#         print (len(val))
#         print (key)
#         print (val)        
# printInfo(dojo)

users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]   
x = users
print (x[0]['first_name'])