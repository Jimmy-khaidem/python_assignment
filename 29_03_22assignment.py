# (write functions, call functions, make it return values)
# 1. input the principle, rate and time
#    compute the simple interest and amount
#    SI = ( P x T x R ) / 100
#    Amount = SI + P
#    .......
#    should have (say) functions like this
#    input_data()
#    compute_interest()
#    display_amount()
#    display_simple_interest()

def input_data():
    a=int(input('enter the principle'))
    b=int(input('enter the rate'))
    c=int(input('enter the time'))
    return a,b,c
p,r,t=input_data()
def compute_interest():
    si=(p*r*t)/100
    amont=si+p
    return si,amont
s,amt=compute_interest()
def display_simple_interest():
    print(s)
display_simple_interest()
def display_amount():  
    print(amt)
display_amount()


# 2. given to you a prod_dict = 
#             Price  quantity
#               /    /
#    { 1000: (72.55,10), 2000 : (56.25,5), 3000: (25.25,15) }
#    given prod_name = { 1000: 'Toothpaste', 2000 : 'Soap' , 3000 : 'Campor' }
#    the user is asked to enter the prod name
#    and let say the user inputs Soap
#    then display the amount accordingly
#    also display the quantity available
#    ask the user how much to buy ? if the buying qty inputted is 
#    less than or equal to available qty then go ahead with transaction
#    otherwise display 'Asked qty is NOT available'
#    on transaction being successful deduct the qty accordingly and update
#    Keep doing this till the user say - wish to quit ? YES

prod_dict = { 1000: (72.55,10), 2000 : (56.25,5), 3000: (25.25,15) }
prod_name = { 1000: 'Toothpaste', 2000 : 'Soap' , 3000 : 'Campor' }
while True:
    prod_name = {k:v.upper() for (k,v) in prod_name.items()} ##using dictionary comprehension
    found=0
    item=input('enter the prod_name you want to buy: ')
    item=item.upper()
    if item in prod_name.values():
        for k,v in prod_name.items():
            if v==item:
                found=k
        for k,v in prod_dict.items():
            if k==found:
                print('amount is ',v[0])
                print('quantity available is ',v[1])
                user=int(input('how much do you want to buy? '))
                price=v[0]
                if user<=v[1]:
                    qty=v[1]-user
                    amt=user*price
                    print(amt)
                    print('thank you for  buying your bill amount is ',amt)
                else:
                    print('Asked qty is NOT available')  
        prod_dict.update({found:(price,qty)})  
        print(prod_dict)
    else:
        print('product not available')
    con=input('do you wish to quit: ')
    con=con.upper()
    if con=='YES':
        break


# 3. set1 = { 100, 560,220, 565,121, 10, 15}
#    list1 = [890,560,-220, -565, 12,-10 , 14,22,15]
#    process the set1 , pick the element and search in the list1
#    if the element exists in the list1 (either poistive or negative)
#    example say  10 OR -10 then delete it from the list1
#    count how many got deleted.
#    Once the delete count exceeds 4 then STOP otherwise go ahead and process 
#    the set1

set1 = {890,560,100, 560,220, 565,121, 10, 15}
list1 = [890,560,-220, -565, 12,-10 , 14,22,15]
lst=list(set1)
print(lst)
count=0
list1=[abs(i) for i in list1]
for j in lst:
    for k in list1:
        print(k,j)
        if count==4:
            break 
        elif j==k:
            list1.remove(k)
            count=count+1
print(list1)
    
                


        
