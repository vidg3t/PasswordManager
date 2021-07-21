from __future__ import print_function#for search engine(7)
import pyAesCrypt#thats for crypting/hashing(2,5)
import smtplib#thats for email sending(3)
from email.message import EmailMessage#thats for email sending(3)
import time#just for user-friendly interface
import os#for database using
import getpass#for good passwording
import io#for search engine(7)

#default app password: 'admin'
password = 'dvayukfyukrfvyaefa'
pyAesCrypt.decryptFile('password.aes', 'password.txt', password)
fileparol = open('password.txt', 'r')
mainparol = fileparol.read()
os.remove('password.txt')

if mainparol == '':
    fileparol = open('password.txt', 'w')
    mainparol = input('Setup your password-->')
    fileparol.write(mainparol)
    fileparol.close()
    password = 'dvayukfyukrfvyaefa'
    pyAesCrypt.encryptFile('password.txt', 'password.aes', password)
    os.remove('password.txt')

def add_data(site,mail,login,password):
    f = open('data.txt', 'a')
    print('Site -','"', site,'"','Mail -','"', mail,'"', 'Login -','"', login,'"', 'Password -','"',password,'"', file = open('data.txt', 'a'))
    f.close()

def print_menu():
    print('Welcome to PasswordManager!\n 1. Add passwords\n 2. Encrypt db\n 3. Send db to email for backup\n 4. Show base\n 5. Decrypt db\n 6. Delete .txt base\n 7. Create .txt base\n 8. Find information using mail/login/site/password')

menuansw = 100

def sendmail():
    def email_alert(subject,body,to):
	    msg = EmailMessage()
	    msg.set_content(body)
	    msg['subject'] = subject
	    msg['to'] = to

        #pls, dont change account privacy settings!!!
	    user = "saintjavatest@gmail.com"
	    msg['from'] = user
	    password = "mwiicqrbyccpzgrx"

	    server = smtplib.SMTP("smtp.gmail.com", 587)
	    server.starttls()
	    server.login(user, password)
	    server.send_message(msg)
	    server.quit()

    f = open('data.txt', 'r')
    text = f.read()
    f.close()
    mail = input('Your email -->')
    email_alert('DataBackUP', text, mail)
    time.sleep(1)

while menuansw != 0:
    print_menu()
    menuansw = int(input('Choose option(press 0 for exit) --> '))
    
    if menuansw == 1:
        hmt = int(input('How many times? --> '))
        for i in range(hmt):
            s = input('Site --> ')
            m = input('Mail --> ')
            l = input('Login --> ')
            p = input('Password --> ')
            add_data(s,m,l,p)
            print('Success!')
            time.sleep(2)

    if menuansw == 2:
        passw = input('Create password for future decrypting -->')
        pyAesCrypt.encryptFile('data.txt', 'data.aes', passw)
        print('Success!')
        time.sleep(2)
        cd = input('Should we clear/delete .txt file?(c/d)')
        if cd == 'c':
            f = open('data.txt', 'w')
            f.close()
            print('Success! File "data.txt" was CLEARED. To add some information use menu')
            time.sleep(2)
        elif cd == 'd':
            os.remove('data.txt')
            print('Success! File "data.txt" was DELETED. To create new .txt use menu')

    if menuansw == 3:
        passcheck = getpass.getpass('Your password-->')
        if passcheck == mainparol:
            print('Access is allowed')
            time.sleep(2)
            sendmail()
            f = open('data.txt', 'w')
            f.close()
            print('Success!')
            time.sleep(2)
        else:
            print('Access denied')
            time.sleep(2)

    if menuansw == 4:
        passcheck = getpass.getpass('Your password-->')
        if passcheck == mainparol:
            print('Access is allowed')
            time.sleep(2)
            f = open('data.txt', 'r')
            text = f.read()
            f.close()
            print(text)
            print('Success!')
            time.sleep(2)
        else:
            print('Access denied')
            time.sleep(2)

    if menuansw == 5:
        password = getpass.getpass('Your decrypting password-->')
        try:
            pyAesCrypt.decryptFile('data.aes', 'data.txt', password)
            print('Success! Decrypted file named "data.txt".')
            time.sleep(2)
        except ValueError:
            print('Access denied')
            time.sleep(2)

    if menuansw == 6:
        passcheck = getpass.getpass('Your password-->')
        os.remove('password.txt')
        if passcheck == mainparol:
            print('Access is allowed')
            time.sleep(2)
            os.remove('data.txt')
            print('Success! File "data.txt" was deleted.')
            time.sleep(2)
        else:
            print('Access denied')    
            time.sleep(2)

    if menuansw == 7:
        passcheck = getpass.getpass('Your password-->')
        if passcheck == mainparol:
            time.sleep(2)
            print('Access is allowed')
            time.sleep(1)
            f = open('data.txt', 'w')
            f.close()
        else:
            print('Access denied')    
            time.sleep(2)

    if menuansw == 8:
        passcheck = getpass.getpass('Your password-->')
        if passcheck == mainparol:
            print('Access is allowed')
            time.sleep(2)
            word = input('Print what you know -->')
            with io.open('data.txt', encoding='utf-8') as file:
                for line in file:
                    if word in line:
                        print('Here is all information we found:\n',line)
                        time.sleep(2)
        else:
            print('Access denied')
            time.sleep(2)
