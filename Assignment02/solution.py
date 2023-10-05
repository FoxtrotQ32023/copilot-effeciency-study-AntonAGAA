# opgaven består i at søge efter strings i den speciferede streng og returnere start index for hvor ordet er.
# det første tal angiver hvor mange gange der skal søges i den n+1 linje
import re

def foo(file_path):
    with open(file_path, encoding="utf-8") as file:
        contents = file.read()
        print(contents)
        data = contents.splitlines()
        print(data)

    for i in (data):
        print(re.findall('r\d+',i))
        
    re.finditer

    

    
          
            
      

foo("Assignment02/stringmultimatching.in")



