# 1. enter the inital meter reading 
#    enter the final meter reading
#    enter D for Domestic or C for commercial
#    ask whether the bill payment is done after the due
#    date ? if yes then Fine is applied else no fine
#    calc
#    for the domestic category - ask whether Solar pannels are there
#    for water heating - if yes then give a discount in the bill of 2%
#    otherwise no discount.

#    Domestic category
#         units
#        1 to 1000     1.90/unit
#      1001 to 2500    2.85/unit
#      2501 ...        4.10/unit
#     fine 5% of the bill amt
 
#     commercial category      
#      1 to 2000       2.25/unit
#     2001 to 5000     3.75/unit
#     5001 to 8000     4.90/unit
#     8001 ...         6.15/unit
#     fine is 10% of the bill amt
class meterReading:
    def __init__(self):
        self.con=True
        while self.con:
            try:
                self.initial=float(input('enter the initial meter reading: '))
                self.final=float(input('enter the final meter reading: '))
                if self.initial>0 and self.final>0 and self.final>self.initial:
                    self.con=False
                else:
                    print('invalid meter')
            except ValueError:
                print('input numbers only')
    def category(self):
        while True:
            self.cat=input('choose the category   enter D for Domestic or C for commercial: ')
            if self.cat.upper()=='D' or self.cat.upper()=='C':
                break
            else:
                print('please input the mentioned category that is "D" or "C"') 
        while True:
            self.due_date=input('Is the bill payment done after the due_date? YES/NO : ')  
            if self.due_date.upper()=='YES' or self.due_date.upper()=='NO':
                print('fine applied.....')
                break
            else:
                print('please answer "YES" or "NO"')   
    def calc(self):
        self.price=0
        self.totmeter=self.final-self.initial
        if self.cat.upper()=='D':
            if self.totmeter>=1 and self.totmeter<=1000:
                self.price=self.totmeter*1.90
            elif self.totmeter>=1001 and self.totmeter<=2500:
                self.price=self.totmeter*2.85
            else:
                self.price=self.totmeter*4.10
            while True:
                    self.solarpannel=input('Are Solar pannels there for water heating? YES/NO : ')
                    if self.solarpannel.upper()=='YES' or self.solarpannel.upper()=='NO':
                        break
                    else:
                        print('choose yes or no')
        else:
            if self.totmeter>=1 and self.totmeter<=2000:
                self.price=self.totmeter*2.25
            elif self.totmeter>=2001 and self.totmeter<=5000:
                self.price=self.totmeter*3.75
            elif self.totmeter>=5001 and self.totmeter<=8000:
                self.price=self.totmeter*4.10
            else:
                self.price=self.totmeter*4.10
    def display(self):
        if self.due_date.upper()=='YES':
            if self.cat.upper()=='D':
                if self.solarpannel.upper()=='YES':
                    self.discountprice=self.price-(self.price*2/100)
                    print('electric bill for domestic category after discount with fine is',self.discountprice+(self.discountprice*5/100))
                else:
                    print('electric bill for domestic with fine is ',self.price+(self.price*5/100))
            else:
                print('electric bill for commercial category with fine is',self.price+(self.price*10/100))
        else:
            if self.cat.upper()=='D':
                if self.solarpannel.upper()=='YES':
                    self.discountprice=self.price-(self.price*2/100)
                    print('electric bill for domestic category after discount is',self.discountprice)
                else:
                    print('electric bill for domestic category is ',self.price)     
            else:
                print('electric bill for commercial category is',self.price)
a=meterReading()
a.category()
a.calc()
a.display()


# 2. Display all the numbers in the range say 345 to 590
#    (range could be anything ...)
#    Find out how many numbers are not divisible by 7
#    how many prime numbers are there in that range
#    how many numbers are divisible by BOTH 3 as well as 4
#    add the FIRST and the LAST number of the range and print the sum

# class Numberofrange:
#     def __init__(self):
#             try:
#                 con=True
#                 while con==True:
#                     self.start=int(input('input the starting of the range: '))
#                     self.end=int(input('input the ending of the range: '))
#                     con=False
#             except ValueError:
#                 print('input only integer number character or float not allowed')
#             if self.start>self.end:
#                 self.swap=self.start
#                 self.start=self.end
#                 self.end=self.swap
                
#     def div7(self):
#         self.count7=sum(map(lambda x : x%7!=0,range(self.start,self.end)))
#         print('{} numbers are not divisible by 7'.format(self.count7))
#     def isprime(self):
#         primecount=0
#         for i in range(self.start,self.end):
#             con=False
#             if i>1:
#                 for j in range(2,i):
#                     if i%j==0:
#                         con=True
#                         break
#                 if con==False:
#                         primecount+=1
#         print('the number of prime number in the range is',primecount)
#     def div3and4(self):
#         self.countdiv3and4=sum(map(lambda x : x%3==0 and x%4==0,range(self.start,self.end)))
#         print('{} numbers are divisible by 3 and 4 in given range'.format(self.countdiv3and4))
#     def sum(self):
#         print('the sum of first and last number the range is',self.start+self.end)
# n=Numberofrange()
# n.div7()
# n.isprime()
# n.div3and4()
# n.sum()

# 3. given a list
#    data_1 = [12,-13,-99,155,788,-199,455,-14,23,89,
#               100,49,80,221,-444,120,-333]

#    process the list (use the data_1)
#       add all the 3 digits non-negative numbers
#       find the avg of those numbers
#       how many two digits NEGATIVE numbers are there
#       remove the numbers stored in two variables a=-14 , b=221
#       add the FIRST and the LAST numbers in the list and display the sum
#       convert the list to tuple , iterate and display
#       convert the tuple to the set, iterate and display

# class Process:
#     def calulate(self):
#         a=-14
#         b=221
#         avg=0
#         sum=0
#         neg2digit=0
#         data_1 = [12,-13,-99,155,788,-199,455,-14,23,89,100,49,80,221,-444,120,-333]
#         for i in data_1:
#             if len(str(i))==3 and i>0:
#                 avg+=1
#                 sum=sum+i
#             elif i<0 and i>-100 :
#                 print(i)
#                 neg2digit+=1
#         data2=list(filter(lambda n:n!=a and n!=b,data_1))
#         sumoffirstandlast=data2[0]+data2[-1]
#         tupledata=tuple(data2)
#         tp=tuple(map(lambda x:x,tupledata))
#         setdata=set(data2)
#         sd=set(map(lambda x:x,setdata))
#         print('sum of all the 3digit negative number is ',sum)
#         print('average of 3digit negative number is ',sum/avg)
#         print('number of two digits negative number are ',neg2digit)
#         print('addition of the FIRST and the LAST numbers in the list is ',sumoffirstandlast)
#         print('iterating after converting to tuple:-',tp)
#         print('iterating after converting to set:-',sd)
# p=Process()
# p.calulate()