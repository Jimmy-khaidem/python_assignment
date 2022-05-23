class Table:
    def __init__(self):
        while True:
            try:
                self.num=int(input('enter any two digit number :'))
                if len(str(self.num))==2:
                    self.twonum=list(str(self.num))
                    break
                else:
                    print('enter only two digit number')
            except:
                print('enter digit only')
    def display(self):
        mulnum1=[]
        mulnum2=[]
        for i in range(1,11):
            a='0'+str(int(self.twonum[0])* i)
            b='0'+str(int(self.twonum[1])* i)
            if len(a)==2:
                mulnum1.append(a)
            else:
                mulnum1.append(str(int(self.twonum[0])* i))
            if len(b)==2:
                mulnum2.append(b)
            else:
                mulnum2.append(str(int(self.twonum[1])* i))
        for j in range(10):
            print(mulnum1[j],'  ',mulnum2[j],'  ',mulnum1[j],'+',mulnum2[j][0],'   ',str(int(mulnum1[j])+int(mulnum2[j][0]))+mulnum2[j][1])
t=Table()                
t.display()

# 1. create a file say file1.txt - in notepad 
#    add about 15 lines in it (copy some text from net)
#    Write a program to copy the first 10 lines 
#    to a file file2_10.txt
#    and the last 5 lines to file3_5.txt

source_file='S:/Aroha_tech/python/python_assignment/file1.txt'
with open(source_file,'r') as outfile1:
    lines=outfile1.readlines()
with open('S:/Aroha_tech/python/python_assignment/file2_10.txt','a') as outfile2:
    for i in range(10):
        outfile2.write(lines[i])
with open('S:/Aroha_tech/python/python_assignment/file3_5.txt','a') as outfile3:
    for i in range(-5,0):
        outfile3.write(lines[i])
