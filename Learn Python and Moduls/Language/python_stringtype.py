  #Hello wrold ,lets code --> 
str1 =  "Hello wrold"
str2 = "Python is a programming language and I love it"
str3= "I am a student of computer science and i love programming"

  # This is our basic (QUA) string and we've to perform operation in this strings 
  # frist lets check the types of this strs (1,2,3) # 

print(type(str1)) 
print(type(str2)) 
print(type(str3)) 

# okey lets print those strs lenght # 
print(len(str1))
print(len(str2))
print(len(str3))

# exclient lets use the indexing of strings also who to slice # 
ex_str1 = str1[0:5]  # slicing
print(ex_str1)

ex_str2 = str1[3] # Indexing
print(ex_str2)

ex_str3 = str2[1:23] # slciing 
print(ex_str3)

ex_str4 = str3[:57] # slicing 
print(ex_str4)

# This is string indexing and slicing of strings # 
# So lets move forword --> Come on i show you to use the (\n) called backslashed N # 

ex_str5 = "hello\nwrold"
print(ex_str5)

# lets use the negitive index of one  last time # 
ex_str6= str3[-32]
print(ex_str6)

ex_str7= str3[0:-4] # Negitive slicing 
print(ex_str7)

# We should never use those negitive indexes # 
# So lets move to our example of strings called uppercase() # 
ex_str8 = str1.upper()
print(ex_str8)

ex_str9 = str3.upper()
print(ex_str9)

# okey lets use the lowercase method in strigs # 
ex_str10 = str2.lower()
print(ex_str10)

ex_str11 = str3.lower()
print(ex_str11)


# lets use the stripts method in strigs # 
ex_str12 = str1.strip()
print(ex_str12)

ex_str13 = str2.strip()
print(ex_str13)

# lets use the string replace method # 
ex_str14= str1.replace("Hello",'Hi')
print(ex_str14)

ex_str15 = str2.replace("Python",'Java')
print(ex_str15)

ex_str16= str3.replace("student",'teacher')
print(ex_str16)

# all methods example is succesfully worked # 
# so lets jumpted on split method # 
ex_str17 =str2.split()
print(ex_str17)

ex_str18 = str3.split()
print (ex_str18)

# lets use the join methds of strings # 
ex_str19 =  ' ' . join(ex_str10)

# Okey lets  use the capitalized mmethod # 
ex_str20 = str2.capitalize()
print(ex_str20)

#  we have already coverup our chapter # 
# lets finished with last 2 items #
ex_str21= str2.find("a")
print(ex_str21)

ex_str22= str3.find("student")
print(ex_str22)

# Thsis is our last method of string # 
ex_str23= str2.count('programming')
print(ex_str23)

ex_str24 = str3.count('science')
print(ex_str24)

# This is hole examples of strings methods in Python # 

          #Chapter no 2 --> List methods 
mezbah = [2,17,345,85,64,19087]  # this is our frist list [1]
istiak = ["mezbah_khan","noman_bhai","tomo_bhai","sagor_bhai","mamun_bhai"]  # this is secend list [2]

# frist lets check this list type #
print(type(mezbah))  
print(type(istiak))

    # All good, lets create our operations # 
    # frist lets use the indexing method # 

ex_mezbah01 = mezbah.copy()
print(ex_mezbah01[0])
print(ex_mezbah01[4])

# this is istiak's example 
ex_istiak01 = istiak.copy()
print(ex_istiak01[0])
print(ex_istiak01[2]) 

# we ahve use the indexing methods # 
# lets methods in indexing py list # 

ex_mezbah02 = mezbah.copy()
print (ex_mezbah02[0:])
print (ex_mezbah02[:5])
print(ex_mezbah02[::])
print(ex_mezbah02[0:3])
print(ex_mezbah02[2:3])
print(ex_mezbah02[2:5])

# lets find one of indexes with methods # 
print(ex_mezbah02.index(345))

 # this is for istiak example # 
ex_istiak02= istiak.copy()
print(ex_istiak02[0:])
print(ex_istiak02[:5])
print(ex_istiak02[0:3])
print(ex_istiak02[2:3])
print(ex_istiak02[1:4])

# lets find one of indexes with methods #
print(ex_istiak02.index("tomo_bhai"))

# this all indexing method in py as list function # 
# lets add some value in this list with apppend methods # 

ex_mezbah03= mezbah.copy()
ex_mezbah03.append(176523)
print(ex_mezbah03)

# this is example of istiak # 
ex_istiak03= istiak.copy()
ex_istiak03.append ("sakil_bhai")
print(ex_istiak03)

# the apppend method is worked 
# lets used the insert method 
ex_mezbah04= mezbah.copy()
ex_mezbah04.insert(1,1256)
print(ex_mezbah04)

# this is example of istiak #
ex_istiak04= istiak.copy()
ex_istiak04.insert(2,"shimul_bahi")
print(ex_istiak04)

# yaaah the code is worked # 
# lets do another method named extend in PYTHON # 
ex_mezbah05= mezbah.copy()
ex_another01= [21,32,43]
ex_mezbah05.extend(ex_another01)
print(ex_mezbah05)

# this  is istiak example # 
ex_istiak05= istiak.copy()
ex_another02 =["akash_bhai",'dolon_bhai']
ex_istiak05.extend(ex_another02)
print(ex_istiak05)

# The code is sussesfully worked and runnable code # 
# lets do another method named remove in PYTHON #
ex_mezbah06= mezbah.copy()
ex_mezbah06.remove(2)
print(ex_mezbah06)

 # this is istiak example #
ex_istiak06= istiak.copy()
ex_istiak06.remove("noman_bhai")
print(ex_istiak06)
 
 # the rmove method is succesfully worked #
 # lets create an example of pop method in PYTHON # 

ex_mezbah07= mezbah.copy()
ex_mezbah07.pop(1)
print(ex_mezbah07)

# this is example of istiak # 
ex_istiak07= istiak.copy()
ex_istiak07.pop(3)
print(ex_istiak07)

# the code is worked so lets move on the next method # 
# lets create an example of delete method in PYTHON #
# we are going to use the (del) method # 

ex_mezbah08= mezbah.copy()
del ex_mezbah08[4] # remove index 
print(ex_mezbah08)

#this is example of istiak #
ex_istiak08 = istiak.copy()
del ex_istiak08[4]
print(ex_istiak08)

# the code os worked so lets move to the next method # 
# lets create a another method of clean funtion # 
# lests do it # 
ex_mezbah09= mezbah.copy()
ex_mezbah09.clear()
print(ex_mezbah09)
 
 # the code is worked # 
 # this is example of istiak # 
ex_istiak09= istiak.copy()
ex_istiak09.clear()
print(ex_istiak09)
 
 # both code is successfully worked SO # 
#  lets jumped the another method callled modify function # 
# lets do this # 
ex_mezbah010 = mezbah.copy()
ex_mezbah010[3] = 23901
print (ex_mezbah010)

# we should pratice the modify method method more #

ex_mezbah010[2]= 1090910
print(ex_mezbah010)

# this is example of istiak # 
ex_istiak010 =istiak.copy()
ex_istiak010[2]= "mezbah_khan"
print(ex_istiak010)

 # we should pratice the modify method method more #
ex_istiak010[1]='istiak_bhai'
print(ex_istiak010)
 
 # both code is succesfully worked so lets try a another game # 
 # lets create example of list length methods in PYTHON # 
 
ex_mezbah11= mezbah.copy()
print(ex_mezbah11.count(2))
print(ex_mezbah11.count(17))

# this is example of istiak #
ex_istiak11= istiak.copy()
print(ex_istiak11.count("mamun_bhai"))
print(ex_istiak11.count("tomo_bhai"))

# The example is outstanding so lets create a another projects # 
# lets try the sort method in python # 
ex_mezbah12= mezbah.copy()
ex_mezbah12.sort()
print(ex_mezbah12)

# this is example of istiak #
# the sort method use to colllect values by serially # 
# so lets try the reverse method in python #

ex_mezbah13 = mezbah.copy()
ex_mezbah13.reverse()
print(ex_mezbah13)

# this is example of istiak #
ex_istiak13 = istiak.copy()
ex_istiak13.reverse()
print(ex_istiak13)

# both code is worked so lets try a another game #
# lets try last 2 methods like (len) list python # 

ex_mezbah14 = mezbah.copy()
print(len(ex_mezbah14))

# this is example of istiak #

ex_istiak14 = istiak.copy()
print(len(ex_istiak14))

# this is last method of python list function # 
# we are going fan in this code  and thats is (type)

ex_mezbah15= mezbah.copy()
ex_istiak15= istiak.copy()

print(type(ex_mezbah15))
print(type(ex_istiak15))