names = []
salary = []
amount = 0
memberscnt = input("Enter famaly members count: ")
mc = int(memberscnt)
for i in range(mc):
    names.append(input("Введите имя " + str(i + 1) + " человека: "))

for i in range(mc):
    salary.append(input("Введите зарплату " + str(i + 1) + " человека: "))


credit = input("Input credit ammount: ")
how_long = input("How long: ")
percent = input("Percent: ")
pay_month = int(credit)/(12 * int(how_long)) + (int(credit)/100 * int(percent))/12

print(pay_month)

for sal in salary:
    amount += int(sal)

mean = (amount - pay_month)/mc

for name in names:
    print(name.title() + "может потрптить " + str(mean))

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
