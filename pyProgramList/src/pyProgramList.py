# -*- coding: iso-8859-15 -*-

'''
Created on 11 dic 2018

@author: Marco
'''

from winreg import *

key =  OpenKey(HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, KEY_READ)
subkeynum = QueryInfoKey(key)[0]

for i in range(subkeynum):
    subkeyname = EnumKey(key, i)
    print(subkeyname, end=';')
    subkey = OpenKey(key, subkeyname, 0, KEY_READ)
    try:
        if QueryInfoKey(subkey)[1] != 0: #sono presenti valori
            print(QueryValueEx(subkey, "DisplayName")[0], end=';')
            print(QueryValueEx(subkey, "DisplayVersion")[0])
        else:
            print()
    except:
        print("NO Name")

if __name__ == '__main__':
    pass