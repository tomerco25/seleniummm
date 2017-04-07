from sys import path
import threading
from os import getcwd
import tests
from tests import *
from excel_conf import *
import os

path.append(getcwd() + "\\tests")

def runbyfile():
    for i in  activetests():
        runtest=i
        os.popen('python "+runtest+".py')
        testpath=(getcwd() + "\\tests\\"+runtest+"")
        execfile(testpath) #runs python c:\test5.py

def runbyname():
    for i in activetests():
        runtest = i[:-3]
        a = getattr(eval(runtest),runtest) #runs test5.test5()
        a()
def worker(num):
    runtest = i[:-3]
    a = getattr(eval(runtest), runtest)  # runs test5.test5()
    a()
    for j in range(10000):print"thread"

if __name__ == '__main__':
    runbyfile()
    print "-----------------"
    runbyname()
# for i in activetests():
#     t = threading.Thread(target=worker, args=(i,))
#     t.start()