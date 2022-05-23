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

