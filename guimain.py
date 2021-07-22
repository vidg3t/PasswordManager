from __future__ import print_function#for search engine(7)
import pyAesCrypt#thats for crypting/hashing(2,5)
import smtplib#thats for email sending(3)
from email.message import EmailMessage#thats for email sending(3)
import time#just for user-friendly interface
import os#for database using
import getpass#for good passwording
import io#for search engine(7)
import pyautogui#for graphics
import sys

password = 'dvayukfyukrfvyaefa'
pyAesCrypt.decryptFile('password.aes', 'password.txt', password)
fileparol = open('password.txt', 'r')
mainparol = fileparol.read()
os.remove('password.txt')

def add_data(site,mail,login,password):
    f = open('data.txt', 'a')
    print('Site -','"', site,'"','Mail -','"', mail,'"', 'Login -','"', login,'"', 'Password -','"',password,'"', file = open('data.txt', 'a'))
    f.close()

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
    mail = pyautogui.prompt('Your email -->')
    email_alert('DataBackUP', text, mail)

menuansw = '100'

if mainparol == '':
    fileparol = open('password.txt', 'w')
    mainparol = pyautogui.prompt(text = 'Setup your password-->')
    fileparol.write(mainparol)
    fileparol.close()
    password = 'dvayukfyukrfvyaefa'
    pyAesCrypt.encryptFile('password.txt', 'password.aes', password)
    os.remove('password.txt')
else:
    passcheck = pyautogui.password(text = 'Your password', title = 'Password')
    if passcheck == mainparol:
        pyautogui.alert(text = 'Access is allowed!', title = 'Authentification')

        while menuansw != 'Exit':
            menuansw = pyautogui.confirm(text = 'Welcome to PasswordManager', title = 'Menu', buttons = ['Exit','Add passwords','Encrypt db','Send db to email for backup','Show base','Decrypt db','Delete .txt base','Create .txt base','Find information using mail/login/site/password',])

            if menuansw == 'Add passwords':
                hmt = pyautogui.prompt('How many times? --> ')
                for i in range(int(hmt)):
                    s = pyautogui.prompt(text = 'Site --> ', title = 'Site')
                    m = pyautogui.prompt(text = 'Mail --> ', title = 'Mail')
                    l = pyautogui.prompt(text = 'Login --> ', title = 'Login')
                    p = pyautogui.prompt(text = 'Password --> ', title = 'Password')
                    add_data(s,m,l,p)
                    pyautogui.alert(text = 'Success!', title = 'Access')
                    

            if menuansw == 'Encrypt db':
                passw = pyautogui.prompt(text = 'Create password for future decrypting -->', title = 'password')
                pyAesCrypt.encryptFile('data.txt', 'data.aes', passw)
                pyautogui.alert(text = 'Success!', title = 'Access')
                
                cd = pyautogui.confirm(text = 'Should we clear/delete .txt file?', title = 'CorD', buttons = ['Clear', 'Delete'])
                if cd == 'Clear':
                    f = open('data.txt', 'w')
                    f.close()
                    pyautogui.alert(text = 'Success! File "data.txt" was CLEARED. To add some information use menu', title = 'Access')
                    
                elif cd == 'Delete':
                    os.remove('data.txt')
                    pyautogui.alert(text = 'Success! File "data.txt" was DELETED. To create new .txt use menu',title = 'Access')

            if menuansw == 'Send db to email for backup':                    
                sendmail()
                f = open('data.txt', 'w')
                f.close()
                pyautogui.alert(text = 'Success!', title = 'Access')
                    

            if menuansw == 'Show base':
                try:
                    f = open('data.txt', 'r')
                    text1 = f.read()
                    f.close()
                    pyautogui.alert(text = text1, title = 'Base')
                except FileNotFoundError:
                    creorgo = pyautogui.confirm(text = 'There is no base in our directory, you can create new, using our menu', title = 'Issue', buttons = ['Create db', 'Go to menu'])
                    if creorgo == 'Create db':
                        f = open('data.txt', 'w')
                        f.close()
                        pyautogui.alert(text = 'Success! File "data.txt" was created.', title = 'Success')
                    


            if menuansw == 'Decrypt db':
                passcheck = pyautogui.password(text = 'Your decryption password', title = 'Password')
                try:
                    pyAesCrypt.decryptFile('data.aes', 'data.txt', password)
                    pyautogui.alert(text = 'Success! Decrypted file named "data.txt".', title = 'Access')
                    
                except ValueError:
                    pyautogui.alert(text = 'Access denied', title = 'Access')
                    

            if menuansw == 'Delete .txt base':
                try:
                    os.remove('data.txt')
                    pyautogui.alert(text = 'Success! File "data.txt" was deleted.', title = 'Success')                    
                except FileNotFoundError:
                    sameshit = pyautogui.confirm(text = 'There is no base in our directory, you can create new, using our menu', title = 'Issue', buttons = ['Create db','Go to menu'])
                    if sameshit == 'Create db':
                        f = open('data.txt', 'w')
                        f.close()
                        pyautogui.alert(text = 'Success! File "data.txt" was created.', title = 'Success')

            
            if menuansw == 'Create .txt base':                     
                f = open('data.txt', 'w')
                f.close()
                pyautogui.alert(text = 'Success! File "data.txt" was created.', title = 'Success')                    

            if menuansw == 'Find information using mail/login/site/password':
                pyautogui.alert(text = 'Access is allowed', title = 'Access')
                    
                word = pyautogui.prompt(text = 'Print what you know -->', title = 'Information')
                with io.open('data.txt', encoding='utf-8') as file:
                    for line in file:
                        if word in line:
                            pyautogui.alert(text = f'Here is all information we found:\n{line}')
                        else:
                            pyautogui.alert(text = 'There is nothing we could find')

    else:
        pyautogui.alert(text = 'Access denied', title = 'Authentification')
                    
