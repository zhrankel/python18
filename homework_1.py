# calculate the user's age
age = input("Enter your current age: ")
next_year = input("Enter the year, you whant to calculate your age: ")
cur_year = 2020
future_age = str(int(next_year) - 2020 + int(age))
print(f'Dear %USERNAME%, your age in {next_year} is {future_age}')