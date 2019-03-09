import random
import requests
import string
x=input("Enter s for strong psswrd and w for weak:")
z=['alaska','zamboni','mofo','yolo','casa casa']
if x=='s':
    x=int(input("enter password length:"))
    c=''.join(random.choice(string.ascii_letters + string.digits) for n in range(x))
    print("your password is ",c)
elif x=='w':
    k=random.choice(z)
    print("your password is ",k)

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()
ayo=random.choice(WORDS)
print(ayo)
