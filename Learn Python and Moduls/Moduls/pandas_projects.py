# Hello wrold this is mezbah khan form backend develoer
# Lets create the dataframe with pandas and use the numarical data for dataset 
# Lets do this with numpy and pandas

 
import numpy as np 
import pandas as pd 

# Let's create the class with operations
class FristInstructor: 
    hello = 'This system is created by Mezbah Khan'
    
    def __init__(self, num, array, sum1): 
        self.num = num 
        self.array = array
        self.sum1 = sum1
  
    # Let's create the warning 
    @staticmethod
    def warning():  
        return 'Only numerical values and personal data are allowed!'
    
    # This is the first function
    def frist_function(self):  
        if isinstance(self.num, int) and isinstance(self.sum1, int) and all(isinstance(i, int) for i in self.array): 
            with open('demo.txt', 'w+') as file: 
                file.write(f'{self.num}\n{self.sum1}\n{self.array}\n')
        else: 
            print('System error!')

# Let's create the user input data function 
user_input = {}
user_input['num'] = int(input('Enter your roll number: '))
user_input['array'] = list(map(int, input('Enter your result numbers separated by commas: ').split(',')))
user_input['sum1'] = int(input('Enter your total number in subjects: '))

# Let's recall the system for error check 
system_check01 = FristInstructor(**user_input)
print(system_check01.hello)
print(system_check01.warning())
system_check01.frist_function()

# This is the class object of FristInstructor  
class SecendInstructor(FristInstructor):
    welcome = 'This system is designed by Mezbah Khan'
    
    def __init__(self, file_int):
        self.file_int = file_int
    
    # Let's create the alert 
    @staticmethod
    def alert():
        print('The system will check your data!')
        return 'Ensure your data as well'
    
    def secend_function(self, file_int):
        self.file_int = [int(i) for i in file_int.split(',')] 
        save_data = np.array(self.file_int)
        with open('array_data.txt', 'w+') as file:
            np.savetxt(file, save_data, fmt='%d')
        return save_data

# Example user input for SecendInstructor
user_input_secend = input('Enter your data like [12,23,4,5,67,434,232,12]: ')
system_check02 = SecendInstructor(user_input_secend)
print(system_check02.welcome)
print(system_check02.alert())
array_data = system_check02.secend_function(user_input_secend)
print('This is the array data:', array_data)

# Create a DataFrame with the numerical data
df = pd.DataFrame(array_data, columns=['Data'])
print(df)

# Hello wrold this is mezbah khan form backend develoer
# Lets create the dataframe with pandas and use the numarical data for dataset 
# Lets do this with numpy and pandas

 
import numpy as np 
import pandas as pd 

# Let's create the class with operations
class FristInstructor: 
    hello = 'This system is created by Mezbah Khan'
    
    def __init__(self, num, array, sum1): 
        self.num = num 
        self.array = array
        self.sum1 = sum1
  
    # Let's create the warning 
    @staticmethod
    def warning():  
        return 'Only numerical values and personal data are allowed!'
    
    # This is the first function
    def frist_function(self):  
        if isinstance(self.num, int) and isinstance(self.sum1, int) and all(isinstance(i, int) for i in self.array): 
            with open('demo.txt', 'w+') as file: 
                file.write(f'{self.num}\n{self.sum1}\n{self.array}\n')
        else: 
            print('System error!')

# Let's create the user input data function 
user_input = {}
user_input['num'] = int(input('Enter your roll number: '))
user_input['array'] = list(map(int, input('Enter your result numbers separated by commas: ').split(',')))
user_input['sum1'] = int(input('Enter your total number in subjects: '))

# Let's recall the system for error check 
system_check01 = FristInstructor(**user_input)
print(system_check01.hello)
print(system_check01.warning())
system_check01.frist_function()

# This is the class object of FristInstructor  
class SecendInstructor(FristInstructor):
    welcome = 'This system is designed by Mezbah Khan'
    
    def __init__(self, file_int):
        self.file_int = file_int
    
    # Let's create the alert 
    @staticmethod
    def alert():
        print('The system will check your data!')
        return 'Ensure your data as well'

    def secend_function(self, file_int):
        self.file_int = [int(i) for i in file_int.split(',')] 
        save_data = np.array(self.file_int)
        with open('array_data.txt', 'w+') as file:
            np.savetxt(file, save_data, fmt='%d')
        return save_data

# Example user input for SecendInstructor
user_input_secend = input('Enter your data like [12,23,4,5,67,434,232,12]: ')
system_check02 = SecendInstructor(user_input_secend)
print(system_check02.welcome)
print(system_check02.alert())
array_data = system_check02.secend_function(user_input_secend)
print('This is the array data:', array_data)

# Create a DataFrame with the numerical data
df = pd.DataFrame(array_data, columns=['Data'])
print(df)

secend_idx = int(input('Enter your stopping index: '))

# Let's create an object for our class
system_check = Mezbah(0)
system_check.hello()
dis_loop_dta = system_check.val_loop(frist_idx, secend_idx)

print('This is loop data in array format:', dis_loop_dta)


