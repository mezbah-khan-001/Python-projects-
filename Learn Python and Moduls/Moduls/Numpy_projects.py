# hello wrold this is mezbah khan form backend developer.lets create an array  with numpy and linked with fucntion of [python] dataset 
# Also add an loop function for data for input user like(Customer or datausers). So lets do this woth proper codes in python language 

import numpy as np
class Mezbah:
    def __init__(self, file_int):
        self.file_int = file_int
        self.file_fnt = [int(i) for i in file_int.split(',')]
        self.svt_dta = np.array(self.file_fnt)
        
    def hello():
        print('Hello wrold')
        
    def input_dta(self):
        return self.file_fnt

    def save_dta(self):
        return self.svt_dta

file_int = input("Enter your data: ")
system_check = Mezbah(file_int)
print('This is your data as array : ', system_check.save_dta()) 

# helloworld this is mezbah khan from  backend dveeloepr 
# l ets creat  an AI model 
#  lets d o this 

import numpy as np

# Let's create a class
class Mezbah:
    def __init__(self, loop):
        self.loop = loop 
        
    # Let's create a static method to welcome the user
    @staticmethod
    def hello():
        print('Hello user, this is your loop:')
        
    def val_loop(self, start, end):
        self.loop = 0
        str_dta = np.arange(start + 1, end + 1)  # Create an array with the loop data
        for val in str_dta:
            print(val)
        return str_dta
        
frist_idx = int(input('Enter your starting index: '))
secend_idx = int(input('Enter your stopping index: '))

# Let's create an object for our class
system_check = Mezbah(0)
system_check.hello()
dis_loop_dta = system_check.val_loop(frist_idx, secend_idx)

print('This is loop data in array format:', dis_loop_dta)


