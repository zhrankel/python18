name1 = input("Введите имя первого человека")
name2 = input("Введите имя второго человека")
name3 = input("Введите имя третьего человека")

salary1 = input("Введите зарплату первого: ")
salary2 = input("Введите зарплату второго: ")
salary3 = input("Введите зарплату третьего: ")

credit = input("Input credit ammount: ")
how_long = input("How long: ")
percent = input("Percent: ")
pay_month = int(credit)/(12 * int(how_long)) + (int(credit)/100 * int(percent))/12

print(pay_month)
# mean = str((int(salary1) + int(salary2) + int(salary3))/3)
# print(name1 + " Может потратить: " + mean)
# print(name2 + " Может потратить: " + mean)
# print(name3 + " Может потратить: " + mean)




# print("Privet User!")
# name = input("Type your name: ")
# name = name.strip()
# print("Welcome " + name.title())
#
# stroka = "Gvatemala 'strana' s teplym klimatom"
# entry1 = int(input("Введите первое число: "))
# entry2 = int(input("Введите первое число: "))
# print(entry1 + entry2)
