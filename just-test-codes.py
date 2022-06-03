def add():
    name = input('Account Name:')
    pwd = input('Password: ')
    
    with open('"name".txt', 'a') as a: ##automatically closes the file after reading it
        a.write(name + "|" + pwd + "\n")
        
        
    
def test2(marko):
    x = marko
    return x, 100, [0, 1, 2], False

a, b, c, d = test2('watataps')

print(a)
# abc

print(b)
# 100

print(c)
# [0, 1, 2]
print(d)
user = 'mark'
pwd = 'tenorio'
def check(a,b):
    users  = []
    password = []
    if user in users and pwd in password:
        print('Logging in..')
        return True
    else:
        return False
x = check(user,pwd)
print(x)


##############
import re
x = 'mark'

a = "kramasdasd markjosh"

pattern = r"x+[^.]*\."
match = re.match(f"{x}[^.]*", a)
print(match)