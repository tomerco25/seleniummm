""

"""
if __name__ == '__main__':
---------------------------
--what is below if __name__ == '__main__': will always run if the file is the main running.
--if we import file(1.py) that include if __name... to another file(2.py) and run 2.py as main,only the lines
that not below if __name__ == '__main__': will run.
-- before using the class we MUST apply the class to var example test=class1()
-- self- need to be in every function in class,self is descirce the varibale outside the class.
-- def __init__(self) -constructor - will always run the lines in this function when call the class AND calling the class+func
-- def __call__(self) - will run the lines below this function when only call the class versus calling the class+func
-- def __str__(self): return print "something" -- will always print "something" when calling only the print + class without ()
-- copy class to other class(parent to child) - just put on child class the name of parent class a(): ** class b(a):
--python to exe -> CMD-->pyinstaller --onefile pyfilelocation Example: pyinstaller --onefile C:\test1.py

--import pdb  # debbuging functions add line  pdb.set_trace()  before debug

-- ADD var to line "+VAR+"
"""