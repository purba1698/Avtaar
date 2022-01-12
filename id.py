import random
import string

print('This is an unique id generator!')

length = int(input('\nEnter the length of the id: '))                      

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)
 
id = "".join(temp)
print(id)