# 1) create a dict called contact use Global variable for dict
#    store the mobile number as key 
#    name and email as value - list example:
#    9661425678 : ['Ganesh Prasad','ganesh@gmail.com']
#    9535354450 : ['Latha Srinivas','latha.srinivas@yahoo.com']
#    ..... and so on...
#    first display the menu as following:
#    1. add new mobile details
#    2. view all the details from contacts
#    3. view the details of the specific mobile
#       if that mobile exists else display
#       error message
#    4. remove the mobile number from contact
#    5. edit the details based on the mobile
#       number. correcting the email id
#       only.
#    6. EXIT
#    enter the choice:
# on EXIT convert the contact to JSON string 
# make sure you write 5 functions
# add_new_contacts()
# view_all_contacts()
# view_a_contact(mobile)
# delete_contact(mobile) - returns True if successfull delete else False
# modify_contact(mobile)
import json
class Contacts:
    contact={}
    def add_new_contact(self):
        con=True
        while con:
            try:
                while True:
                    mobile=int(input('enter mobile number :'))
                    if len(str(mobile))==10:
                        if mobile not in Contacts.contact:   
                            name=input('enter the name :')
                            email=input('enter the email :')
                            Contacts.contact.update({mobile:(name,email)})
                            break
                        else:
                            print('mobile number already existed')
                    else:
                        print('mobile number should consist of 10 numbers')
                con=False
            except ValueError:
                print('mobile number should be only number')
        return Contacts.contact
    def view_all_contacts(self):
        for k,v in Contacts.contact.items():
            print('phone number: ',k,) 
            print('name: ',v[0],' ','email: ',v[1])
            print()
            print('--------------------------------------------------------------')
    def view_a_contact(self):
        flag=True
        mobile=int(input('enter the mobile number to view the details : '))
        for k,v in Contacts.contact.items():
            if k==mobile:
                print('name :',v,'email:', v[1])
                flag=False
        if flag==True:
            print('entered number not matched')
    def delete_contact(self):
        mobile=int(input('enter the number to be deleted'))
        if mobile in Contacts.contact:
            try:
                Contacts.contact.pop(mobile)
                return True
            except KeyError:
                return False
        else:
            print('mobile Number not matched')
    def modify_contact(self):
        mobile=int(input('enter the mobile number of the email you want to modify : '))
        newmail=input('enter your new email :')
        if mobile in Contacts.contact:
            Contacts.contact.update({mobile:(Contacts.contact[mobile][0],newmail)})
            print(mobile,'      ',Contacts.contact[mobile][0],'  ',newmail)
            
        else:
            print('mobile number not found')
class Display(Contacts):
    def menu(self):
        while True:
            try:
                choice=int(input('''
                1. add new mobile details
                2. view all the details from contacts
                3. view the details of the specific mobile
                   if that mobile exists else display
                   error message
                4. remove the mobile number from contact
                5. edit the details based on the mobile
                   number. correcting the email id
                   only.
                6. EXIT
                enter the choice : '''))
                if choice==1:
                    super().add_new_contact()
                elif choice==2:
                    super().view_all_contacts()
                elif choice==3:
                    super().view_a_contact()
                elif choice==4:
                    super().delete_contact()
                    print('after deleting remaining data :')
                    for k,v in Contacts.contact.items():
                        print('phone number: ',k,'       ','name: ',v[0],' ','email: ',v[1])
                elif choice==5:
                    super().modify_contact()
                elif choice==6:
                    with open("sample.json", "w") as outfile:
                        json.dump(Contacts.contact, outfile,indent=4)
                        break
                else:
                    print('please choose from the given number')
            except ValueError:
                print('invalid input!!! please enter only number other character not allowed.')
        
d=Display()
d.menu() 
# 2) Generate some number inputing the following details
#    start value, stop value and step value
#    store the generated numbers in a list called list1
#    given there is set1 = { 500,12,55,78,191,222,150,19,290,510}
#    add 10 generated Random numbers between 1 to 1000 into the set1
#    (find out how to generate the random numbers)
#    shuffle the set1 (find out)
#    add all the elements of set1 to the list1
#    sort the list1 in descending order
#    sum the last 5 element of the sorted list
#    in the first 6 elements (of the sorted list)
#    how many elements are greater than last but 1 element ?
#    example
#                                                     |
#    [12,44,55,19,22,25,50,78,90,199,219,333,100,150,34,2000]
#     <...............>
#    how many are greater than (say) 34


