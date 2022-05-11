import os
import shutil
 
envfile=open("S://Aroha_tech//python//.env",'r')
lst=[x.split('=') for x in envfile]
dic={i[0]:i[1].replace("\n",'') for i in lst} 
source=dic['source']
target=dic['target']
for j in os.listdir(source):
    sourcefile=source+j
    targetfile=source+j
    if os.path.isfile(sourcefile):
        shutil.copy(source+j,target+j)



#same program using dotenv modules
from dotenv import load_dotenv
load_dotenv()
source = os.getenv('source')
target = os.getenv('target')
print(target)
for file in os.listdir(source):
    file_to_copy= source + file
    file_to_paste= target + file
    if os.path.isfile(file_to_copy):
        shutil.copy(file_to_copy,file_to_paste)
     