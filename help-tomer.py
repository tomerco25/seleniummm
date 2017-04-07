""

"""
if __name__ == '__main__':
---------------------------
--what is below if __name__ == '__main__': will always run if the file is the main running.
--if we import file(1.py) that include if __name... to another file(in 2.py we do:import 1.py) and run 2.py as main,
only the lines on the file 1.py that not below if __name__ == '__main__': will run.
-- before using the class we MUST apply the class to var example test=class1()
-- self- need to be in every function in class,self is descirce the varibale outside the class.
-- def __init__(self) -constructor - will always run the lines in this function when call the class AND calling the class+func
-- def __call__(self) - will run the lines below this function when only call the class versus calling the class+func
-- def __str__(self): return print "something" -- will always print "something" when calling only the print + class without () example: print classname
--python to exe -> CMD-->pyinstaller --onefile pyfilelocation Example: pyinstaller --onefile C:\test1.py

--import pdb  # debbuging functions add line  pdb.set_trace()  before debug

-- ADD var to line "+VAR+"
--ADD var to print "hello %s" %var   OR "hello {}".format(var)
--__init__.py  - It is used to import a module(py file) in a directory,using import.
we put __init__.py in each directorie so that we can import the py file.
--change int to string - str(x) OR `x`   NO ''
-- lambda - use like fuction -->
lamb = lambda x: x ** 3
print(lamb(5)) -->result 125(5*5*5)
--*args - use on fuction when we don't know how much var will func receive --> def tom(*args):
-- copy class to other class(parent to child) - just put on child class the name of parent class a(): ** class b(a):
--When calling module to class we need to add in class "module.__init__(self)"
  EXAmple: class test(threading.Thread)
             threading.Thread.__init__(self)

--with - we will use with to open and close operations like(file open,lock)(instead of using file open&close)
--threading - each time we want to use 1 theard to do opeartion we need to use acquire&release
--Ride-selenium GUI(Google selenium2library keywords) -open by cmd- "cd C:\Python27\Scripts" -->python ride.py

"""