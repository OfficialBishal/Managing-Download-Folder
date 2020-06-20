import os 
import platform
import shutil
import getpass
from time import sleep
from .Fileextensions import *

class org:
    #Class To Organise
    def __init__(self):
        print("Ready")
    def usernameFind(self): 
        #Check Username of logged in user
        self.user = self.username()
    def platformUsing(self):
        '''checking os'''
        self.platformName = platform.system()
        if(self.platformName =='Windows'):
            self.initialPath = 'C:/Users/'
        elif(self.platformName =='Linux'):
            self.initialPath = '/home/'
    def setPath(self):
        """Path of Download folder and Documents folder"""
        self.path_ = self.initialPath + self.user+'/Downloads/'
        if self.platformName == 'Linux':
            self.path2_ = self.initialPath + self.user + '/Documents/'
        else:
            self.path2_ = self.initialPath + self.user + '/Documents/'
            if(not(self.checkPath(self.path2_))):
                self.onedrive = True
                self.path2_ = self.initialPath + self.user + '/OneDrive/Documents/'
    def checkPath(self, pathNeeded):
        return(os.path.isdir(pathNeeded))
    def username(self):
        '''Get username of logged in user'''
        return getpass.getuser()
    def checkFileType(self,ext, user, path_, initialPath,platformName):
        '''Check if the file is System, Video, audio, raster-image or none of them'''
        types_ = ['audio' for i in audio[:] if i == self.ext]
        if types_ and types_[0] == 'audio':
                return(self.initialPath + self.user+ '/Music')
        types_ = ['video' for i in video[:] if i == self.ext]
        if types_ and types_[0] == 'video':
            return (self.initialPath + self.user + '/Videos')
        types_ = ['raster-image' for i in image[:] if i == self.ext]
        if types_ and types_[0] == 'raster-image':
            if self.platformName == 'Linux':
                return(self.initialPath + self.user +'/Pictures')
            else:
                if(self.onedrive):
                    return(self.initialPath + self.user +'/OneDrive/Pictures')
                else:
                    return(self.initialPath + self.user +'/Pictures')
        types_ = ['document' for i in document[:] if i == self.ext]
        if types_ and types_[0] == 'document':
            if self.platformName == 'Linux':
                return(self.initialPath + self.user+'/Documents')
            else:
                if(self.onedrive):
                    return(self.initialPath + self.user +'/OneDrive/Documents')
                else:
                    return(self.initialPath + self.user +'/Documents')
        if not types_:
            return('None')
    def moveByExt(self, path_, ext, entry):
        '''Arrange Files through Extension'''
        if os.path.exists(path_+'/'+ext):
            shutil.move(path_+'/'+entry,path_+'/'+ext+'/'+entry)
        else:
            os.makedirs(path_+'/'+ext)
            shutil.move(path_+'/'+entry,path_+'/'+ext+'/'+entry)
    def moveToRespectiveFolder(self,move,name,path_):
        '''Moves file to respectie folder'''
        shutil.move(path_+'/'+name,move+'/'+name)
    def runInfinite(self):
        '''Repeat organizing every 60 seconds'''
        while(1):
            self.runOnce()
            print(".")
            sleep(60)
    def runOnce(self):      
        self.usernameFind()
        self.platformUsing()
        self.setPath()
        '''Organize everything once'''
        for entry in os.scandir(path = self.path_):    #Scan dir of path of Downloads
            if entry.is_dir():  #check if it is dir
                continue
            self.ext = entry.name.split('.')[-1] #gets extension for a file
            if (self.ext == 'crdownload' or self.ext == 'part' or self.ext == 'ini'):
                continue
            self.move_ = self.checkFileType(self.ext, self.user, self.path_, self.initialPath, self.platformName)
            try:
                if self.move_ == 'None': 
                    self.moveByExt(self.path_ , self.ext, entry.name)
                else:
                    self.moveToRespectiveFolder(self.move_, entry.name, self.path_)
            except FileExistsError:
                continue
        for entry in os.scandir(path = self.path2_):  #Scans dir of path of Documents
            if entry.is_dir():  #Checks if it is dir
                continue
            self.ext = entry.name.split('.')[-1] #gets extension for a file
            try:
                self.moveByExt(self.path2_ , self.ext, entry.name)  #move file by extension
            except FileExistsError:
                continue
    def __del__(self):
        print("Done")