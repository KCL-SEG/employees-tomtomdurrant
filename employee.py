"""Employee pay calculator."""
from abc import abstractmethod

"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary}.\nTheir total pay is {self.salary}.'


class HourlyEmployee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def get_pay(self):
        return self.hours * self.hourly_rate

    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour.\nTheir total pay is {self.get_pay()}.'


class SalariedEmployeeWithBonusCommission(SalariedEmployee):
    def __init__(self, name, salary, commission):
        super().__init__(name, salary)
        self.commission = commission

    def get_pay(self):
        return self.commission + super().get_pay()

    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}.\nTheir total pay is {self.get_pay()}.'


class HourlyEmployeeWithBonusCommission(HourlyEmployee):
    def __init__(self, name, hours, hourly_rate, commission):
        super().__init__(name, hours, hourly_rate)
        self.commission = commission

    def get_pay(self):
        return self.commission + super().get_pay()

    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.commission}.\nTheir total pay is {self.get_pay()}.'


class SalaryEmployeeWithContractCommission(SalariedEmployee):
    def __init__(self, name, salary, contracts, commission_per_contract):
        super().__init__(name, salary)
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + self.contracts * self.commission_per_contract

    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract.\nTheir total pay is {self.get_pay()}.'


class HourlyEmployeeWithContractCommission(HourlyEmployee):
    def __init__(self, name, hours, hourly_rate, contracts, commission_per_contract):
        super().__init__(name, hours, hourly_rate)
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + self.contracts * self.commission_per_contract

    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract.\nTheir total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalariedEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', hours=100, hourly_rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployeeWithContractCommission('Renee', salary=3000, contracts=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployeeWithContractCommission('Jan', hours=150, hourly_rate=25, contracts=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalariedEmployeeWithBonusCommission('Robbie', salary=2000, commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployeeWithBonusCommission('Ariel', hours=120, hourly_rate=30, commission=600)
