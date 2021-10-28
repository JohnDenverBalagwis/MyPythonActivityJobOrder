name = input("enter name: ").strip()
typeOfEmp = input("type of employee: ").strip()

if not (typeOfEmp.lower() == 'regular'or typeOfEmp.lower() == 'casual' or typeOfEmp.lower() ==  'job order'):
    sys.exit()

daysWorked = int(input("days worked: "))
OverTime = int(input("OverTime: "))

if name == 'regular':
    rate = 800
    over = 0.15
elif name == 'casual':
    rate = 400
    over = 0.08
else:
    rate = 615
    over = 0.1

regSalary = daysWorked * rate
overtimeSalary = (rate * over) * OverTime
OverAllSalary = regSalary + overtimeSalary

print(f"{name} his salary is P {OverAllSalary} pesos!")