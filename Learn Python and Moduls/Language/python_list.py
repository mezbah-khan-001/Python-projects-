# Hello wrold this is mezbah khan form backend develoepr 
# Lets create an list and perform operations in this project -->

mezbah = [ 1,2,3,4,5,6,7,8,9,10]
 # frist print the statemnets # 
print(type(mezbah))
print(mezbah)
# lets crate a varriable (result >>) and make it all usefull # 
result01 = mezbah.copy()
print(result01)

# lets add the number (11) in mezbah # 

result02= mezbah.copy()
result02 .append(11)
print(result02)

# lets remove the number (10) from mezbah # 
result03 = result02.copy()
result03.remove(11)
print(result03)

# lets use the slice of dsa(data stracture and algorithoms) in py # 

result04 = result02.copy()
result04[3]= 12121
print(result04)

# lets clean the  result 3 form system index # 

result05 = result02.copy()
result05.clear()
print(result05)

# lets count the index of mezbah in result06 # 

result06= mezbah.copy()
print(len(result06))

#lets use thee 
result07= result02.copy()
result07.pop(2)
print(result07)

# lets uss the insert methods in phy # 
result08= result02.copy()
print(result08[:])
print(result08[::])
print(result08[0:])
print(result08[:5])

# lets uss the insert methods in py #
mezbah01= [1,2,3,4,5,5,5,5,55,5,5,5,5,5,5,21]
index= mezbah01.copy()
result09 = index.count(5)
print("The number of 5 has been use:",result09,"times -->")

# lets cuse a last methods in list functions # 
result10 = result02.copy()
result10.reverse()
print(result10)

# letts use the sortt methods in list functions 
result11= mezbah01.copy()
result11.sort()
print(result11)

# so we use all (bult in functions) methoods in  list 