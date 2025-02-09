# Hello World ...
# LET'S code the designed program ---> 

import numpy as np
import pandas as pd
import os, sys, time
from faker import Faker

class Homeclass:
    """This project is created by Mezbah Khan"""

    def __init__(self, data, ai_data):
        self.data = data
        self.ai_data = ai_data

    @staticmethod
    def warning_call():
        return "The system encountered an ERROR."

class SystemFunctions(Homeclass):
    """This class handles function-based operations"""

    def __init__(self, data, ai_data):
        super().__init__(data, ai_data)

    def humanoid_functions(self):
        print("1. Enter your password as a String")
        print("2. Enter your password as an Integer")
        print("3. Enter your password as a Float")

        try:
            choice = int(input("Enter your choice (1/2/3): "))

            if choice == 1:
                user_input = input("Enter your password (String): ")
            elif choice == 2:
                user_input = int(input("Enter your password (Integer): "))
            elif choice == 3:
                user_input = float(input("Enter your password (Float): "))
            else:
                print("Invalid choice!")
                return
            
            print(f"Your saved password: {user_input}")

            # Save input to file --> 
            with open("Humanoid_data.txt", "a") as file:
                file.write(f"Humanoid Password: {user_input}\n")

        except (ValueError, TypeError):
            print(self.warning_call())

    def ai_functions(self):
        print("1. Generate AI-based password (String)")
        print("2. Generate AI-based password (Integer)")
        print("3. Generate AI-based password (Float)")

        try:
            choice = int(input("Enter your choice (1/2/3): "))
            fake = Faker()

            if choice == 1:
                ai_password = fake.password(length=12, digits=True, upper_case=True, lower_case=True)
            elif choice == 2:
                ai_password = np.random.randint(1000, 9999)
            elif choice == 3:
                ai_password = round(np.random.uniform(1000.0, 9999.0), 2)
            else:
                print("Invalid choice!")
                return

            print(f"Generated AI Password: {ai_password}")

            # Save AI-generated password to file
            with open("AI_data.txt", "a") as file:
                file.write(f"AI Password: {ai_password}\n")

        except (ValueError, TypeError):
            print(self.warning_call())

    def humanoid_data(self):
        try:
            return {"User_data": [self.data]}
        except (ValueError, TypeError):
            return self.warning_call()

    def ai_dataset(self):
        try:
            return {"User_data": [self.ai_data]}
        except (ValueError, TypeError):
            return self.warning_call()


class SystemCalls(SystemFunctions):
    """This class handles system call-based operations"""

    def __init__(self, data, ai_data):
        super().__init__(data, ai_data)

    def run(self):
        print("1. Use Humanoid Functions")
        print("2. Use AI-based Functions")

        try:
            choice = int(input("Enter your choice (1/2): "))

            if choice == 1:
                self.humanoid_functions()
            elif choice == 2:
                self.ai_functions()
            else:
                print("Invalid choice!")

        except ValueError:
            print(self.warning_call())


if __name__ == "__main__":
    instance = SystemCalls("User123", "AI_456")
    instance.run()
   