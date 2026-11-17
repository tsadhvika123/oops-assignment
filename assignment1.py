
"""

topic: constructor, class attributes and instance attributes


1. constructor:
a constructor is a special method in python that is automatically
called when an object is created.

it is defined using __init__().

it is used to initialize the attributes of an object.


2. class attributes:
class attributes are variables declared inside a class but
outside the constructor and other methods.

they are shared by all objects of the class.

example: college name, company name, number of wheels.


3. instance attributes:
instance attributes are variables that belong to individual objects.

they are usually declared inside the constructor using self.

each object can have different values.

example: student name, age, employee salary.


4. difference between class attributes and instance attributes:

class attributes:
- belong to the class.
- shared by all objects.
- declared outside the constructor.
- accessed using the class name or object.

instance attributes:
- belong to individual objects.
- can have different values for each object.
- usually declared inside the constructor.
- accessed using the object name.


------------------------------------------------------------
program 1: student class
------------------------------------------------------------
"""


class student:

    college = "st martin's engineering college"  # class attribute

    def __init__(self, name, age, course):
        self.name = name       # instance attribute
        self.age = age         # instance attribute
        self.course = course   # instance attribute

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("course:", self.course)
        print("college:", student.college)


s1 = student("sadhvika", 22, "ai and data science")
s2 = student("rahul", 23, "computer science")

print("student 1 details:")
s1.display()

print()

print("student 2 details:")
s2.display()


"""
output:

student 1 details:
name: sadhvika
age: 22
course: ai and data science
college: st martin's engineering college

student 2 details:
name: rahul
age: 23
course: computer science
college: st martin's engineering college


------------------------------------------------------------
program 2: employee class
------------------------------------------------------------
"""


class employee:

    company = "tcs"  # class attribute

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        print("name:", self.name)
        print("employee id:", self.employee_id)
        print("salary:", self.salary)
        print("company:", employee.company)


e1 = employee("sadhvika", 101, 25000)
e2 = employee("priya", 102, 30000)

print("employee 1 details:")
e1.display()

print()

print("employee 2 details:")
e2.display()


"""
output:

employee 1 details:
name: sadhvika
employee id: 101
salary: 25000
company: tcs

employee 2 details:
name: priya
employee id: 102
salary: 30000
company: tcs


------------------------------------------------------------
program 3: car class
------------------------------------------------------------
"""


class car:

    wheels = 4  # class attribute

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display(self):
        print("brand:", self.brand)
        print("model:", self.model)
        print("color:", self.color)
        print("wheels:", car.wheels)


c1 = car("tata", "nexon", "black")
c2 = car("hyundai", "creta", "white")

print("car 1 details:")
c1.display()

print()

print("car 2 details:")
c2.display()


"""
output:

car 1 details:
brand: tata
model: nexon
color: black
wheels: 4

car 2 details:
brand: hyundai
model: creta
color: white
wheels: 4


------------------------------------------------------------
conclusion:

- constructor is used to initialize objects.
- __init__() is automatically called when an object is created.
- self refers to the current object.
- class attributes are shared among all objects.
- instance attributes belong to individual objects.
"""
