 #   Chapter no 4--> (Tupple)

mezbah = (2,45,983,1534,89325)
istiak= ("mezbah khan",'Noman bhai','mamun bhai','tomo bhai','sagor bhai')

# frist lets cheeck the types of those verriables # 
print(type(mezbah))
print(type(istiak))

# As frist operation lets try indexing and slicing methods # 
ex_tup1 = mezbah[2]
print(ex_tup1)

ex_tup2 = istiak[2]
print(ex_tup2)  
 
ex_tup3 = mezbah[0:]
print(ex_tup3)

ex_tup4 = istiak[0:]
print(ex_tup4)

ex_tup5 = mezbah[:-3]
print(ex_tup5)

ex_tup6 = istiak[:-2]
print(ex_tup6)

ex_tup7 = mezbah [2:4]
print(ex_tup7)

ex_tup8 = istiak[1:3]
print(ex_tup8)

# This is indexing and slicing examples # 
# we are goona concatinate tupls #  
con1 =  (mezbah + istiak)
print(con1)

   # for example lets create an another tup and concatinate both # 
Repo_acc = ('chattgpt','Gimini','blueebard', 'skyff',344) 
project_acc= (12,'Github','Gitlab','Git','Terminal')

github_acc= (Repo_acc + project_acc)
print(github_acc)

   # This who anyone can concatinate tupples # 
   #lets count the tupple # 
   
ex_tup9= mezbah.count(2)
print(ex_tup9)

ex_tup10 = istiak.count("sagor bhai")
print(ex_tup10)

 #c this is count method example # 
 # Lets try the index method # 
 
ex_tup11= mezbah.index(2)
print(ex_tup11)

ex_tup12= istiak.index("mamun bhai")
print(ex_tup12)

 # A Tupple have imutibility So we can modify # 
 # lets modify both methods # 
 
modified_mezbah = mezbah + (1000,)
print("Modified Mezbah Tuple:", modified_mezbah)

modified_istiak = istiak[:1] + ("Updated Name",) + istiak[2:]
print("Modified Istiak Tuple:", modified_istiak)

# This  is all example of tupple in python # 