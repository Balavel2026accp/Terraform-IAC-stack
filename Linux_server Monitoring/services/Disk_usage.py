## Disk Usage monitor. 
import subprocess
from pprint import pprint
import platform
import os 

class disk_details:
    def disk_information(self):
        Os_name = platform.system()
        
        ## check disk information
        try:
            if Os_name == "Linux":
                disk_information = subprocess.run("df -h", shell=True, capture_output=True, text=True)
                #raise PermissionError("Do not have permission to execute the command")
                lines = disk_information.stdout.splitlines() 
                headers = lines[0].split()
                headers[-2:] = ["Mounted on"]
                ## create file system dictionary
                filesystems = []

                for line in lines[1:]:
                 values = line.split(maxsplit=5)
                 filesystems.append(dict(zip(headers, values)))
            return filesystems     

        except subprocess.CalledProcessError as error:
            return "Command not found", error
        
        except ValueError as a:
            return "Os type mismatched", str(a), Os_name
        
        except Exception as f:
            return "Unexpected error", str(f)

object1 = disk_details()
print(object1.disk_information())        
        
        
