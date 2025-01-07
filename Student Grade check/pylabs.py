# Hello World
# Let's code the program ...

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import functools
import time
from pathlib import Path
from icecream import ic

# Lets start -->
class FirstCls:
    def __init__(self, init1, data):
        self.init1 = init1
        self.data = data

    @staticmethod
    def system_warning():
        return 'The system encountered an error, try again...'

    @staticmethod
    def welcome_user():
        return 'Welcome, sir. This is my software.'

    @staticmethod
    def goodbye_user():
        return 'Goodbye, sir. Have a nice day!'

    def user_data(self):
        try:
            user_data = {'User_data': self.data}
            with open('user_data.txt', 'a') as file:
                file.write(f"{self.data}\n")
            return user_data
        except Exception as e:
            print(f'Error: {e}')
            return self.system_warning()


class SecondCls(FirstCls):
    def __init__(self, init1, data):
        super().__init__(init1, data)

    def system_functions(self, data):
        try:
            if 80 <= data <= 100:
                print('Your grade is (A+)')
                return 'Excellent'
            elif 70 <= data < 80:
                print('Your grade is (A)')
                return 'Good'
            elif 60 <= data < 70:
                print('Your grade is (B)')
                return 'Satisfactory'
            elif 50 <= data < 60:
                print('Your grade is (C)')
                return 'Needs Improvement'
            elif 35 <= data < 50:
                print('Your grade is (D)')
                return 'Needs Revision'
            elif 0 <= data <= 34:
                print('Your grade is (F)')
                return 'Failed'
            else:
                print('Invalid grade. Please enter a valid grade.')
                return self.system_warning()
        except (TypeError, ValueError):
            return self.system_warning()


# Lets build the User Input layer -->
class LastCls(SecondCls):
    def __init__(self, init1, data):
        super().__init__(init1, data)
        self.user_input = None

    def user_inputs(self):
        print('Please enter your data here:')
        data = input('Enter your total marks: ')
        try:
            data = int(data)  # Convert input to integer
            self.user_input = data
            return self.system_functions(data)
        except ValueError:
            raise ValueError("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    # Example of usage:
    last_instance = LastCls("Example1", 'datas')
    print(LastCls.welcome_user())
    print(last_instance.user_inputs())
    print(last_instance.user_data())
    print(LastCls.goodbye_user())


