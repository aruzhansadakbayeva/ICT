
import re 
def delvow(string): 
  newstr = re.sub( "[aeiouAEIOU]","",string)
  newstr1 = re.sub("\B",".",newstr)
  return(re.sub("\A",".",newstr1).lower())
  
       
 

string = str(input())
print (delvow(string))