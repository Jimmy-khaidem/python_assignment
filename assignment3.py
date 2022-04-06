names=('Uday','Shankar','Hari','Gopal')
names1=list(names)
n='Gopal'
for i in names1:
    if i==n:
        names1.remove(i)
names=tuple(names1)
print(names)



data1=(12,45,67,22,44,12,12,89,100)
t2=len(set(data1))
print('number of unique values are:',t2)


data2='kiran,Shankar Rao,Akash,Kiran Chopra,Gopal Kamath'
x=data2.split(',')
x.sort()
count=0
for i in x:
    if i.endswith('a') or i.endswith('n'):
        count=count+1
print('number of names ends with a or n are:',count)

empid=(100,250,330,19,671)
emp_names=['Anand','Ganesh','Veer','Jagat','Kirty']
employ={}
how=len(empid)
for i in range(0,how):
    employ.update({empid[i]:emp_names[i]})
print(employ)

def imp():
    n=0
    while True:
        n=int(input('enter a number:'))
        if n>999 and n<10000:
            break
    return n
n1=imp()
n2=imp()
print('sum is',n1+n2)


data1=(100,133,-118,-456,667,900,12,55,68)
data2=['123','566','-588','7809']
od=set()
evn=set()
neg=set()
numb_dict={}
for i in data1:
    if i>0:
        if i%2==0:
            evn.add(i)
        else:
            od.add(i)
    else:
        neg.add(i)
for j in data2:
    j=int(j)
    if j>0:
        if j%2==0:
            evn.add(j)
        else:
            od.add(j)
    else:
        neg.add(j)

numb_dict.update({'ODD':od})
numb_dict.update({'EVEN':evn})
numb_dict.update({'NEGATIVE':neg})
print(numb_dict)

def digit_4():
    n=0
    while True:
        try:
            n=int(input('enter a 4 digit number:'))
            if n>999 and n<10000:
                break
            else:
                print('please reenter 4 digit number')
        except ValueError:
            print('please reenter only 4 digit number please')
    return n
print('-----MAIN BLOCK starts-------')
numb=[]
how=int(input('how many 4 digit number you wish to put?'))
for i in range(0,how):
    result=digit_4()
    print('well the input is valid')
    numb.append(result)
print('total is:',sum(numb))



