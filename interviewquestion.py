# 1	Write a logic to extract [1,3,5,7,9] from a given list a=[1,24,3,43,66,5,7,85,9]

# a=[1,24,3,43,66,5,7,85,9]
# a=list(filter(lambda x: x<10 and x>=0,a))
# print(a)
# 2	Write a program to convert a given list to string s=[‘Welcome’,2,’learn’,3,’python’]
# OUTPUT- “Welcome 2 learn 3 python
# s=['Welcome',2,'learn',3,'python']
# a=str()
# for i in s:
#     a+=str(i)+' '
# print(a)
# 3	Create a list , find the length of the list , and return value at the last position and max value of the list
# a=[1,24,3,43,66,5,7,85,9]
# print('length of the list ',len(a))
# print(a[-1])
# print(max(a))


# 4	Replace all ‘The’ with ‘An’ in any string.
# E:- “The day the Earth stood still will become An day an Earth stood still”

# e="THe day the Earth stood still will become An day an Earth stood still"
# b=e.split(' ')
# for i in b:
#     if i.upper()=='THE':
        
#         z=i.replace(i,'An')
#         print(i)
#         e=e.replace(i,z)
# print(e)


# 5	What will happen if you use a keyword /reserved word to store a variable


# write a program to Count no of english letters are used in given string

# st="the python program is better than any other programming language"
# count=0
# for i in st:
#     if i.upper()>=chr(65) and i.upper()<=chr(90):
#         print(i)
#         count+=1
# print(count)

# 6	Write the logic to get the required output base on the input 
# inpt= ['Hi']
# output=''
# a=int(input("number of repetition of 'Hi' :"))
# for i in range(a):
#     for j in inpt:
#         output+=str(j)+'!'
# print(output)

# OUTPUT= Hi!Hi!Hi!Hi!


# 7	Find the sum of the list  [6,5,3,8,4,2,5,4,11]
# lst = [6,5,3,8,4,2,5,4,11]
# print(sum(lst))


# 8	Find the occurrence of each character for a given string and store it in a dictionary 
# Ex: if string is “Hi”
#       Your keys should be H and I and its occurrence 


# 9	Extract the 1st , 2nd and 4th word of this string and concatenate it with spaces 
# “Hi welcome to world”
# str='Hi welcome to world'
# str=str.split(' ')
# newstr=''
# newstr+=str[0]+' '+str[1]+' '+str[3]
# print(newstr)


# 10	What is the difference between remove() function and del statement?

# 11	NewList =[1,0,1,1,0,0]
# Replace 1 by True and 0 by False using list comprehension
NewList =[1,0,1,1,0,0]
s=[True if x==1 else False for x in NewList]
print(s)


# 12	Pass an input as the students name and compare the value with key and if its present 
# display the marks of the student. If the name is not present add it to the end of the  dictionary
#  with a default value 0. marks={'James':90,'Jules':55,'Arthur':77}
studName=input('enter student name :')
marks={'James':90,'Jules':55,'Arthur':77}
if studName  in  marks.keys():
    for i,j in marks.items():
        if studName==i:
            print(j)
else:
    marks.update({studName:0})
            
print(marks)



# 13	Write a code to get the below pattern 
# a)	1
# 111
# 11111
# b)	1
# 12
# 123
# 1234
# 12345

for i in range(2):
    if i=

# 14	Write a function that takes a list of list s and flattens into a one-dimensional list.
# INPUT = [[1,2],[3,4]]
# OUTPUT = [1,2,3,4]
# 15	What is the Difference between "is" and '=='?
# 16	Check if a word is a anagram i.e if a word is written backwards it will read the same as forward
# 17	Check if a given input is present in a tuple without using loop
# 18	Print the first 10 fibonacci number 
# 19	The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has I twice in a row, while the string "nong" does not have two identical letters in a row. Define a function named double letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string. and False otherwise.
