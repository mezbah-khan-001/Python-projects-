#Hello wrold this is mezbah khan from backend developer 
# Lets do this using with dict key-value pair ......

mezbah ={
    "name" :  "mezbah khan",
    "age" : 18,
    "is_adult" : True,
    "contract" : "backeend developer",
    "NiD"  : "Bangladeshi",
    "gradutation" : "SSC passed",
    "adress" : "Dhaka,Bangladesh",
    "email" : "mezbahkhan155@gmail.com",
    "Phone" : 1733512698,
    "github" : "https://github.com/mezbahkhan155",
    "dev_lan": ["python", "javascript"],
    "dev_fram": ["Tensorflow", "flask"],
    "Collage" : "Bm collage",
    "Collage_passing_year" : 2023}

   # lets create the operation in python set file of dict key value pair # 
print(type(mezbah))

 # lets start to go # 
# frist lets use the (acressing method * 3) # 
ex_mezbah01 = mezbah ["name"]
print(ex_mezbah01)
print (mezbah["age"])
print(mezbah['is_adult'])
print(mezbah['Phone'])
 
 # we can also use the get method to get the value of dict key value pair #
ex_mezbah02= mezbah .get('github')
print(ex_mezbah02)
 
  # thats okh lets move forword in our journey # 
# Now lets use the modify elements in python # 

ex_mezbah03= mezbah.copy() 
     # In our name and dev lan value have [ mezbah] , ["python", "javascript"] 
     # we are going to change or modify this values my modify mehthod # 
    
ex1 = ex_mezbah03.get('name')
print(ex1)
ex2= ex_mezbah03.get('dev_lan')
print(ex2)

ex3= ex_mezbah03.copy()
ex3['name'] = "Elon mask"
print(ex3["name"])

ex4= ex_mezbah03.copy()
ex4 ['dev_lan'] = ['python', 'javascript', 'c++']
print(ex4['dev_lan'])

# The modify is successfuly worked so congrats # 
# lets worked with removing elements in python #

     # IN Our dict we have NiD and collage keys, we are going to remove this keys #
     # lets do this with proper indentation #
ex_mezbah04 = mezbah.copy()
ex5 = ex_mezbah04.pop('NiD')
print(ex_mezbah04)

# use the del method to remove the elements in python #
del ex_mezbah04['Collage']
print(ex_mezbah04)

 ## All good happeend in our project #
 ## Lets move more deep in our learing chapter # 
 
 # lets khow about key and value methods in dicts # 
ex_mezbah05= mezbah.copy()
ex6= ex_mezbah05.keys()
print(ex6)
ex7 = ex_mezbah05.values()
print(ex7)

 # lets try the item methods in dicts # 
ex_mezbah06= mezbah.copy()
ex8= ex_mezbah06.items()
print(ex8)

 # we fuond the items so lets try to update to values in dicts # 
ex_mezbah07= mezbah.copy()
ex9 = ex_mezbah07.update({'collage': "hatem ali collage"})
ex10=ex_mezbah07.update({"gradutation" :False})
ex11 = ex_mezbah07.update({"NiD" : "Bangali"})
print(ex_mezbah07)

# yahh update method is successfully workeds so lets try an other method #
# this is all methods of python dict key value pair 