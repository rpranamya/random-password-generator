import random
import string
name = list(string.ascii_letters+string.digits+"@_")
def randpassgen():
    length = int(input("length?"))
    passwd = []
    for i in range(length):
        passwd.append(random.choice(name))
    random.shuffle(passwd)
    final = ''.join(passwd)
    print(final)

randpassgen()