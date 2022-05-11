#  given
#   prod = { 100 : ['Laptop',45550,True], 200 : ['Mouse',2000,False] }
#   key is 100
#   value is list describing the item name, price and True indicates
#   available in store, False not available
#   write a function to add more products till the user type -1 to stop
#   write a function display_all to iterate and display all the items
#   which are AVAILABLE in the store
#   write a function display_item which accepts the item code and if that
#   item exists then display the details and if the item code is not there
#   display ITEM not found
#   have a function called item_not_available which has a dict
#   by name itm_not_in store = { } which holds all the items with the 
#   status False
#   the code should be menu driven.....
#   1. Add
#   2. Display all
#   3. display specific item
#   4. Move item NOT avialable
#   5. E X I T out of menu
#   enter your choice .....





# class Product:
#     prod = { 100 : ['Laptop',45550,True], 200 : ['Mouse',2000,False] }
#     def add(self):
#         while True:
#             try:
#                 key=int(input('enter key :'))
#                 value=[]
#                 if key==-1:
#                     break
#                 else:
#                     itemname=input('enter item name :')
#                     price=int(input('enter price :'))
#                     while True:
#                         available=input('enter True or False :').capitalize()
#                         if available=='True':
#                             available=True
#                             break
#                         elif available=='False':
#                             available=False
#                             break
#                         else:
#                             print('Please enter True or False ')
#                     value.append(itemname)
#                     value.append(price)
#                     value.append(available)
#                     Product.prod.update({key:value})
#             except:
#                 print('input integer for key and price only')
#     def displayall(self):
#         a=[]
#         for k,v in Product.prod.items():
#             if v[2]==True:
#                 a.append(v[0])
#         print('available items are',a)
#     def displayspecificitem(self):
#         con=True
#         while con:
#             try:
#                 ask=int(input('enter the item code: '))
#                 if ask in Product.prod.keys():
#                     for k,v in Product.prod.items():
#                         print(k)
#                         if k==ask:
#                             print('details: ',v)
#                             con=False  
#                 else:
#                     print('Item not found')
#                     con=False
                    
#             except:
#                 print('you have enter wrong input  item code is in integer format')
#     def item_not_available(self):
#         itm_not_instore={ }
#         for k,v in Product.prod.items():
#             if v[2]==False:
#                 itm_not_instore.update({k:v})
#         print(itm_not_instore)
#     def exit(self):
#         while True:
#             move=input('exit the menu : YES?NO').upper()
#             if move=='YES':
#                 break
#             elif move=='NO':
#                 p.add()
#                 p.displayall()
#                 p.displayspecificitem()
#                 p.item_not_available()
#             else:
#                 print('choose Yes or NO')

# p=Product()
# p.add()
# p.displayall()
# p.displayspecificitem()
# p.item_not_available()
# p.exit()




        


    


# 2) have any text file (motivational.txt) , 
#    created in notepad having few sentences
#    say this one....
#    *******
#    Sudha Murthy was hardworking and determined to succeed in her studies, 
#    which is why she emerged a topper in both her undergraduate and 
#    postgraduate studies. After graduation, Sudha Murthy was hired by 
#    TATA Engineering and Locomotive Company, also known as TELCO, 
#    and she was the first female engineer in the company.
#    At every stage in our lives, we come across immense challenges and 
#    various forms of discrimination. But that should not discourage 
#    us from performing our best. We should be determined and 
#    strive to achieve success despite the obstacles we 
#    face in life. And we should have the courage to fight and 
#    eradicate policies that may stifle the growth of our country. 
#    These are some of the lessons that we can learn from Sudha Murthy.
#    ************* 
#    open that file , find out how many words are there 
#    which word is having the max length (there can be many words of the same length)
#    have ALL those words
#    Display the LAST 10 words from the file
# import os
# number_of_words = 0
# max_len=''
# f = open(r'S:\Aroha_tech\assignmentQ\python\motivational.txt')
# for i in f:
#     data = f.read()
#     lines = data.split()
#     for word in lines:
#         number_of_words += 1
#         if len(word)>len(max_len):
#             max_len=word
# print(number_of_words)
# print(max_len)
# print(lines[-10:])




# 3. Store 'n' names in the a set (till the user types STOP), 
#    sort the name set 
#    how many names are there which starts from R to U
#    display the last 2 char of the names from the set (use SLICING)
#    How many names are there with Last name
#    say the name can be Ravi Rao, Anish Kamath, Uday , Rashmi Bhat etc...

# class Name:
#     names=set()
#     def setName(self):
#         while True:
#             nme=input('input some name :')
#             if nme.upper()=='STOP':
#                 break
#             else:
#                 Name.names.add(nme)
#     def solve(self):
#         c=0
#         lastnamecount=0
#         alpha=['R','S','T','U']
#         name1=list(Name.names)
#         name1.sort()
#         for i in name1:
#             for j in alpha:
#                 if i.upper().startswith(j):
#                     c+=1
#             if len(i.split(' '))>1:
#                 lastnamecount+=1
#         last2char=list(map(lambda x:x[-2:],name1))
#         print('number of names starts from R to U are',c)
#         print('last two char of all the names are', last2char)
#         print('number of names with last names are ',lastnamecount )
# n=Name()
# n.setName()
# n.solve()
a='adfs'
print(a[0:5])
