import os
import fleep  
import move
import platform
user=move.username() #Check Username of logged in user
#checking os
platformName = platform.system()
if(platformName=='Windows'):
    initialPath = 'C:/Users/'
elif(platformName=='Linux'):
    initialPath = '/home/'
#Path of Download folder and Documents folder
path_ = initialPath +user+'/Downloads/'
path2_ = initialPath +user+'/Documents/'
for entry in os.scandir(path=path_):    #Scan dir of path of Downloads
    if entry.is_dir():  #check if it is dir
        continue
    ext = entry.name.split('.')[-1] #gets extension for a file
    with open(path_+'/'+entry.name,"rb") as file: #Opens that file as a binary file
        DataType = fleep.get(file.read(128)).type   #fleep gets the file type
    if not DataType:    #Somefile's data type is not returned hence those are sorted in download folder by extension
        move.moveByExt(path_ , ext, entry.name)
        continue
    move_ = move.checkFileType(DataType,user,path_, initialPath) #check file type
    if move_ == 'None': 
        move.moveByExt(path_ , ext, entry.name)
    else:
        move.moveToRespectiveFolder(move_,entry.name,path_)
for entry in os.scandir(path = path2_):  #Scans dir of path of Documents
    if entry.is_dir():  #Checks if it is dir
        continue
    ext = entry.name.split('.')[-1] #gets extension for a file
    move.moveByExt(path2_ , ext, entry.name)  #move file by extension
