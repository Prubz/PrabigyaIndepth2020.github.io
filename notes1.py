  def createNoteAndFolder(self):
        os.chdir("./Notes")

        self.fileName = self.fileName + self.extension
        if os.path.isdir("./" + self.folderName):
            os.chdir("./" + self.folderName)
        else:
            os.mkdir(self.folderName)
            os.chdir("./" + self.folderName)
    
        if not os.path.isfile("./" + self.fileName):
            open(self.fileName, "a").close()

        os.system("subl " + self.fileName)
    
    def findFileInFolder(self, folder):
        if os.path.isdir(self.path + "/" + folder):
            self.path = self.path + "/" + folder
            self.findFile(self.fileName, "", self.path)
        else:
            self.path = self.findFolder(folder, "", self.path)
            self.findFile(self.fileName, "",  self.path)
        
        # print(self.path)
        os.system("subl " + self.path)
    
    def findFile(self, fileToFind, folderToSearch, thepath):
        fileExists = False
        pathToFolder = ""
        for subdir, dirs
        , files in os.walk(thepath + folderToSearch):
            for dir_ in dirs:
                if dir_.lower() == self.folderName.lower():
                    pathToFolder = ""
                    pathToFolder = subdir + "/" + self.folderName
            for file_ in files:
                name = ""
                for i in range(len(str(file_))):
                    if len(str(self.fileName)) > i:
                        if str(file_).lower()[i] == str(self.fileName).lower()[i]:
                            name = name + str(file_)[i]
                            if len(name) > len(self.fileName) * 0.8:
                                self.path = os.path.join(subdir, file_)
                                fileExists = True
                                break
        if not fileExists:
            self.path = os.path.join(pathToFolder ,self.fileName + self.extension)
            open(self.path, "a").close()
