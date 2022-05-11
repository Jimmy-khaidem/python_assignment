
# 2. a=[1,24,3,43,66,5]
#    how to get [1,3,5] only as a list

# a=[1,3,43,66,5]
# a=list(filter(lambda x: x<10 and x>=0,a))
# print(a)

# from functools import reduce 
# 7. e=[[9,4],[3,5]] how to print e as [9,4,3,5]
# e=[[9,4],[3,5]]
# e=list(reduce(lambda a,b: a+b,e))
# print(e)

# 9. write a programe to allow only if the str contains continues same letter. like apple contains two p
#    continuesly
flag=True
while flag==True:
    strng=input('enter a string : ')
    for i in range(0,len(strng)-1):
        if strng[i]==strng[i+1]:
            flag=False
    if flag==False:
        print('string is allowed')
    else:
        print('string is not allowed')
        