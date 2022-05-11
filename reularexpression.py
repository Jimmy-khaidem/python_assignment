import re  
# count=0   
# pattern=re.compile("ab")   
# matcher=pattern.finditer("abaababa")   
# for match in matcher:   
#     count+=1   
#     print(match.start(),"...",match.end(),"...",match.group())
# print("The number of occurrences: ",count)
print('----------------------------------------------------------------')
# count=0     
# matcher=re.finditer('ab',"abaababa")   
# for match in matcher:   
#     count+=1   
#     print(match.start(),"...",match.end(),"...",match.group())
# print("The number of occurrences: ",count)

# print("--------------------------------------------------------------------")
# character classes to search group of characters
# 1. [abc]===>Either a or b or c 
# 2. [^abc] ===>Except a and b and c 
# 3. [a-z]==>Any Lower case alphabet symbol 
# 4. [A-Z]===>Any upper case alphabet symbol 
# 5. [a-zA-Z]==>Any alphabet symbol 
# 6. [0-9] Any digit from 0 to 9 
# 7. [a-zA-Z0-9]==>Any alphanumeric character 
# 8. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters) 




#predefined character classes
#  \s ->Space character 
# \S -> Any character except space character 
# \d -> Any digit from 0 to 9 
# \D -> Any character except digit
#  \w -> Any word character [a-zA-Z0-9] 
# \W -> Any character except word character (Special Characters) 
# .  -> Any character including special characters 

# x="\s"
# matcher=re.finditer(x,"a7b k @9z")   
# for match in matcher:   
#     print(match.start(),"......",match.group())   



#QUANTIFIER:-


#  a -> Exactly one 'a'  
# a+ ->Atleast one 'a'  
# a* -> Any number of a's including zero number  
# a? -> Atmost one 'a' ie either zero number or one number  
# a{m} -> Exactly m number of a's  
# a{m,n} -> Minimum m number of a's and Maximum n number of a's 
# x='a{1,2}'
# matcher=re.finditer(x,"abaaabaaaaab")   
# for match in matcher:   
#     print(match.start(),"......",match.group())   



print('---------------------------------------------------------------')


#IMPORTANT FUNCTION OF RE MODULES

# 1. match()  
# 2. fullmatch()  
# 3. search()  
# 4.findall()  
# 5.finditer()  
# 6. sub()  
# 7.subn()  
# 8. split()  
# 9. compile() 



