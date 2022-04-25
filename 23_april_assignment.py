# 1) data1= [ 100,200,'500','6501',400]
#    process the data1 (hint use type and int)
#    add all the numbers , find the sum, avg, min and max
#    use for loop
# data1= [100,200,'500','6501af',400]
# data2=[]
# for i in list(data1):
#     if type(i)==int or type(i)==float:
#             data2.append(i)
#     else:
#         try:
#             i=int(i)
#             data2.append(i)
#         except:
#             pass
# print(data2)
# print('sum of the list is :',sum(data2))
# print('average of the list is :',sum(data2)/len(data2))
# print('min of the list is :',min(data2))
# print('max of the list is :',max(data2))


# 2) data2 = (10,22,[45,33,78],[90,99],(10,12,44,100),35,99)
#    note the above tuple could have lists and other tuple
#    HINT use type to process using the for loop
#    Find the total, max, min, avg
# data2 = (10,22,[45,33,78],[90,99],(10,12,44,100),35,99)
# data2=list(data2)
# for i in list(data2):
#     if type(i)!=int:
#         for j in i:
#             data2.append(j)
#         data2.remove(i)
# print('sum of the list is :',sum(data2))
# print('average of the list is :',sum(data2)/len(data2))
# print('min of the list is :',min(data2))
# print('max of the list is :',max(data2))

# 3) 
#    Write user defined functions 
#    generate 100 random numbers in the range of 1 to 1000
#    store all the numbers less than or equal to 500 in 
#    set_500 and others in set_1000
#    store all the odd_numbers in the set_odd and even in set_even
#    find the max odd number
#    find the min even number
#    find the avg of all the even numbers
#    Sort the set_odd, in that find the avg of last 10 highest numbers
#    in the set_odd
# import random
# def numberGenerator():
import random
def numberGenerator():
    randomlist = random.sample(range(1,1000), 100)
    set_500=set()
    set_1000=set()
    set_odd=set()
    set_even=set()
    for i in randomlist:
        if i%2==0:
            set_even.add(i)
        else:
            set_odd.add(i)
        if i<=500:
            set_500.add(i)
        else:
            set_1000.add(i)
    set_odd=list(set_odd)
    set_odd.sort()
    last10=[x for x in set_odd[:-11:-1]]
    
    return max(set_odd),min(set_even),sum(set_even)/len(set_even),sum(last10)/len(last10)
maxodd,mineven,avgeven,avglast10=numberGenerator()
print('maximum of odd number is :',maxodd)
print('minimum of even number is :',mineven)
print('average of even number is :',avgeven)
print('average of last 10 highest odd numbers :',avglast10)
# 4) input the sentence into a string
#    convert the sentence into upper case
#    use the converted upper case string for the following...
#    convert the string to the list (HINT use split)
#    sort the list
#    store the word having more than 3 or more vowels in the set
#    set_vowel
#    create a dict with keys as 100 and 200
#    100 indicates that all the words starting with A to M will be 
#    stored as set against the key 100
#    200 indicates that all the words starting with N to Z will be stored 
#    against the key 200
#    example...
#    100 :  {'AND','LIVING','DIETY','GARDEN',.....}
#    200 :  {'NEITHER', 'ODD', 'PROFESSIONAL','ZUBEN','X-MAS','VIOLIN',...}

word=input('write a sentence :').upper()
wordlst=word.split()
set_vowel=set()
dict={100:set(),200:set()}
vowels='AEIOU'
for i in wordlst:
    count=0
    for j in i:
        if j in vowels:
            count+=1
    if count>=3:
        set_vowel.add(i)
    if i[0] >='A' and i[0]<='M':
        dict[100].add(i)
            
    elif i[0]>='N' and i[0]<='Z':
        dict[200].add(i)
    else:
        pass
print('words having 3 or more vowels :',set_vowel)
print(dict)
# ****************
