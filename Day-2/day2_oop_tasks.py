from abc import ABC, abstractmethod
from datetime import datetime
import re

# =========================
# Task 1: Book Class
# =========================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("1984", "George Orwell")
book2 = Book("The Alchemist", "Paulo Coelho")

print("\nTask 1 Output:")
print(book1.title, "-", book1.author)
print(book2.title, "-", book2.author)


# =========================
# Task 2: Laptop Class
# =========================
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

laptops = [
    Laptop("Dell", 800),
    Laptop("HP", 750),
    Laptop("Apple", 1500)
]

print("\nTask 2 Output:")
for l in laptops:
    print(f"{l.brand} - ${l.price}")


# =========================
# Task 3: Employee System (Advanced OOP)
# =========================
class Employee(ABC):
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    def display_info(self):
        print(f"{self.name} | Role: {self.get_role()} | Salary: {self.calculate_salary()}")

    def work(self):
        print("Employee is working")


class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary, benefits):
        super().__init__(name)
        self.annual_salary = annual_salary
        self.benefits = benefits

    def calculate_salary(self):
        return self.annual_salary / 12

    def get_role(self):
        return "Full Time Employee"

    def work(self):
        print("Working full time")

    def yearly_bonus(self):
        return self.annual_salary * 0.1


class Manager(FullTimeEmployee):
    def __init__(self, name, annual_salary, benefits, team_size, bonus_percentage):
        super().__init__(name, annual_salary, benefits)
        self.team_size = team_size
        self.bonus_percentage = bonus_percentage

    def calculate_salary(self):
        return (self.annual_salary / 12) + (self.annual_salary * self.bonus_percentage)

    def get_role(self):
        return "Manager"

    def work(self):
        print("Managing team")

    def manage_team(self):
        print(f"Managing {self.team_size} people")


class Director(Manager):
    def __init__(self, name, annual_salary, benefits, team_size, bonus_percentage, department, stock):
        super().__init__(name, annual_salary, benefits, team_size, bonus_percentage)
        self.department = department
        self.stock = stock

    def calculate_salary(self):
        return (self.annual_salary / 12) + self.stock

    def get_role(self):
        return "Director"

    def work(self):
        print("Directing company strategy")

    def approve_budget(self):
        print("Budget approved")


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked, contract_duration):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.contract_duration = contract_duration

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_role(self):
        return "Contract Employee"

    def work(self):
        print("Working on contract basis")

    def extend_contract(self):
        print("Contract extended")


print("\nTask 3 Output:")
e1 = FullTimeEmployee("Aman", 60000, ["Insurance"])
e2 = Manager("Riya", 90000, ["Insurance"], 10, 0.05)
e3 = Director("Karan", 150000, ["All"], 50, 0.1, "IT", 2000)
e4 = ContractEmployee("Neha", 50, 160, "6 months")

employees = [e1, e2, e3, e4]   # Polymorphism

for e in employees:
    e.display_info()
    e.work()

print("\nMRO of Director:")
print(Director.mro())


# =========================
# Task 4: BankAccount
# =========================
class BankAccount:
    """Simulates abstraction using docstrings"""

    def __init__(self, balance):
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


print("\nTask 4 Output:")
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.get_balance())


# =========================
# Task 5: DataSize
# =========================
class DataSize:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.size}MB"

    def __add__(self, other):
        return DataSize(self.size + other.size)


print("\nTask 5 Output:")
d1 = DataSize(500)
d2 = DataSize(300)
d3 = d1 + d2
print(d3)


# =========================
# Task 6: Team
# =========================
class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


print("\nTask 6 Output:")
team = Team(["A", "B", "C", "D"])
print(len(team))


# =========================
# Task 7 & 8: Dog Class
# =========================
class Dog:
    species = "Canine"
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1


print("\nTask 7 & 8 Output:")
d1 = Dog("Tommy")
d2 = Dog("Rocky")

print(d1.name, "-", d1.species)
print(d2.name, "-", d2.species)
print("Total dogs created:", Dog.count)


# =========================
# Task 9: MathOps
# =========================
class MathOps:
    def square(self, x):
        return x * x

    @classmethod
    def cube(cls, x):
        return x ** 3

    @staticmethod
    def is_even(x):
        return x % 2 == 0


print("\nTask 9 Output:")
m = MathOps()
print(m.square(4))
print(MathOps.cube(3))
print(MathOps.is_even(10))


# =========================
# Task 10: Advanced Employee System
# =========================
class EmployeeSystem:
    company = "GrowByData"
    employees = []
    department_count = {}

    def __init__(self, name, email, salary, department):
        self.name = name
        self.email = email
        self.salary = salary
        self.department = department
        self.employee_id = self.generate_employee_id()

        EmployeeSystem.employees.append(self)

        if department not in EmployeeSystem.department_count:
            EmployeeSystem.department_count[department] = 1
        else:
            EmployeeSystem.department_count[department] += 1

    @classmethod
    def change_company(cls, new_name):
        if 3 <= len(new_name) <= 50 and re.match("^[A-Za-z0-9 ]+$", new_name):
            cls.company = new_name
        else:
            print("Invalid company name")

    @classmethod
    def generate_employee_id(cls):
        year = datetime.now().year
        unique = len(cls.employees) + 1
        return f"EMP-{year}-{str(unique).zfill(4)}"


print("\nTask 10 Output:")
emp1 = EmployeeSystem("Rahul", "rahul@mail.com", 50000, "IT")
emp2 = EmployeeSystem("Simran", "simran@mail.com", 60000, "HR")

print(emp1.employee_id)
print(emp2.employee_id)
print("Company:", EmployeeSystem.company)
print("Departments:", EmployeeSystem.department_count)
