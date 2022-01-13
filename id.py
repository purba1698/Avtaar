username=input("enter your name::")

import uuid

print ("The random id is : ",end="")
print (uuid.uuid1())

from datetime import datetime
now=datetime.now()
print("Request Time: ",now.strftime("%Y-%m-%d %H:%M:%S"))
