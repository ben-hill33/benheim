## Classes and Objects

This article will describe each of these concepts, illustrate each concept as a class diagram, and dive into some examples by hammering out some Python code implementations.

Core to object-oriented programming are the following concepts:

### Encapsulation

??? "The idea that data inside an object is protected from the outside... Kinda like this content admonition has a dropdown feature that contains more on encapsulation."

    === "Description"

    	Also known as _data hiding_ because it hides the data being used inside the object or class from any code that's outside the object or class.
    	
        _Implementation_ in Python involves hidden attributes to store data within the class and public methods to access the data from outside the class.

      	- A method that gets hidden data from a class is called **accessor** and often uses `get` as part of its name.
      	- A method that changes a hidden variable is called a **mutator** and often uses `set` as part of its name.
      	- In Python, hidden variables start with a single underscore or double underscore
          	- A single underscore indicates to programmers that the attribute should _not_ be accessed directly from outside the class.
          	- A double underscore (aka _dunder_ in Python) causes the underlying name to be changed internally to avoid conflicts with other libraries.

    === "Class Diagram"

        ``` mermaid
        classDiagram
        class Student{
            - _firstName : string
            - _lastName  : string
            - _studentNumber : string
        }
        Student : +get_firstName()
        Student : +set_firstName(value)
        Student : +get_lastName()
        Student : +set_lastName(value)
        Student : +get_studentNumber()
        Student : +set_studentNumber()
        ```

    === "Implementation"

        An example is; a school might have a rule that, once a student has been assigned a `StudentNumber`, it should never be changed.

        The `__init__()` method is called a _constructor_ which is used to set initial values when a new instance of an object is created. Since this example is making use of a student number, which would need to be connected to a student's first and last name, this data should be kept private in each instance of the `Student` class.

        To access data from outside the class, the _accessor_ (getter_) and _mutator_ (setter)methods will retrieve and modify data respectively.

        ```py
        classStudent:
            def __init__(self, newStudentNumber, newFirstName, newLastName):
                self._studentNumber = newStudentNumber
                self._firstName = newFirstName
                self._lastName = newLastName

            def get_studentNumber(self):
                return self._studentNumber

            def set_studentNumber(self):
                print("Student number cannot be changed")

            def get_firstName(self):
                return self._firstName

            def set_firstName(self, val):
                self._firstName = val

            def get_lastName(self):
                return self._lastName

            def set_lastName(self, val):
                self._lastName = val
        ```


### Abstraction

??? "An idea that the programmer does not need to have to know how a method does its job."
    
    === "Description"

        Suppose we wanted to find the area of a circle and a rectangle, each shape having a different formula, but each shape will both utilize a method called `Area()`

        We don't have to know how the `Area()` method works internally, we just need to know that if we use `Area()` on a new instance of a `Rectangle` and `Circle` object, we will get the area of the shape regardless of how they're calculated.

        If we create a program in Python to implement this problem, we could import Python's built-in abstract base class library or ABC.

    === "Class Diagram"

        ``` mermaid
        classDiagram
        Shape <|-- Rectangle
        Shape <|-- Circle
        Shape : +Area()

        class Rectangle{
            -_length : float
            -_width : float
            +get_length()
            +set_length()
            +get_width()
            +set_width()
            +Area()
        }

        class Circle{
            -_radius : float
            +get_radius()
            +set_radius()
            +Area() 
        }
        ```

    === "Implementation"

        ```py
        from abc import ABC, abstractmethod
        import math

        class Shape(ABC):
            @abstractmethod
            def Area(self, area):
                pass

        class Rectangle(Shape):
            def __init__(self, newLength, newWidth):
                self._length = newLength
                self._width = newWidth

            def get_length(self):
                return self._length

            def set_length(self, val):
                self._length = val

            def get_width(self):
                return self._width

            def set_width(self, val):
                self._width = val

            def Area(self):
                return self._length * self._width

        class Circle(Shape):
            def __init__(self, newRadius):
                self._radius = newRadius

            def get_radius(self):
                return self._radius

            def set_radius(self, val):
                self._radius = val

            def Area(self):
                return math.pi * math.pow(self._radius, 2)
        ```

### Inheritance

??? "Allows the reuse of code"
    
    === "Description"

        When you define a class that inherits from another class or the **base class**, it automatically inherits the properties and methods from the base class. You can also add additional properties or methods that are not part of the base class. 

        This example will be an `Employee` class with two types of employees, hourly and salary. The `Employee` class includes includes fields and properties that are common to all employees. 

        The `Hourly` and `Salary` classes inherit all the fields and properties from the `Employee` class but also adds `hourlyPay` and `annualPay` which is employee specific types. 

    === "Class Diagram"

        ``` mermaid
        classDiagram
        Employee <|-- EmployeeHourly
        Employee <|-- EmployeeSalary
        Employee : -int _employeeID
        Employee : -_employeeDOB
        Employee : -_employeeFirstName
        Employee : -_employeeLastName
        Employee : -_employeeType
        Employee : +get_employeeID()
        Employee : +set_employeeID()
        Employee : +get_employeeDOB()
        Employee : +set_employeeDOB()
        Employee : +get_employeeFirstName()
        Employee : +set_employeeFirstName()
        Employee : +get_employeeLastName()
        Employee : +set_employeeLastName()
        Employee : +get_employeeType()
        Employee : +set_employeeType()

        class EmployeeHourly{
            -_hourlyPay
            +get_hourlyPay()
            +set_hourlyPay()
        }

        class EmployeeSalary{
            -_annualPay
            +get_annualPay()
            +set_annualPay()
        }
        ```

    === "Implementation"

### Polymorphism

??? "The idea that methods may have to act differently on different types of objects or that they may have different numbers or types of parameters."

    === "Description"

        Literally means "many shapes". Polymorphism is not only fun to say, it's the idea that methods can have different implementations. If you go further up this page where I used the Shape abstract base class to get the area of a circle and rectangle. I could implement those Shape objects another way.

        Click the "Implementation" tab if you're interested.

    === "Implementation"

        ```py
        class Rectangle(Shape):
            def _init_(self, newlength, newWidth=None):
                if newWidth == None:
                    self._length = newlength
                    self._width = newlength
                else:
                    self._length = newlength
                    self._width= newWidth 

            def get_length(self):
                return self._length 

            def set_length(self, val):
                self._length = val 

            def get_width(self):
                return self._width

            def set_width(self, val):
                self._width= val

            def Area(self):
                return self._length * self._width
        ```

These concepts will be the foundation on which we'll explore other object-oriented types and topics. See you in the next one!