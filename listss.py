# # # list1 = ['physics', 'chemistry', 1997, 2000]
# # # list2 = [1, 2, 3, 4, 5, 6, 7 ]
# # list3 = [1, 8,'v', 5, 2,'f', 9,'a',8]
# #
# # def printlist(list3):
# #     # print list1[0]
# #     # print list2[1:5]
# #     print  "original %s " %list3
# #     list3.remove('f')
# #     print  "remove value f %s" %list3
# #     list3.reverse()
# #     print  "reverse %s " %list3
# #     list3.sort(reverse=True)
# #     print  "reverse and sort %s " %list3
# #     list3.append('vvvvvv')
# #     print  "append vvvvvv %s" %list3
# #     del list3[0]
# #     print  "del var location 0%s" %list3
# #     print "count v = %s" %list3.count('v')
# # printlist(list3)
# # print "----------------------------------------------"
list3=raw_input('please enter list of values:')
list3=list3.split()
print list3
print list(list3)
#
# tomdic={'age':4,'name':'tomer','money':4444}
# print tomdic['age']
# print tomdic.get('money',2)
# print tomdic.values()
#
# # string_input = raw_input()
# # input_list = string_input.split() #splits the input string on spaces
# # print input_list
# # process string elements in the list and make them integers
#
# """ reverse list"""
#
# str1="hello"
# strtolist=list(str1)
# strtolist.reverse()
# jointostr=''.join(strtolist)
# print jointostr