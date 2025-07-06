import os, secrets as sec, string as s, random as ran, getpass as g, pyperclip as p, bcrypt as by
from cryptography.fernet import Fernet

def Encrypt(con) :
    key = Fernet.generate_key()
    obj = Fernet(key)
    enc = obj.encrypt(str(con).encode())
    return enc, key

def Decrypt(con, key) :
    obj = Fernet(key)
    dec = obj.decrypt(con).decode()
    return dec

def menu() :
    while True :
        print('CHOOSE YOUR ACTION\n')
        print('1. Encrypt .txt Data Securely')
        print('2. Retrieve Encrypted Files')
        print('3. Store Password Securely')
        print('4. Retrieve Password')
        print('5. Generate Secure Passwords')
        print('6. Exit The Application')
        c = int(input('\nEnter Your Action : '))
    
        if c == 1 :
            while True :
                add = input('\nEnter File Address : ')
                name = os.path.splitext(os.path.basename(add))[0]
                if os.path.splitext(add)[1] == '.txt' :
                    try :
                        with open(add, 'r') as f :
                            r = f.read()
                            a, b = Encrypt(r)
                            f1 = open(f'Encrypted Files/{name}.txt', 'wb')
                            f2 = open(f'Key/{name}key.txt', 'wb')
                            f1.write(a)
                            f2.write(b)
                            f1.close()
                            f2.close()    
                            print('\nData Encrypted And Stored In Vault Securely\n')
                            break
                    except FileNotFoundError :
                        print('\nPath Not Found')
                else :
                    print('\nPlease Give .txt File Only')
            
        elif c == 2 :
            while True :
                try :
                    name = input('\nEnter File Name : ')
                    f1 = open(f'Encrypted Files/{name}.txt', 'rb')
                    f2 = open(f'Key/{name}key.txt', 'rb')
                    r1 = f1.read()
                    r2 = f2.read()
                    c = Decrypt(r1, r2)
                    f1 = open(f'Decrypted Files/{name}.txt', 'w')
                    f1.write(c)
                    print('\nData Decrypted And Stored In \'Decrypted Files\' Folder Successfully\n')
                    f1.close()
                    break
                except FileNotFoundError :
                    print('\nFile Name Not Found')

        elif c == 3 :
            name = input('\nEnter Alias For The Password : ')
            print('\nFor Security Reasons')
            print('\nYou Can Enter The Password But It Wont Be Visible On The Screen. It Would Just Look Like Not Typing. But The Text Is Being Recognised.\n')
            while True :
                pas1 = g.getpass('Enter Password : ')
                pas2 = g.getpass('Enter Password Again For Confirmation : ')
                if pas1 == pas2 and len(pas1) != 0 :
                    con, key = Encrypt(pas1)
                    f1 = open(f'Password/{name}.txt', 'wb')
                    f2 = open(f'Password/{name}Key.txt', 'wb')
                    f1.write(con)
                    f2.write(key)
                    f1.close()
                    f2.close()
                    print('\nPassword Stored In Vault Securely\n')
                    break
                else :
                    print('\nPassword Confirmation Gone Wrong')

        elif c == 4 :
            while True :
                try :
                    name = input('\nEnter Alias For The Password : ')
                    f1 = open(f'Password/{name}.txt', 'rb')
                    f2 = open(f'Password/{name}Key.txt', 'rb')
                    r1 = f1.read()
                    r2 = f2.read()
                    c = Decrypt(r1, r2)
                    p.copy(c)
                    print('\nPassword Is Copied To The Clipboard. You Can Paste It Anywhere You Want.\n')
                    break
                except FileNotFoundError :
                    print('\nAlias Not Found')

        elif c == 5 :
            print('\nPlease Enter The Number Of Letters, Digits And Special Symbols Should Occur\n')
            let = int(input('Letters         : '))
            dig = int(input('Digits          : '))
            pun = int(input('Special Symbols : '))
            a = s.ascii_letters
            b = s.digits
            c = s.punctuation
            pas = ''
            for i in range(let) :
                pas += sec.choice(a)
            for i in range(dig) :
                pas += sec.choice(b)
            for i in range(pun) :
                pas += sec.choice(c)
            l1 = list(pas)
            l2 = []
            while True :
                r = ran.randrange(0, len(l1))
                l2.append(l1[r])
                l1.remove(l1[r])
                if len(l1) == 0 :
                    break
            st = ''
            for i in l2 :
                st += i
            p.copy(st)
            print('\nPassword Is Copied To The Clipboard. You Can Paste It Anywhere You Want.\n')
            

        elif c == 6 :
            print('\nThank You For Using The Vault')
            break

        else :
            print('\nPlease Enter A Valid Number For The Respective Action\n')

def action() :
    os.makedirs('Encrypted Files', exist_ok = True)
    os.makedirs('Decrypted Files', exist_ok = True)
    os.makedirs('Key', exist_ok = True)
    os.makedirs('Password', exist_ok = True)
    
    if not os.path.exists('Login.txt') :
        f = open('Login.txt', 'wb')
        f.close()
    f = open('Login.txt', 'rb')
    r = f.read()
    f.close()
    
    if len(r) == 0 :
        print('Sign Up')
        print('\nFor Security Reasons')
        print('\nYou Can Enter The Password But It Wont Be Visible On The Screen. It Would Just Look Like Not Typing. But The Text Is Being Recognised.\n')
        pas = ''
        f1 = open('Login.txt', 'wb')
        while True :
            if len(pas) == 0 :
                pas = g.getpass('Enter Password : ')
                pas1 = g.getpass('Enter Password Again For Confirmation : ')
                if pas == pas1 and len(pas) != 0 :
                    h = by.hashpw(pas.encode(), by.gensalt())
                    f1.write(h)
                    f1.close()
                    print()
                    break
                else :
                    pas = ''
                    print('\nPassword Confirmation Gone Wrong\n')
            else :
                print('\nPlease Enter A Valid Password\n')

    else :
        print('Sign In')
        print('\nFor Security Reasons')
        print('\nYou Can Enter The Password But It Wont Be Visible On The Screen. It Would Just Look Like Not Typing. But The Text Is Being Recognised.\n')
        pas = ''
        while True :
            if len(pas) == 0 :
                pas = g.getpass('Enter Password : ')
                pas1 = g.getpass('Enter Password Again For Confirmation : ')
                if pas == pas1 and len(pas) != 0 :
                    h = by.checkpw(pas.encode(), r)
                    if h :
                        print()
                        menu()
                        break
                    else :
                        pas = ''
                        print('\nPassword Wrong\n')
                else :
                    pas = ''
                    print('\nPassword Confirmation Gone Wrong\n')
            else :
                print('\nPlease Enter A Valid Password\n')

while True :
    action()
