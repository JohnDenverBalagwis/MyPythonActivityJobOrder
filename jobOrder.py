regRate, otRate = 0, 1

typeEmpList = ['regular', 'casual', 'job order']
salaryRate = [[800, 0.15], [400, 0.08], [615, 0.1]]

name = input("Enter Name: ").strip()
typeOfEmp = input("Enter Type of Employee (regular, casual, job order): ").strip().lower()

if(typeOfEmp in typeEmpList):
    
    getEmpRegRateIndex = typeEmpList.index(typeOfEmp);
    
    daysWorked = int(input("Input No of Days Worked: "))
    overTime = int(input("Input Overtime Worked: "))
    
    regSalary = daysWorked * salaryRate[getEmpRegRateIndex][regRate]
    overTimeSalary = (salaryRate[getEmpRegRateIndex][regRate] * salaryRate[getEmpRegRateIndex][otRate]) * overTime
    overAllSalary = regSalary + overTimeSalary
    
    print(f"{name} his/her salary is P {overAllSalary} pesos")
else:
    print("PLEASE Select Correct Employee Type!")