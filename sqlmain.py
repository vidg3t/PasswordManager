from __future__ import print_function#for search engine(7)
import sqlite3#for database using
import pyAesCrypt#thats for crypting/hashing(tobeinstalled)
import smtplib#thats for email sending(3)
from email.message import EmailMessage#thats for email sending(3)
import time#just for user-friendly interface
import os#for database using
import io#for search engine(7)
import pyautogui#for graphics(tobeinstalled)
import sys
import sqlite3

try:
    password = 'dvayukfyukrfvyaefa'
    pyAesCrypt.decryptFile('password.aes', 'password.txt', password)
    fileparol = open('password.txt', 'r')
    mainparol = fileparol.read()
    os.remove('password.txt')
except ValueError:
    f = open('password.txt', 'w')
    f.close()
    password = 'dvayukfyukrfvyaefa'
    pyAesCrypt.encryptFile('password.txt', 'password.aes', password)
    os.remove('password.txt')
    pyAesCrypt.decryptFile('password.aes', 'password.txt', password)
    fileparol = open('password.txt', 'r')
    mainparol = fileparol.read()
    os.remove('password.txt') 

db = sqlite3.connect('pm.db')
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS users(
    site TEXT,
    mail TEXT,
    login TEXT,
    password TEXT
)''')

db.commit()

def add_data(site,mail,login,password):
    sql.execute(f"SELECT site FROM users WHERE site = '{site}'")
    sql.execute(f"INSERT INTO users VALUES(?,?,?,?)", (site,mail,login,password))
    db.commit()

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

    message = list()
    for value in sql.execute("SELECT * FROM users"):
        message.append(value)
    mail = pyautogui.prompt('Your email -->')
    email_alert('DataBackUP', str(message), mail)

menuansw = '100'

if mainparol == '':
    fileparol = open('password.txt', 'w')
    mainparol = pyautogui.prompt(text = 'Setup your password(app will stop and u will need to reboot it after)-->')
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
            menuansw = pyautogui.confirm(text = 'Welcome to PasswordManager', title = 'Menu', buttons = ['Exit','Add passwords','Encrypt db','Send db to email for backup','Show base','Decrypt db','Find information using mail/login/site/password',])

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
                pyAesCrypt.encryptFile('pm.db', 'pm.aes', passw)
                os.remove('pm.db')
                pyautogui.alert(text = 'Success!', title = 'Access')
                
            if menuansw == 'Send db to email for backup':                    
                sendmail()
                pyautogui.alert(text = 'Success!', title = 'Access')
                    
            if menuansw == 'Show base':
                message = list()
                for value in sql.execute("SELECT * FROM users"):
                    message.append(value)
                pyautogui.alert(text = message)

            if menuansw == 'Decrypt db':
                passcheck = pyautogui.password(text = 'Your decryption password', title = 'Password')
                try:
                    pyAesCrypt.decryptFile('pm.aes', 'pm.db', passcheck)
                    pyautogui.alert(text = 'Success! Decrypted file named "pm.db".', title = 'Access')
                    
                except ValueError:
                    pyautogui.alert(text = 'Access denied', title = 'Access')
                    
            if menuansw == 'Find information using mail/login/site/password':
                    
                word = pyautogui.prompt(text = 'Print what you know -->', title = 'Information')
                message = list()
                for value in sql.execute("SELECT * FROM users"):
                    message.append(value)
                    if value[0] == word or value[1] == word or value[2] == word or value[3] == word:
                        pyautogui.alert(text = value)

    else:
        pyautogui.alert(text = 'Access denied', title = 'Authentification')
