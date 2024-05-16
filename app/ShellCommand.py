import subprocess
import time
from datetime import date


class ShellComands:
    
    def __init__(self) -> None:
        pass
    
    
    def getCommand(self, command):
        return subprocess.run(command, shell=True)
    
    #, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    def Normalization(self,inputFile):
        
        command = f"cd /home/drys/Public/imports-magmi/; php console.php normalize-images data/{inputFile} data/{inputFile}_nrm"  

        self.getCommand(command)
        
    def AddImages(self, exportFile, resultFile, inputFile, outputFile):
        command = f"cd /home/drys/Public/imports-magmi/; php console.php add-images data/{exportFile} data/{resultFile} data/{inputFile}/ data/{outputFile}/"
        
        self.getCommand(command)
        
    
    def ExtractImages(self, jsonFile, outputFile):
        command = f"cd /home/drys/Public/imports-magmi/; php console.php extract-images data/{jsonFile} data/{outputFile}"
        
        self.getCommand(command)
        
    def SendImagesInServer(self, inputFile):
        command = f"rsync -a --progress /home/drys/Public/imports-magmi/data/{inputFile}/ app@10.10.0.227:/mnt/images_magmis/{inputFile}"
        
        self.getCommand(command)
        
    def DownloaderImages(self, inputFile, outputFile):
        command = f"cd /home/drys/Public/imports-magmi/; php console.php download:images data/{inputFile} data/{outputFile} -s b2b -vvv"
        
        self.getCommand(command)
        

    
    def GetDate():
        today = date.today()
        d1 =  today.strftime("%d_%m_%Y")
        return d1
    
    