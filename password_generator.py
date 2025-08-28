#Hello Everyone . Today we are see abou PassWord Generator

#Let see the Program

#Firstafal import the Statement

import random
import string

#Here random means to create a random password and string is used to access

#Now create a function

def password_generator():
    length=int(input("Enter the Length of the password:"))
#Here Length represent the Howmany length the password want by the user
    character=string.ascii_letters+string.digits+string.punctuation
#Here ascii_letter means abced like that and also ABCD like and digits is 0 - 9 and punctuation like speacial character
    password=''.join(random.choice(character) for _ in range(length))
#Here the join means join or generate the password from the character
    print(password)
password_generator()
#the finalize the function 
    


#Thank you
