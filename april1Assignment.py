class Item:
    def __init__(self):
        x=True
        itemid=input('enter the item id: ')
        name=input('enter the name: ')
        try:
            costprice=float((input('enter the costprice: ')))
        except:
            print('wrong input')
            x=False
        if x==True:
            category=(input('''choose the category:
            1)A    2)B
            : '''))
            if category=='A':
                    profit=8.5
                    sp=costprice+(costprice*profit)
            elif category=='B':
                    profit=12.5
                    sp=costprice+(costprice*profit)
            elif category!='A' or category!='B':
                    print('wrong category and it is case sensitive')
                    x=False
        if x==True:           
            print('item id is : ',itemid)
            print('item name is : ',name)
            print('item costprice is : ',costprice)
            print('item category is : ',category)
            print('item selling price is : ',sp)
        
a=Item()    

###############################################################################
class Prime:
    def __init__(self,num):
        Prime.x=0
        self.num=num
        
    def display(self):
        if self.num>1:
            for i in range(2,self.num):
                if self.num%i==0:
                    Prime.x=Prime.x+1
            if Prime.x>0:
                print(self.num,' is not a prime number')
            else:
                print(self.num,' is a prime number')
        else:
            print(self.num,' is not a prime number')
a=Prime(101)
a.display()

# #################################################################################
class Pattern:
    def __init__(self,chr,num):
        self.chr=chr
        self.num=num
    def display(self):
        print(self.chr*self.num)
p1=Pattern('*',15)
p1.display()
                

###################################################################################
class Leap:
    def __init__ (self,year):
        self.year=year
    def display(self):
        if (self.year%4==0 and self.year%100!=0) or (self.year%400==0 and self.year%100==0):
            print('it is leap year')
        else:
            print('it is not leap year')
a1=Leap(1999)
a1.display()