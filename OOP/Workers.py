class Workers:
    number_of_workers = 0
    all_workers = []
    
    def __init__(self, name, age, salary, id_number, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.id_number = id_number
        self.gender = gender
        
        Workers.number_of_workers += 1
        Workers.all_workers.append(self)

def get_profile(self):
    return {
        'Name': self.name,
        'Age': self.age,
        'Gender':self.gender,
        'Salary': self.salary,
        'ID Number': self.id_number,
    }    
        
class Manager(Workers):
    number_of_managers = 0
    
    
    def __init__(self, name, age, id_number, gender):
        salary = 100,000 
        super().__init__(name,age, salary, id_number, gender):
        Manager.number_of_managers += 1
        
        
    def pay_salary(self, employee):
       print(f"{self.name} is paying salary to {employee.name}: ${employee.salary}") 
        
    def hire_employee(self, name, age, id_number, gender):
        new_employee = Employee(name, age, id_number, gender)
        print(f"{self.name} has hired {new_employee.name}")
        return new_employee

    def promote_employee(self, employee, raise_amount):
        old_salary = employee.salary
        employee.salary += raise_amount
         
        
class Employee(Workers):
    number_of_employees = 0

    def __init__(self, name, age, id_number, gender):
        salary = 15000  # Default employee salary
        super().__init__(name, age, salary, id_number, gender)
        Employee.number_of_employees += 1

    def ask_for_raise(self):
        print(f"{self.name} is asking for a raise.")

    def ask_for_leave(self):
        print(f"{self.name} is asking for a leave.")


# Example usage
mgr = Manager("Alice", 40, "MGR001", "Female")
emp1 = mgr.hire_employee("Bob", 25, "EMP001", "Male")
emp2 = mgr.hire_employee("Carol", 30, "EMP002", "Female")

emp1.ask_for_raise()
mgr.promote_employee(emp1, 5000)
mgr.pay_salary(emp1)

        
    