from sys import path
from os import getcwd
path.append(getcwd() + "\\tests")
import tests
from tests import *

from excel_conf import *
import os
    # runsel=runselenuim(wallaurl,passurl)
    # tom="usepass"
    # a=getattr(runsel,tom)
    # a()

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

if __name__ == '__main__':
    runbyfile()
    print "-----------------"
    runbyname()