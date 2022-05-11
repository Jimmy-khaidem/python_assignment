# def name(a):
#     b=a.split()
#     c=''
#     if len(b)==1:
#         return a
#     else:
#         for i in b:
#             c+=i[0]
#     return c
# n=input('enter a string: ')
# res=name(n)
# print(res)


class Exam:
    def input_data(self):
        self.dict={}
        x=True
        while x:
            self.roll=int(input('enter roll number: '))
            self.name=input('enter the Name: ')
            self.average=float(input('enter the average'))
            self.dict.update({self.roll:(self.name,self.average)})
            self.con=input('Exit Y/N: ')
            if self.con=='Y':
                x=False
    def process_avg(self):
        self.total=0
        self.high=0
        self.secondhigh=0
        for i,j in self.dict.items():
            self.total+=j[1]     
            if self.high>j[1]:
                self.secondhigh=j[1]
            else:
                self.secondhigh=self.high
                self.high=j[1] 
        self.avg=self.total/len(self.dict)
    def display_all_details(self):
        self.count=0
        for i,k in self.dict.items():
            if k[1]<40:
                print(k[0],'- fail')
            elif k[1]<=49 and k[1]>=40:
                print(k[0],'- pass')
            elif k[1]<=59 and k[1]>=50:
                print(k[0],'- Second Class')
            elif k[1]<=74 and k[1]>=60:
                print(k[0],'- First Class')
            elif k[1]<=89 and k[1]>=75:
                print(k[0],'- distinction')
            elif k[1]>=90:
                print(k[0],'- high Distinction')
            if k[1]>self.avg:
                self.count+=1
        print("Number of candidates who secures more than classavg. is ",self.count)
        print('the student details who has highest avg is ',self.high, 'and second highestavg is ',self.secondhigh)

            
#  1-39 - Fail
#    40-49 - Pass
#    50-59 - Second class
#    60-74- First class
#    75-89 - distinction
#    90 and above - High Distinction


    # def display_all_details()
a=Exam()
a.input_data()
a.process_avg()
a.display_all_details()


        
            
