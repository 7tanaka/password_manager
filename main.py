from getpass import getpass
import re




def create_account(user,pwd):
     with open(f'txt/ccount_list.txt', 'a') as cr:
        cr.write(user + "|" + pwd + "\n")

def check(user,pwd):
    name = user
    users  = []
    password = []
    with open(f'txt/account_list.txt', 'r') as c:
        
        for line in c.readlines():
            data = line.rstrip()
            user1,pwd1 = data.split('|')
            users.append(user1)
            password.append(pwd1)
    if user in users and pwd in password:
        print('Logging in..')
        return True, user
    else:
        
        return False, user
                

def view(user):
    var = user
    
    with open(f'txt/passwords.txt', 'r') as v:
        
        
        for line in v.readlines():
            data = line.rstrip()
            acc, user, pwd = data.split("|")
            x = acc+user+pwd
            match = re.match(f"{var}[^.]*", x)
            if match:
                print("Account Name: ",acc,"|", "Username: ",user,"|","password: ", pwd)
            
            
            
def add(user):
    name = input('Account Name:')
    pwd = input('Password: ')
    
    with open('passwords.txt', 'a') as a: ##automatically closes the file after reading it
        a.write(user + "|" + name + "|" + pwd + "\n")




while True:
    print("Password Manager")
    username= input('Username: ')
    password = getpass()

    verify, user_name  = check(username,password)
    if verify:
        while True:
            mode = input("What mode would you like to do? \n(add, view) or q to quit\n").lower()
            
            if mode == 'q':
                exit()
            elif mode == 'add':
                add(user_name)
            elif mode == 'view':
                view(user_name)
            else:
                print('Invalid mode')
                continue
    else:
        print(user_name, "can't be found" )
        ask = input('Would you like to create an account? (yes/no) ').lower()
        if ask == 'yes':
            username = input('Enter your username: ')
            password = input('Password: ')
            create_account(username,password)
            print('Account created!')
            continue
        else:
            break
