class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("Im a teacher")


class Customer:
    def __init__(self,name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
         print("getting name")
         return self._name

    @name.setter
    def name(self,name):
        print("setting name")
        self._name = name

    @name.deleter
    def name(self):
        del self._name


    def update_membership(self, new_membership):
        self.membership_type =new_membership

    def __str__(self):
        return self.name + "" + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type:
            return True

        return False

    __hash__= None

    __repr__ =__str__



customers = [Customer("Tim", "Gold"),
             Customer("Brad", "Bronze")
             Teacher()]

for user in users:
    user.log()