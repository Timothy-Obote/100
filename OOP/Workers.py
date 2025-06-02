class Workers:
    number_of_workers = 11
    
    def __init__(self, name, age, salary, id_number, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.id_number = id_number
        self.gender = gender
        
class Manager(Workers):
    number_of_managers = 1
    salary = 100,000 
    
    def __init__(self, name, age, id_number, gender):
        super().__init__(name,age)
    def pay_salary():
        
    def hire_employee():
        
    def promote_employee():
         
        
class Employee(Workers):
     number_of_employees = 10
     salary = 15,000
     

    
    def __init__(self, name, age, id_number, gender):
        super().__init__(name,age)
        
        
    def ask_for_raise(self):
        print(f"{self.name} is asking for a raise.")
        
    def ask_for_leave(self):
        print(f"{self.name} is asking for a leave")
    
        
        
    