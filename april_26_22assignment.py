# concepts to use it comprehension, loops, string methods,
# list, set, dict, tuple , user defined function, random, lambda etc

# 1) given a set1 = set()
#    populate the set with the following :
#    10 random numbers less than 500
#    25 random numbers above 1000 but less than 5000
#    15 random numbers - can be anything
#    convert the set to tuple. use comprehnsion to find the sum
#    of all the odd numbers
#    which is the highest even number?
#    how many numbers are divisible by 5 as well as 7 ? (it should not be
#    2-digit number, except that)
#    find the avg of the number which is in the range of 600 to 800
#    (both the range inclusive)

import random
def fn1():
    set1=set()
    set1={x for x in random.sample(range(500),10)}
    set1.update({x for x in random.sample(range(1001,5000),25)})
    set1.update({x for x in random.sample(range(600,800),15)})
    set1=tuple(set1)
    print(set1)
    sumodd=sum(i for i in set1 if i%2!=0)
    try:
        higheven=max((x for x in set1 if x%2==0))
    except ValueError:
        higheven=0
    try:
        dv57=max(filter(lambda x : x%5==0 and x%7==0 and (x<=9 or x>99),set1))
    except:
        dv57=0
    try:
        lst=list(x for x in set1 if x>=600 and x<800)
        avg=sum(lst)/len(lst)
    except:
        avg=0

    return sumodd,higheven,dv57,avg
a,b,c,d=fn1()
print('sum of odd number is ',a)
print('highest even number is ',b)
print('number divisible by 5 and 7 and is not 2 digit number is ',c)
print('average of the number which is in the range of 600 and 800 is ',d)

# 2. input a sentence each word seperated by #
#    example today#is#Tuesday#month#is#April
#    split on the basis of #, store them in the list
#    convert all the words to upper case
#    sort the list
#    create a dictionary called words_dict ={}
#    all the words starting between A to H - store it against the 
#    key 100 , value list of words
#    I to N - store it against the key 250 , value list of words
#    M to Z - store it against the key 350
#    Given 
#    data1 = { 'Ganesh','Harish','Xavier','Deepak','Bhashkar','Lata','Usha'
#              'Zubin','Rishi','Vivek' }
#    add these names in the words_dict
sentence='today#is#Tuesday#month#is#April'
new=sentence.split('#')
new=[x.upper() for x in new]
new.sort()
words_dict={100:list(),250:list(),350:list()}
data1 = {'Ganesh','Harish','Xavier','Deepak','Bhashkar','Lata','Usha','Zubin','Rishi','Vivek'}
for i in data1:
    if i[0]>='A' and i[0]<='H':
        words_dict[100].append(i)
    elif i[0]>='I' and i[0]<='N':
        words_dict[250].append(i)
    elif i[0]>='M' and i[0]<='Z':
        words_dict[350].append(i)
    else:
        pass
print(new)
print(words_dict)


# ************