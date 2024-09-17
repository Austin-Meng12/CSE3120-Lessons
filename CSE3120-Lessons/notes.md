# CSE3120 Object Oriented Programming 1

## Definitions

__Object-oriented Analysis (ODA)__ is the process of looking at a problem, system, or task and and idenitifying the objects and interactions between those objects. It answers the question, _what needs to be done_?
    * Often, then process identifies properties and actions for the problem/system/tasks.
    * Example: what makes a chair, a chair?
    * Examples: Does a table fall under your definition of a chair? How would you change your definition of a chair?

__Object-Oriented Design (OOO)__ is the process of converting the identifies objects and iteractions from OOA into object behaviours. It answers the question, _how things interact_?

__Object-oriented Programming (OOP)__ is the process of implementing the outcome of OOD into a function program.
    * OOP is the most common form of programming framework.
    * Structures the program around _how data is managed_ instead of how the program manages data.


A __Class__ is a model of an object. Classes contain __attributes__ and _behaviours_, which are inherited by objects instantiated from the class.
Another definition of a class is a blueprint or a template. 
* An _Attribute_ is a property of characteristic an object possesses. Each object can have different values for the attributes, but all objects instantiated from the class 
    inherits the attributes. Other names for attributes include _memebers_ and _properties_. 
* A _Behaviour_ is an action that can be performed on an object. Behaviours are formally named _Methods_ and are written the same as a function. Therefore, methods can also accept parameters and return values. 
* One major advantage to methods is they automatically have acess to all atrributes within the object. Therefore, object only have to pass arguments for data outside of the object. 
* Methods always have at least one argument, '''self''', which indicates that the function refers to the current object.
  * __Contructors__ are methods that provide the object with the default set of attributes. In python, it is  '''self.\_\_int\_\_()'''. Contructors create the object from the class template with the values within the attributes. Other attributes can be the defaults of the class. 
  * In general, all attributes of the object should be present in the Constructor, even if the default value is None.

```python
class Die:
    
    
        def __init__(self, maxValue):  # constructor
            self.maxVal = maxValue  # argument passed from the constructor
            self.mass = 0.01 # default value



    if __name__ == "__main__":
        Die = Die(6)    # constructs the Die object
```


An __Object__ is a unique set of data and functions instantiated from a class. An object accesses attributes and method using _dot notation_. 
Which identifies the object, then the attribute or value.

```python
<object>.<attriubte> = VALUE
<object>.<method>(PARAMETERS) // date the PARAMETER data into the object 
VARIABLES = <object>.<method>() // object returns the data to the rest of the program.
```

A __God object__ or __system object__ is an object that connects or has many methods that connect to other objects. System objects are indications that the developer is programming procedurally in an object-oriented environment. Thus, the advantages of OOP is lose when there is only one main system object.
    * This problem is often found when learning to program in java.

    

# Unified Modeling Language

A standardized modeling language unifying notational systems and approaches to data management and software design. This language is programming language agnostic and does not require programming background to utilize. It is composed of three main diagram types, structure, behaviour, interactions.

NOTE: While software developers require knowledge of all three diagrams, this unit will only focus on strucuture

A class diagram is a common strucutre diagram. It contains the name of the class, the attributes and methods of the class

|Bank Account | |
| --- | --- | 
| _attribute_| _Data Type_ |
| AccountNo | int | 
| AccountType | obkect |
| Balance | float | 
| ClientID | object | 
| TransactionHistory | object |
| _Methods(parameters)_ | _return_ |
| chargeTransaction(float) | None |
| depositFunds(float) |  None |
| withdrawFunds(float) | float | 


# Why OOP?

1. __Encapsulation__ is the process of protecting or hiding data through the implementation of an _interface_  for the data. The interface is often a collection of methods, such as setter (mutator) and getter (accessor) methods, that other objects can interact with
   1. A television encapsulates all the circuitry and hardware in a small plastic box so that the user cannot accidentally damage the TV. Then the user uses an interface, which is the remote control, while provides specific functions for the TV.
   2. For objects, setter and getter methods are the interface for how the program interacts with the attributes inside of the object.
   ```python
     class Person:
        def __init__(self):
            self.NAME = NAME # unprotected
   
     ME = person("Mr.Zhang")
     print(ME.NAME)  # Mr.Zhang - > Accessing an unprotected attribute
   
   
   class Person2:
        def __init__(self,NAME):
            self.__NAME = NAME # protect
        def getName(self):
            return self.__NAME
   
   ME2 = Person2("Mr.Zhang")
   print(ME2.__NAME)  # error -- > the print cannot access the attribute
   print(ME2.getName()) # MR.Zhang -- > getName() is the interface for self.__NAME.

   ```
    in python, anattribute is protected, when the attribute begins with _two underscores_

2. __Abstraction__ is the process of setting the level of detail and complexity to what is appropriate for the given task. 
   1. A driver only needs to interact with the steering, accelerator, and breaks of a car to drive. but a mechanic has much more complex understanding of the car to interact with it for maintenance and repair. Therefore, the mechanic and the driver's abstraction of the car is different. 
3. __Aggregation__ is the process of grouping objects together. Objects exist _independently_ of each other. All compositions are aggregates, but not all aggregates are compositions.
4. __Composition__ is the process of creating a complex object by collecting several objects together.
    1. A car is composed of an engine, transmission,starter, headlights, windshields, etc. Each of the car's objects have attributes and behaviours that are critical for the functioning of the car on a road. Without a critical object, the car will not run safely or legally. 
   




