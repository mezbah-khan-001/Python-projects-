# Hello world this is Mezbah Khan from backend developer
# Let's create a project based on humanoid and AI lock system
# Let's do this with proper code....
!pip install faker
import numpy as np
import pandas as pd
import os
import time
from faker import Faker

class FirstCls: 
    intro = 'The project is built by Mezbah Khan.'
    
    def __init__(self, data, ai_data): 
        self.data = data 
        self.ai_data = ai_data
    
    @staticmethod
    def warn(): 
        print('The system is closed....')
        
    def humanoid_dataset(self): 
        try: 
            return {'user_data': [self.data]}
        except ValueError: 
            self.warn()
            return None

    def ai_dataset(self): 
        try: 
            return {'user_data': [self.ai_data]}
        except ValueError: 
            self.warn()
            return None

class SecondCls(FirstCls): 
    welcome = 'The project is based on AI and Humanoid.'
    
    def __init__(self, data, ai_data, lock): 
        self.lock = lock 
        super().__init__(data, ai_data)
        
    def first_function(self):
        if isinstance(self.data, (int, float, str)):
            with open('humanoid_model.txt', 'a') as file:
                file.write(f'This is user data: {self.data}\n')
            print('1. Set an integer password')
            print('2. Set a floating password')
            print('3. Set a string password')
            try:
                user_choice = int(input('Enter your choice: '))
                if user_choice == 1:
                    self.data = int(input('Enter your password: '))
                elif user_choice == 2:
                    self.data = float(input('Enter your password: '))
                elif user_choice == 3:
                    self.data = input('Enter your password: ')
                else:
                    print('Invalid choice!')
                print(f'This is your password: {self.data}')
            except (TypeError, ValueError):
                self.warn()
    
    def second_function(self):
        if isinstance(self.ai_data, (int, float, str)):
            with open('Ai_based_model.txt', 'a') as file:
                file.write(f'This is user data: {self.ai_data}\n')
            print('1. Set AI-based integer password')
            print('2. Set AI-based string password')
            print('3. Set AI-based floating password')
            try:
                user_choice = int(input('Enter your choice: '))
                if user_choice == 1:
                    self.ai_data = np.random.randint(4500, 10000, 450).sum()
                elif user_choice == 2:
                    self.ai_data = Faker().password(length=12, digits=True, upper_case=True, lower_case=True)
                elif user_choice == 3:
                    self.ai_data = np.random.uniform(1232.0, 2938.0)
                else:
                    print('Invalid choice!')
                print(f'This is your AI password: {self.ai_data}')
            except (ValueError, TypeError):
                self.warn()
                
class ThirdCls(SecondCls):
    function = 'This project is focused on data locking...'
    
    @classmethod
    def user_call_choice(cls):
        print('1. Use humanoid lock pattern...')
        print('2. Use AI lock pattern...')
        
        try:
            choice = int(input('Enter your choice: '))
            instance = cls(10, 20, 'lock')  # Creating an instance with dummy data
            
            if choice == 1:
                instance.first_function()
            elif choice == 2:
                instance.second_function()
            else:
                print('Invalid choice!')
        except ValueError:
            print('Invalid input! Please enter a valid number.')
        except TypeError:
            cls.warn()

if __name__ == "__main__": 
    ThirdCls.user_call_choice()
 
    
   # the project is complete .. 
   # hope you like it 
