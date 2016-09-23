from openpyxl import load_workbook
import threading
import time
count = '1'
wb = load_workbook(filename='C:/1/units.xlsx')
sheet_ranges = wb['Sheet1']
tlock=threading.Lock()
def printexcel():
    global count
    tlock.acquire() #also we can use "with tlock:" instead acquire&release(see below)
    print "------Starting {}------".format(threading.current_thread().name)
    tlock.release()
    while (sheet_ranges['A'+str(count)+''].value != None):
        with tlock:
            count=str(count)
            unitid=sheet_ranges['A'+count+''].value
            if unitid!=None:
                print (threading.current_thread().name),"UnitId is:{}".format(unitid)
                count = int(count) + 1
for i in range(10):
    t=threading.Thread(target=printexcel)
    t.start()



