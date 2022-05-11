
#program to find the file which size is greater than the user input value


import os,glob
# sz = os.path.getsize("25practice.py")
# print(sz)
def fcheck(n):
    lst=[]
    path = 'S:\Aroha_tech\python\*'
    files = glob.glob(path)
    for f in files:
        x=os.path.getsize(f)
        if x>n:
            lst.append(f)
    return lst
res=fcheck(9000)
print(res) 



