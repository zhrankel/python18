# calculate the user's age
# author: Boris Kaiser

import re

age = None
next_year = None
cur_year = 2020

while not age:
    age = input("Enter your current age (please type only digits): ")
    if not re.search(r"^[0-9]+$", age):
        print("Try again, and enter only digits")
        age = None

while not next_year:
    next_year = input("Enter the year, you whant to calculate your age (greater than 2020): ")
    if not re.search(r"202[1-9]|20[1-9][0-9]|21[0-9]{2}", next_year):
        next_year = None
        print("Sorry, but year should be greater than 2020")

future_age = str(int(next_year) - 2020 + int(age))
print(f'Dear %USERNAME%, your age in {next_year} is {future_age}')