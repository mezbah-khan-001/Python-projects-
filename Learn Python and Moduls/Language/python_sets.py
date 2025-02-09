# Chapter no 5--> (set functions) 
# we are gonna explore the set function in python 

mezbah = {1,45,767,3498,23098}
istiak = {'python','java','javascript','c++','c#'}

# first lets checck the types of those verriables 
print(type(mezbah))
print(type(istiak)) 
   # Both arew set type #
   # les started our operation # 
   # we have use (set) option for constroctoing sets 
   
ex_set1 = set([23,67,33,323])
print(ex_set1)
print(type(ex_set1))

# started from basic like adding elements 
# lets try or add the in both indentifiers 
ex_set2= mezbah.add(781267)
print(mezbah)

ex_set3 = istiak.add('PhP')
print(istiak)

# succesfully worked # 
# come i show you how to copy sets # 
ex_set4= mezbah.copy()
print(ex_set4)

ex_set5=istiak.copy()
print(ex_set5)

# lets use the remove item of set function # 
ex_set6= mezbah.copy()
ex_set6.remove(45)
print(ex_set6)

ex_set7 = istiak.copy()
ex_set7.remove('c#')
print(ex_set7)

   # anotherwise we can use the pop() method in set # 
ex_set8= mezbah.copy()
ex_set8.pop()   # remove the frist index 
print(ex_set8)

# This is last example of set # 
# we are using the clear () option # 

ex_set9= mezbah.copy()
ex_set9.clear()
print(ex_set9)

ex_set10= istiak.copy()
ex_set10.clear()
print(ex_set10)