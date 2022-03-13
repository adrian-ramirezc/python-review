# Quick review of Python
- Data types (everything is an object)
- Cast (int(var), float(var), str(var))
- String methods (.upper(), .count(), +, .capitalize())
- Conditions (==, !=, <, >, ...)
- If statement -> if, elif, else
- List : mutable, ordered, have methods, idx
- Tuples: inmutable, CANT append remove change elements, ordered
- For loops: for i in range(5): for_function()
- While loops: while(condition): while_function()
- Slice operator: x[:-4:-1]
- Sets: unordered, unique collection of elements
- Dictionary: {'key' : value}
- Comprehensions: [i for i in range(5)]
- Functinons: def my_func(args): x = 4 return x
- *args : LIST - unpack collections
- **kwargs: DICTIONARY - unpack collections
- raise Exceptions
- Handle Exceptions
- lambda: one line anonymous function
- map: using lambda
- filter: using lambda
- F strings: f'Hello World {var}'
- Zip function: zip(list1, list2, list3) - use in loops
- Generators: fucntions that returns iterators -> def mygen(): yield 10; yield 20; yield 40 / print(next(gen))

# Python Object Oriented Programming (POOP)
- Class definition 
- Inheritance (i.e 2 parent classes)
- __init__()
- __super__()
- Class attributes
- Class methods
- Static methods

# Decorators
Allows to add extra functionalities to pre-existing functions

# Basic utility of "argparse" library from pythonn
Basically this library allows the user to execute a 'customized' python code from a terminal.
Users can insert 'arguments' that will be used during the execution of the code.
This allows to have different outputs depending on the input arguments. 

# With statement
Simplify resource management patterns (system resouces: files, locks, networks connections)

# Basic application of 'with' and 'open' statements
With allows to write cleaner and easier to mantain code.

