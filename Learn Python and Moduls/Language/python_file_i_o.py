  # This is file input output tutorials for beginners

file = open('demo.txt','+a') 
data = file.write("Hello wrold\n")
data = file .write("this is mezbah khan form backend devloper\t")
data = file.read()
print(data)
off_file= file.close()

      # lets use the with option for option for opening file

with open ("demo.txt",'at') as file :
    data = file .write("Im from python background\n")
    data =file .write("Im work in microsoft as a machine learning expert\n")
    print(data)

     #Now i want too read the files 
     #So use the methods for reading line 

text = open("demo.txt",'rt')
text = text.read()
print(text)

  #we have to use the reasdlines methods in order to read the lines 
  #lets create an (text) and use the readlines in the operations 

text= open("demo.txt","r+")
text = text.readlines()
print(text)

  #the code is succesfullu runed So, 
  #lets move the another example. lets to apppend data in file 

text = open ("demo.txt",'+a')
ex_data = text.write("IM Closing the files forever\t")
ex_data = text.write ("goodbye")
print(ex_data)

  #lets finish this game by deleting this file 
  #Specify the file path
import os
os.remove("demo.txt")

    #The operation is succesfully completed 
    #lets build-up an another projects in file input and output 
              # file input/output (I/o) 

with open ("demo.txt","w") as file :
    data = file .write("Hello world\n")
    data = file .write("This is mezbah khan\t from backend developer\n")
    print(data)

with open ("demo.txt",'at') as file :
    data = file .write("Im from python background.\n")
    data =file .write("Im work in microsoft as a machine learning expert\n")
    print(data)

 #Now i want too read the files 
 #So use the methods for reading line 

text = open("demo.txt",'rt')
text = text.read()
print(text)

  # we have to use the reasdlines methods in order to read the lines 
  # lets create an (text) and use the resdlines in the operations 
text= open("demo.txt","r+")
text = text.readlines()
print(text)

# we have used, lets use the append methods in python file again # 
# lets do this and build a successful code # 

text = open ("demo.txt",'+a')
ex_data = text.write("IM Closing the files forever\t")
ex_data = text.write ("goodbye")
print(ex_data)
# lets finish this game by deleting this file # 

import os
# Specify the file path
import os
os.remove("demo.txt")

# Hello wrold this is mezbah khan form backendd develoepr 
# lets create a projects with  file input and output 
# lets buildup this is code with python language 

with open ("demo.txt",'+a') as file:

     # Lets create an input option for recieved user data 
     # we've to save daata in file demo.txt and run for databased 

 with open("demo.txt",'a+') as file:

     new_data= str(input("Enter your Name : "))
     file.write(new_data)
     file.write('\n')

     new_data = int(input("Enter your age : "))
     file.write(str(new_data))
     file.write('\n')

     new_data = float(input("Enter your height : "))
     file.write(str(new_data))
     file.write('\n')

     new_data = str(input('Enter your gender: '))
     file.write(new_data)
     file.write('\n')

     new_data = int(input("Enter your NID number: "))
     file.write(str(new_data))
     file.write('\n')

     new_data = int(input("Enter your phone number: "))
     file.write(str(new_data))
     file.write('\n')

     new_data = str(input("Enter your email: "))
     file.write(new_data)
     file.write('\n')

     # we have done it 
     # lets check the code 