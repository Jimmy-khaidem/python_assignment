#  input any 5 numbers and store in set
#    find the highest number
#    find the lowest number
#    find the avg of all the numbers
#    display the set in DESC order of numbers
class Fivenumbers:
    def __init__(self):
        self.numbers=set()
        i=0
        while i<5:
            try:
                self.num=int(input('enter a number: '))
                self.numbers.add(self.num)
                i=i+1
            except:
                print('input number only')
    def highest(self):
        print('highest number is ',max(self.numbers))
    def lowest(self):
        print('lowest number is ',min(self.numbers))
    def average(self):
        print('average of all number is ',sum(self.numbers)/5)
    def descending(self):
        lst=list(self.numbers)
        lst.sort(reverse=True)
        print('descending order of number is',lst)
# f=Fivenumbers()
# f.highest()
# f.lowest()
# f.average()
# f.descending()

#  once 1 is working
#    convert the set to the list - call it list1
#    given list2 = [89,23,67,22,100,105,15]
#    process the list2 and add it into the list1
#    in the last 5 elements find the highest
#    in the first 6 elements find the lowest
#    find the avg of all the list1 elements
#    how many numbers are above the avg ?
class Operation2(Fivenumbers):
    def __init__(self):
        super().__init__()
        list1=list(self.numbers)
        list2 = [89,23,67,22,100,105,15]
        self.list1=list1+list2
    def result(self):
        super().highest()
        super().lowest()
        super().average()
        super().descending()
        avg=sum(self.list1)/len(self.list1)
        a=sum(map(lambda x: x>avg,self.list1 ))
        print('the highest in the last 5 elements is ',max(self.list1[-5:]))
        print('the lowest in the last 6 elements is ',min(self.list1[0:7]))
        print('average in list1 is ',avg)
        print('numbers that are above the avg :',a)       
o=Operation2()
o.result()

# 3) st1 = {'Java','Python','C'}
#    st2 = {'SQL','Java','C#','Python'}
#    to the st1 add those elements from st2 which is not there in st1
#    remove the skill 'Java' from both st1, st2
#    add the skills st3 = {'SQLServer','ASP.net','AWS'}
#    into both st1 and st2 using for loop
#    display the st2 in DESC order of sorting
# st1 = {'Java','Python','C'}
# st2 = {'SQL','Java','C#','Python'}
# st3 = {'SQLServer','ASP.net','AWS'}
# skill='Java'
# st1.update(st2)
# st1.remove(skill)
# st2.remove(skill)
# st3=list(st3)
# print(st3)
# for i in st3:
#     st1.add(i)
#     st2.add(i)
# print('after adding st3 element to st1 and st2 :')
# print('st1: ',st1)
# print('st2: ',st2)
# st2=list(st2)
# st2.sort(reverse=True)
# print('displaying st2 in descending order ',st2)




