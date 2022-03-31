# data=[1,2,3,4,5,6,7,1,2,3,4]
# sdata=list(set(data))
# count=0
# for i in sdata:
#     for j in data:
#         if i==j:
#             count=count+1
#     print(i,count)
#     count=0


    
# data2=[('sunil',888),('Dev',876),('Anil',25)]
# sal=dict(data2)
# print(sal)
# print(type(sal))
# n=None
# h=0
# l=999999999999
# for i in data2:
#     if i[1]>h:
#         h=i[1]
#         n=i[0]
# dc=dict()
# a=[10,20,30,40]
# b=['A','B','C','D']
# dc=dict(zip(a,b))
# for k,v in dc.items():
#     print(k,v)
# correct_orders = { 'O100' : 36002, 'O900':35000 , 'O120' : 3300,\
#                   'O200' : 25600, 'O300' : 36011,\
#                 'O111' : 36009, 'O170' : 26000}
# high = 0 
# ord_no = 0 
# for k,v in correct_orders.items():
#     print (k,' ',v)
#     if v > high:
#         high = v
#         ord_no = k
# print ('order with highest value is ',high,' order no. is ',ord_no)        

# lst_keys = list(correct_orders.keys())      
# lst_values = list(correct_orders.values()) 
# print (lst_keys)
# print (lst_values)
# h  = max(lst_values)
# print ('h is ',h) 
# pos = lst_values.index(h)
# print ('position ',pos) 
# print ('VIA LIST order with highest value is ',h,' order no. is ',lst_keys[pos])    
# print()
# high = max(lst_values) 
# list_of_high_values=[]  
# for k,v in correct_orders.items():
#     print (k,' ',v)
#     if v == high:        
#         ord_no = k
#         list_of_high_values.append((ord_no,high))
# print ('high value listing ....')
# for i in list_of_high_values:
#     print (i[0],' ',i[1])


# try:
#     a=int(input('enter a number:'))
#     b=int(input('ente another number:'))
#     print(a+b)
#     print(a/b)
# except ValueError:
#     print('invalid input')
# except ZeroDivisionError:
#     print('cannot divide by zero')


# from functools import reduce


# num=[1,2,3,4,5,6]

# even=list(filter(lambda n:n%2==0,num))
# doub=list(map(lambda n:n+n,even))
# sum=reduce(lambda a,b:a+b,doub)
# print(even)
# print(doub)
# print(sum)

# data2={1000:(12,45,66),2500:(45,78,99),3000:(12,42,66)}
# print(type(data2))
# total=c=0 
# lst=[]
# for k,v in data2.items():
#     total=sum(v)
#     c=c+len(v)
#     for j in v:
#         lst.append(j)
# lst.sort()


# l=[1,2,3,4,5]
# k=['a','b']
# emp={}
# for i in range(0,len(l)):
#     try:
#         emp.update({l[i]:k[i]})
#     except:
#         emp.update({l[i]:None})

# print(emp)



    