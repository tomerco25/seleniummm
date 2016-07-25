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
 """reverse list from string"""
# str1="hello"
# strtolist=list(str1)
# strtolist.reverse()
# jointostr=''.join(strtolist)
# print jointostr
"""reverse list without reverse"""
# list=[5,2,7,4,1,8,7,22,55,6,11,44,865]
# for i in range(0,len(list)/2):
#     firstvar=list[i]
#     lastvar=list[len(list)-(i+1)]
#     list[list.index(lastvar)]=firstvar
#     list[list.index(firstvar)]=lastvar
# print list

"""return index of item in list"""
# fruits = ['banana', 'apple',  'mango']
# for i in fruits:
#    print fruits.index(i)
"""return index of item in dic"""
# dic = {"banana":"yellow","apple":"red","mango":"orange"}
# print dic
# print dic.values()
# print dic.keys()
"""add char to list"""
# liststr = ("a", "b", "c")
# print ''.join(liststr) #result abc
# print '--'.join(liststr) #result a--b--c
# print "--".join(liststr[0:2]) #result a--b
"""Keep dictionary order"""
"""before create dictionarty put lines:"""
# import collections
# tom = collections.OrderedDict()
"""To USE dictionarty order:"""
# tom={} NO!! tom={"dsad":"dasdsa","aaaa":"bbb"}
# tom["z55zz"]="zzz"
# tom["vvv"]="bbb"
# tom["aaa"]="zzz"
# tom["ccc"]="zzz"
# result of print tom -- OrderedDict([('z55zz', 'zzz'), ('vvv', 'bbb'), ('aaa', 'zzz'), ('ccc', 'zzz')])
# result of  print d.items() -- [('z55zz', 'zzz'), ('vvv', 'bbb'), ('aaa', 'zzz'), ('ccc', 'zzz')]
# to separate -- for i,u in d.items():print i,u