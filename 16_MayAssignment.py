# 1) create file only if it does not exists
#  otherwise append text to the file
# keep inputting text till the user types QUIT to stop

# then read the file - in the form of string
# find how many times (say) word success appears in the file
# display the FIRST and the LAST line from the file

# import os.path
# while True:
#     if os.path.exists('S:\Aroha_tech\python\dummy.txt'):
#         with open('dummy.txt','a+') as outfile:
#             while True:
#                 txt=input('enter a text :')
#                 if txt.upper()=='STOP':
#                     break
#                 else:
#                     outfile.write(txt+'\n')
#             outfile.seek(0)
#             data=outfile.read()
#             break
#     else:
#         f=open('dummy.txt','a')
#         f.close()
# num=data.count('success')
# print('The word "success" appears in the file :',num)
# with open('S:\Aroha_tech\python\dummy.txt','r') as file:
#     fst=file.readlines()
# print('''first line of the file is :
# ''',fst[0])
# print('''last line of the file is :
# ''',fst[-1])
# 2) input decimal numbers store in a file called data1.txt
# when the user types any NEGATIVE number - STOP

# read all the numbers from the file, store it in a set
# how many inputted numbers repeated? which were those?
# (hint use the concept of list and set properly)
# find the highest, lowest, avg of all the numbers
# how many numbers are not in the range 175 to 339?
# finally append the following data from the set to the data1.txt file
# s1 = {100.22,78.22,190.33,800.22}
# with open('data1.txt','a+') as outfile:
#     while True:
#         try:
#             num=float(input('enter a decimal number :'))
#             if num==-1:
#                 break
#             else:
#                 outfile.write(str(num)+',')
#         except  ValueError:
#             print('input only numbers')
#     outfile.seek(0)
#     data=outfile.read()
# lst=data.split(' ')
# lst.remove(lst[-1])
# setnum=set(lst)
# setnum={float(x) for x in setnum}
# s=len([x for x in setnum if x>=175 and x<339])
# print('highest number in the set is ',max(setnum))
# print('lowest number in the set is ',min(setnum))
# print('average number in the set is ',sum(setnum)/len(s1))
# print('numbers are not in the range 175 to 339 is',len(setnum)-s)
# with open('data1.txt','a+') as outfile:
#     outfile.write(str(s1))



# 3) given a list1 = ['hello1.txt','data1.txt','data2.txt']
# process the list - they are file name. try to read the contents of the file
# if those files exists.
# find out totally how many lines you read from all the 3 files.
# import os.path
# list1 = ['hello1.txt','data1.txt','data2.txt']
# rep=0
# for file in list1:
#     if os.path.exists(file):
#         try:
#             with open('S:\\Aroha_tech\\python\\'+file,'r') as outfile:
#                 lines=outfile.readlines()
#                 rep+=len(lines)
#         except FileNotFoundError :
#             pass
# print(rep)
import copy

a = [ [1, 2, 3], [4, 5, 6] ]
b = copy.copy(a)

c = [ [7, 8, 9], [10, 11, 12] ]
d = copy.deepcopy(c)

print(a)
print(b)

a[1][2] = 23
b[0][0] = 98

print(a)
print(b)

print("\n")

print(c)
print(d)

a[1][2] = 23
b[0][0] = 98

print(c)
print(d)
