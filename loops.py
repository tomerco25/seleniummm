# "----------------------------------------------------------"
# # counter=0
# # for i in range(10):
# #     counter+=1
# #     print "the value of counter is:%s" %counter
# #     print "the value of i is:%s" %i
# "----------------------------------------------------------"
# # counter=0
# # for j in range(5,10):
# #     counter+=1
# #     print "the value of counter is:%s" %counter
# #     print "the value of j is:%s" %j
# "----------------------------------------------------------"
# # counter=0
# # for i in "aavvvdw":
# #    counter+=1
# #    print i
# #    print "-----"
# #    print counter
# "----------------------------------------------------------"
# # fruits = ['banana', 'apple',  'mango']
# # print range(len(fruits))
# # for index in range(len(fruits)):
# #    print 'Current fruit :', fruits[index]
# #    print index
# "----------------------------------------------------------"
# """reveese string"""
# str = ''
# for letter in "hello":
#     str = letter + str
# print str
# "----------------------------------------------------------"
# """find the second max"""
# tom=[3,5,18,1,9,10,7,2,15,6,2,7,22]
# max=0
# secondmax=0
# for i in range(len(tom)):
#     if tom[i]>max:
#         secondmax=max
#         max=tom[i]
#     elif tom[i] > secondmax:
#         secondmax = tom[i]
# print secondmax
# print max

"""find missing number in list"""
# a = [1,2,4,5,6,7,8,9,10,11]
# print sum(range(a[0],a[-1]+1))-sum(a)


"""Create a 2D array"""
#board=[[0]*8 for n in range(8)]
#OR:
#board2=[[0 for j in range(8)] for n in range(8)]

"""Queen game board"""
# board=[[0]*8 for n in range(8)] #[0]*8 - create this action for n in range(8) timer
# line=0
# row=0
# for i in board:
#     board[line][row]="Q"
#     row+=1
#     line+=1
# print board

"""Using Queue - first in first out"""
# q = Queue.Queue()    #or use q=Queue.LifoQueue() to First in Last out
# for i in range(5):   #Or use list instead int
#     q.put(i)
# while not q.empty():
#     print q.get()   #result 0 1 2 3 4