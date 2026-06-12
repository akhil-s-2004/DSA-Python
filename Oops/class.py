class Employee:
    # pass -- use pass when the class need not be used or defined right now
    
    #class variables
    raise_amt = 1.10
    employee_count = 0
    def __init__(self,first,last,pay):      # __init__ is the constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.employee_count += 1 # use this only using class name(no instance name)

    #Methods 
    def fullname(self):
        return self.first + " " + self.last
    
    def salary_raise(self):
        self.pay *= self.raise_amt              #using self.raise_amt because we need to either access
        #self.pay *= Employee.raise_amt         using class name or instance(self here)   
    
emp1 = Employee("Akhil","Nair",35000)
emp2 = Employee("Alan","Siju",40000)

#Following both are same
# print(Employee.fullname(emp1))
# print(emp1.fullname()) 

print(Employee.employee_count)  

print(emp1.pay)
emp1.salary_raise()
print(emp1.pay)
print(emp1.__dict__)   # output : {'first': 'Akhil', 'last': 'Nair', 'pay': 38500.0, 'email': 'Akhil.Nair@company.com'} 
emp1.raise_amt = 1.20
emp1.salary_raise()
print(emp1.pay)
print(emp1.__dict__)   #{'first': 'Akhil', 'last': 'Nair', 'pay': 46200.0, 'email': 'Akhil.Nair@company.com', 'raise_amt': 1.2}

#Here as we can see when the raise_amt was updated using 
#emp1(for itself), raise_amt bacame instance variable for emp1(not for other employees)


#The following is required when there is no constructor and is not an ideal process
# emp1 = Employee()
# emp2 = Employee()
# emp1.first = "Alan"
# emp1.last = "Siju"
# emp1.email = "Alan.Siju@company.com"
# emp1.pay = 40000

# emp2.first = "Alin"
# emp2.last = "Saiju"
# emp2.email = "Alin.Saiju@company.com"
# emp2.pay = 50000
