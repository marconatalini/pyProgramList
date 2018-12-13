# -*- coding: iso-8859-15 -*-

'''
Created on 11 dic 2018

@author: Marco
'''

from winreg import *
import os
import shutil

key =  OpenKey(HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, KEY_READ)
subkeynum = QueryInfoKey(key)[0]

user = os.getlogin()
pc = os.getenv("COMPUTERNAME","")
print(os.environ.keys())

#fileOutPath = os.path.join(os.environ["TEMP"],"{} programmi.txt".format(pc))
fileOutPath = os.path.join(os.getenv('HOMEDRIVE', 'C:'),os.getenv('HOMEPATH'),'Desktop',"{}_programmi.txt".format(pc))
fileOut = open(fileOutPath,"w")

for i in range(subkeynum):
    subkeyname = EnumKey(key, i)
    print(subkeyname, end=';')
    subkey = OpenKey(key, subkeyname, 0, KEY_READ)
    try:
        if QueryInfoKey(subkey)[1] != 0: #sono presenti valori
            name = QueryValueEx(subkey, "DisplayName")[0]
            print(name)
            version = QueryValueEx(subkey, "DisplayVersion")[0]
        else:
            name = ''
            version = ''
    except:
        name = ''
        version = ''
        
    fileOut.write(";".join([pc,user,subkeyname,name,version]))
    fileOut.write(os.linesep)

fileOut.close()

src = fileOutPath
dst = os.path.join("savefiles","{}_programmi.txt".format(pc))
shutil.copyfile(src, dst)

print("\n\n\n")
print("File {}_programmi.txt salvato sul DESKTOP.".format(pc))
print("Leggetelo e inviatelo a Marco via mail segnalando")
print("i programmi che già sapete essere senza licenza.")
print("Vi invito a disinstallare ciò che non è in regola e che non vi serve.")
print("A fine censimento valuteremo con la Direzione l'acquisto delle")
print("licenze necessarie.\n\n")

res = input("Premere INVIO per uscire. Grazie")

if __name__ == '__main__':
    pass