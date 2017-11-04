from multiprocessing import Pool
import time

def process_line(line):
    print line
    print "######"
    time.sleep(3)

pool = Pool(4) #using 4 procceses
list_or_file="file"
if list_or_file=="list":
    # for multi proccesing file:
    with open('/root/2.txt', 'r+') as source_file:
        results = pool.map(process_line, source_file, 20)
else:
#for multi proccesing list:
    multilist=[]
    for i in range(10000):
        multilist.append(i)
    pool.map(process_line, multilist,20) # chunk/split the work into batches of 20 lines at a time

