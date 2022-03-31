# def fn():
#     while True:
#         cos=eval(input('enter the cost of the article: '))
#         cat=input('''choose the category:
#                      A
#                      B
#                      C
#                      : ''')
#         proft=0
#         if cat=='A':
#             proft=8/100
#         elif cat=='B':
#             proft==6.5/100
#         elif cat=='C':
#             proft==5.5/100
#         else:
#             print('you have selected the wrong category')

#         print('selling price of the article is ',cos+(cos*proft))
#         con=input('Do you wish to exit?--YES/NO')
#         if con=='YES':
#             break
# fn()   
# 2) input names till the user types STOP to EXIT
#    add the names to the set
#    if the name inputted already exist then display the 
#    message as the name is already there hence NOT added again
#    process how many names have Kumar or Rao as surname
#    remove the following people name lets say it is provided in a '
#    another set rem_name={'Ashok','Lalit','Pankaj','Anand','Asha','Usha'}
#    how many names were removed from the name set you created
# lst=[]
# b=''
# rem_name={'Ashok Kumar','Lalit Rao','Pankaj chettri','Anand','Asha Bonshle','Usha Rao'}
# new=list(rem_name)
# for i in new:
#     b=i.split(' ')  
#     print(b)
#     lst.append(b)
# print(lst)
# x=list(map(lambda x: x.split(' '),rem_name))
# print(x)
# x=input('enter a name')
# if x in rem_name:
#     print('ok')
# names=set()
# countsurname=0
# removeName=0
# rem_name={'Ashok','Lalit','Pankaj','Anand','Asha','Usha'}
# def func():
#     while True:
#         name=input('enter a name')
#         if name=='Stop' or name=='Exit':
#             break
#         elif name in names:
#             print('the name is already there hence NOT added again')
#         else:
#             names.add(name)
# func()
# print(names)
# x=list(map(lambda x: x.split(' '),names))
# for i in x:
#     if 'Kumar' in i or 'Rao' in i:
#         countsurname+=1
# for j in list(names):
#     for k in x:
#         if j in k:
#             names.remove(j)
#             removeName+=1
# print('number of names which have Kumar or Rao as surname is ',countsurname)
# print('number of names removed from the set of names is ',removeName)
# print(names)
# 3) create a dict called prod
#    which has key prod_id and prod_name and price are the values
#    as shown below
#    prod = { 1000: ['Laptop',55000], 2000: ['Mouse',1500],....}
#    add the prod id and the prod details in a list of prod info
#    the flow should be like this
#    enter the prod id?
#    check if the prod id exists?
#    NO not existing - then input the prod name and price and add them to 
#    a list
#    that list is added as the value for the corresponding key in the dict
#    YES - existing - then display the message that the prod id already exists
#    finally when done with adding then find out
#    the follwing details :-
#    prod details - which is the costliest item
#    prod details - which is the cheapest item
#    how many products are above the rate of 12500?

high=999999999999999
low=0
rate=[]
low_item=str()
high_item=str()
prod={1000: ['Laptop',55000], 2000: ['Mouse',1500]}
while True:

    try:
        prod_id=int(input('enter the prod_id: '))
        if prod_id in prod:
            print('prod_id is already existed')
        else:
            prod_info=[]
            prod_name=input('enter the product name: ')
            prod_price=int(input('enter the product price: '))
            prod_info.append(prod_name)
            prod_info.append(prod_price)
            prod.update({prod_id:prod_info})
        
    except ValueError:
        break
for k,v in prod.items():
    if v[1]>12500:
        rate.append(v[0])
    if v[1]>low:
        low=v[1]
        high_item=v[0]
    if v[1]<high:
        high=v[1]
        low_item=v[0]
print(high_item)
print(low_item)
print(rate)


        

    