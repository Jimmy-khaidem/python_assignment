lst=[1,2,4,5,6,7,8,4,3,1,4]
for i in list(lst):
    if lst.count(i)>1:
        lst.remove(i)
print(lst)
lst1=['bangalore','chennai','mumbai']
lst2=[1,2,3,4]
lst3=['james','tom','Chris','frank']
for i,j,k in zip(lst1,lst2,lst3):
    print(i,j,k)
import os
import shutil
 
# Get the list of all files and directories
path = "S:\PYTHON\python advanced\PDF"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)
print('***************************************************************')
print()
source_folder = "S:/PYTHON/python advanced/PDF/"
destination_folder = "S:/PYTHON/python advanced/demo/"
file=os.listdir(source_folder)
print(file)

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)
    os.remove(source_folder + file_name)


