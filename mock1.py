# x=list(filter(lambda x:x%2!=0,range(167,379)))
# print('odd numbers from 167 to 168 is ',x)
# print('sum of  167 to 379 is ',sum(x))
# print('average is ',sum(x)/len(x))

# print the alternate char from the inputted string (max of 10 char only)
# from reverse
# (donot take space into the account/no counting/ignore SPACE)

a=input('enter a string :')
a=list(a)
alterReverse=a[::-1]
revStr=[]
count=0
for i in alterReverse:
    if len(revStr)>=13:
        break
    else:
        if count%2==0:
            count+=1
            if i!=' ':   
                revStr.append(i)
            else:
                count-=1
        else:
            count=count+1
print(''.join(revStr))

# ===every one keep doing this
# s1 = {45,79,12,69,37,59,111,119}
# process the set and print maximum 3 prime numbers from it
s1 = {2,7,45,79,12,69,37,59,111,119}
primecount=0
for i in s1:
    con=False
    if i>1:
        for j in range(2,i):
            if i%j==0:
                con=True
                break
    if con==False:
        primecount+=1
        if primecount<=3:
            print(i)



    

