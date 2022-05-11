# class Vowel:
#     def __init__(self,name):
#         self.name=name
#         self.vowel='AEIOU'
#         while True:
#             if len(self.name)>=8:
#                 if self.name[7].upper() in self.vowel:
#                     print('the 8th element of {} is vowel'.format(self.name))
#                     break
#                 else:
#                     print('the 8th element of {} is not vowel'.format(self.name))
#                     break
#             else:
#                 print('the length of the string is less than 8')
#                 self.name=input('enter again : ')
# name=input('Enter a name : ')
# v=Vowel(name)
# 2. enter a sentence
#    enter a word to search in it
#    does the word exists ?
#    if it does how many words are there?
#    which position is the first occurance of the word in the sentence?
# class Sentence:
#     def __init__(self,sen,wor):
#         self.sen=sen
#         self.wor=wor
#         self.count=0
#     def display(self):
#         if self.wor in self.sen:
#             self.a=self.sen.split()
#             self.numofwords=sum(map(lambda n: n==self.wor,self.a))
#             print(self.numofwords)
#             for i in self.a:
#                 if i==self.wor:
#                     break
#                 else:
#                     self.count+=1
#             print("the number of '{}' contain in the sentence is {} ".format(self.wor,self.numofwords))
#             print("the first occurence of '{}' in '{}' is {}".format(self.wor,self.sen,self.count))
#         else:
#             print("the word doesn't exist in the sentence")
# s=input('enter a sentence: ')
# w=input('enter a word: ')
# sentence=Sentence(s,w)
# sentence.display()

# 3. enter a name 
#    print the name in upper case, lower case  and title case
#    find out how many char are there?

# class Name:
#     def __init__(self,nme):
#         self.nme=nme
#         self.lst=list(self.nme)
#         print(self.lst)
#         self.chr=sum(map(lambda n: n!=' ',self.lst))
#         print('uppercase :',self.nme.upper())
#         print('lowercase :',self.nme.lower())
#         print('titlecase :',self.nme.title())
#         print('number of char in {} is {}'.format(self.nme,self.chr))
# n=input('enter a name: ')
# cs=Name(n)


# 4. input the mobile number (as string)
#    check whether the last digit of the mobile number is either 5 or 8
# class Mob:
#     def __init__(self,num):
#         self.num=num
#         if len(self.num)==10:
#             if self.num.endswith('5') or self.num.endswith('9'):
#                 print('yes, the mobile number last digit is either 5 or 9 ')
#             else:
#                 print('No, the mobile number last digit is neither 5 or 9')
#         else:
#             print('invalid mobile number')
# n=input('enter the mobile number: ')
# m=Mob(n)

# 5. given a string say
#    name1 ='Mohan,Ajay,harish,anand,veena,rashmi,Kiran'
#    word1 ='VEENA'
#    find this word1 in name1 irresprective of lower case/upper case
#    how will you solve it?
# class Str:
#     def __init__(self,name,word):
#         self.name=name
#         self.word=word
#         self.nm=self.name.split(',')
#     def display(self):
#         self.found=False
#         self.count=0
#         for i in self.nm:
#             if i.upper()==self.word.upper():
#                 self.found=True
#                 break
#             else:
#                 self.count+=1
#         if self.found==True:
#             print("the word '{}' is found at position {}".format(self.word,self.count))
#         else:
#             print("the word {} is not in '{}'".format(self.word,self.name))
# name1 ='Mohan,Ajay,harish,anand,veena,rashmi,Kiran'
# word1 ='VEENA'
# s=Str(name1,word1)
# s.display()


# 6. enter the day, month and year as numbers, one by one
#    dd = 9
#    mn = 12
#    yr = 2020
#    display it is valid date or not
#    valid date rule is 
#    day must be 1 to 31 for any month 1 to 12
#    day must be 1 to 30 if the month is 4,6,9,11
#    day must be 1 to 29 if the year is Leap and the month is 2
#    Leap year rule
#    if the year is not century year like 2004, 1984 , 1996 etc then
#    divide such year by 4, if it is divisible then it is Leap or not
#    leap
#    Non-leap year have 28 days
#    if the year is like 1700, 1800, 1900, 2000 - then they are century
#    year , such year divide by 400 and if it is divisible then it is 
#    leap century year such year will have 29 days in Feb
#    hence 29 2 1800 is invalid
#          29 2 1600 is valid
#          29 2 2000 is valid
#          29 2 1900 is invalid
# class Leapyr:
#     def __init__(self):
#         self.con=True
#         while self.con==True:
#             try:
#                 self.date=int(input('enter date : '))
#                 self.mon=int(input('enter month : '))
#                 self.yyyy=int(input('enter year : '))
#                 self.con=False
#             except:
#                 print('wrong format please write in integer format only')
#     def display(self):
#         if self.mon<13 and self.mon>0 and self.date<=31 and self.date>0 :
#             if (self.yyyy%4==0 and self.yyyy%100!=0) or (self.yyyy%400==0 and self.yyyy%100==0):
#                 if self.mon!=2 and  self.mon%2==0:
#                     if self.date<=31:
#                         print('{}/{}/{} is valid leap year date'.format(self.date,self.mon,self.yyyy))
#                 elif self.mon==2:
#                     if self.date<=29:
#                         print('{}/{}/{} is valid leap year date'.format(self.date,self.mon,self.yyyy))
#                 else:
#                      if self.date<=30:
#                             print('{}/{}/{} is valid leap year date'.format(self.date,self.mon,self.yyyy))
#             else:

#                 if  self.mon%2==0:
#                     if self.date<=31:
#                         print('{}/{}/{} is valid date'.format(self.date,self.mon,self.yyyy))
#                 else:
#                      if self.date<=30:
#                             print('{}/{}/{} is valid date'.format(self.date,self.mon,self.yyyy))
#         else:
#             print('please write in correct format')
   
# a=Leapyr()
# a.display()


# 7. given
#    price of LPG for domestic is 950 rs
#    price of LPG for commercail is 1450 rs
#    domestic LPG the user cannot take more than 2 qty
#    commercial LPG the user cannot take more than 6 qty
#    input the category (commercial OR domestic)
#    input the qty (apply the rules) 
#    display the bill amount
#    give discount of 5% is the LPG qty is more than 3 in case of commercial 
#    category

# class Lpg:
#     domestic=950
#     commercial=1450
#     def __init__(self):
#         self.con=True
#         while self.con:
#             try:
#                 self.cat=input('''choose the category:-  A)DOMESTIC B)COMMERCIAL
#                         :''')
#                 self.qnty=int(input('''enter the quantity: '''))
#                 if self.cat.upper()=='DOMESTIC' or self.cat.upper()=='A':
#                     if self.qnty>0:
#                         if self.qnty<=2:
#                             print('bill generating............. ')
#                             self.con=False
#                         else:
#                             print('domestic LPG can have only upto 2 quantity ')
#                     else:
#                         print('not a valid quantity')
#                 elif self.cat.upper()=='COMMERCIAL' or self.cat.upper()=='B':
#                     if self.qnty>0:
#                         if self.qnty<=6:
#                             print('bill generating............. ')
#                             self.con=False
#                         else:
#                             print('commercial LPG can have only upto 6 quantity ')
#                     else:
#                         print('not a valid quantity')
#                 else:
#                     print('please choose the mentioned category')
#             except:
#                 print('your item cannot proceed, please enter it correctly')
#     def display(self):
#         if self.cat.upper()=='DOMESTIC' or self.cat.upper()=='A':
#             print('bill amount is  Rs',Lpg.domestic*self.qnty)
#         elif self.cat.upper()=='COMMERCIAL' or self.cat.upper()=='B':
#             if self.qnty>3:
#                 print('bill amount is  Rs',(Lpg.commercial-(Lpg.commercial*5/100))*self.qnty)
#             else:
#                 print('bill amount is  Rs',Lpg.commercial*self.qnty)
# a=Lpg()                        
# a.display()

# 8. input a number and display one of the following
#    it is a SINGLE digit number ::: if it is 1 to 9
#    it is DOUBLE digit number ::: if it is 10 to 99
#    and so on...
#    do it till SIX digit number
#    if number is above SIX digits then display this number is LARGE number
#    NOTE
#    if the user inputs a NEGATIVE number then - donot do the above processing
#    instead display :: cannot process NEGATIVE numbers



# class Numb:
#     def __init__(self):
#         while True:
#             try:
#                 self.a=int(input('input a number: '))
#                 self.b=str(self.a)
#                 if self.a<0:
#                     print('cannot process NEGATIVE numbers')
#                 else:
#                     break
#             except:
#                 print('error input')
#     def display(self):
#             lst=['single','double','three','four','five','six']
#             count=1
#             if len(self.b)>6:
#                 print('this number is LARGE number')
#             else:
#                 for i in lst:
#                     if len(self.b)!=count:
#                         count+=1
#                     else:
#                         print('it is {} digit number'.format(i))
#                         break
# a=Numb()
# a.display()






        

        


