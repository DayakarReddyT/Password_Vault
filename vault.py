# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:04:38 2020

@author: Daya
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:49:26 2020

@author: Daya


import keyring as key
import pyperclip

print(key.get_password('t3est','daya'))
"""


import keyring
import pyperclip
from passlib.hash import pbkdf2_sha256
import os
from os import sys
import getpass
import time 
from colorama import Fore, Back, Style
from keyring.backends import Windows
keyring.set_keyring(Windows.WinVaultKeyring())

user_file_path=os.getcwd()+'\\'+'login_details.txt'
vault_dict={}
login=False 
first=False




welcome='''
                        __      __          _ _
                        \ \    / /	   | | |
                         \ \  / / _ _ _   _| | |_
    Welcome to  The       \ \/ / _ ` | | | | | __|
                           \  / (_|  | |_| | | |_
                            \/ \__,__|\__,_|_|\__|
    
'''


# This is print the Entry text like we type in keyboard .

for line,i in zip(welcome.split('\n'),range(len(welcome.split('\n')))):
    
    print()
    if(line==''):
        continue
    for char in list(line):
        if(i==4):
            speed=(1./10)
        else:
            speed=(1./80)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)



def get_pasword():
    while(True):
        p= getpass.getpass(prompt='Enter your Password    : ')
        p1=getpass.getpass(prompt='ReEnter your Password  : ')
        if(p==p1):
            break
        else:
            print(Fore.RED+Style.BRIGHT+"Password Mimatch , Pleae Enter it again "+Style.RESET_ALL) 
    orig=p
    return orig,encrypt(p)


def encrypt(value):
    pb_256=pbkdf2_sha256.hash(value)
    
    
    return pb_256
    
def update_server_file(li):
    remove_cont=open(os.getcwd()+'\\'+'server_names.sekret','w')
    remove_cont.close()
    
    update_cont=open(os.getcwd()+'\\'+'server_names.sekret','a')
    for item in li:
        update_cont.write(item)
        update_cont.write('\n')
    update_cont.close()
 
try:

    with(open(user_file_path,'r')) as user_file:
        file=user_file.read()    
        if(file == ''):
            print()
            print("  Please Provide the below detials to Registrer ")
            file2=open(user_file_path,'w+')
            user=input('Enter your user name    : ')
            while(True):
                pass1=getpass.getpass(prompt='Enter your Password        : ')
                pass2=getpass.getpass(prompt='Enter your Password Again  : ')
                if(pass1==pass2):
                    hash_pass=pbkdf2_sha256.hash(pass1)              
               
                    file2.write(user+','+hash_pass)
                    keyring.set_password('py_vault',user,hash_pass)
                    file2.close()
                    login=True
                    first=True
                    break
                else:
                    print(Fore.RED+'Password Mismatch , please enter it again'+Style.RESET_ALL)
                  
            
        else:
            user,p=file.split(',')[:2]
            print('\n\n\tHello {0} , Please Enter your password \n'.format(user))
            
            for i in range(3):
                password=getpass.getpass(prompt='Password : ')
                if(  ( pbkdf2_sha256.verify(password,p) ) and (keyring.get_password('py_vault',user)==password)):
                    os.system('cls')
                    login=True
                    break
            
            if(login==False):
                print(Fore.RED+Style.BRIGHT+'Loging Failed for 3 Atempts , Closing the session '+Style.RESET_ALL)
                user_file.close()
                
        
    while(login):
        
        print()
        print(Fore.GREEN+Style.BRIGHT+"Welcome {0} , Password Vault is Your's Now {1}".format(user,Style.RESET_ALL))
        
        print()
        print("\t 1 ->  Add Password to Vault ")
        print("\t 2 ->  Get Password from Vault")
        print("\t 3 ->  Update Password from Vault")
        print("\t 4 ->  Delete Password in  Vault")
        print()
        
           
        try:
            
            
            server_file=os.getcwd()+'\\'+'server_names.sekret'
            
            while(True):
                try:
                    choice=int(input('Enter Your Choice : '))
                    print()
                    if(choice<1 or choice >4):
                        print(Fore.RED+'Please Choose the option from the displayed only '+Style.RESET_ALL)
                        print()
                        
                    else:
                        break
                except ValueError :
                    print(Fore.RED+'  Invalid Input , Please try again '+Style.RESET_ALL)
                    
            
            
            if(choice==1):       
                if(first==True):
                    # info about first time details 
                    pass
                    
                server=input('Enter Website/Server Name : ')
                user=input('Enter user name           : ')
                             
                orig,pa=get_pasword()
                server_add=open(server_file,'a')
                try:
                    server_add.write(server+','+user+','+pa)
                    server_add.write('\n')
                    keyring.set_password(server,user,orig)
                    server_add.close()
                    print()
                    print(Fore.GREEN+Style.BRIGHT+'\t Password Added to the Vault '+Style.RESET_ALL )
                except Exception:
                    print()
                    print(Fore.RED+' Failed to Add Password to Vault '+Style.RESET_ALL)
            elif(choice==2 or choice==3 or choice==4):
                
                
                if(os.path.isfile(server_file)==False):
                    print('Server Details file is not available ')
                    print(Fore.RED+'Someone Deleted/Moved the "server_names.sekret" file  \n  OR \n If this is your first time , pleaes create a file with Name server_names and Extension as sekret : '+Style.RESET_ALL)
                    break
                
                             
                server_details=open(os.getcwd()+'\\'+'server_names.sekret','r').read().split('\n') 
                
                
                        
                if(len(server_details[0])==0):
                    print(Fore.RED+"\t No Data Available in Vault "+Style.RESET_ALL)
                else:
                    
                    
                
                
                    
                    if('' in server_details):
                        server_details.remove('')
                    
                    for item in server_details:
                                            
                        item=item.split(',')[:3]
                        
                        if(item[0] in vault_dict.keys()):
                            vault_dict[item[0]][item[1]]=item[2]
                        else:
                            vault_dict[item[0]]={item[1]:item[2]}
                    
                    print(Fore.YELLOW+'\tChoose the Server/Website Name you want to get Password\n'+Style.RESET_ALL)
                    
                    keys=list(vault_dict.keys())
                    if(len(keys)%2==0):
                        
                        for i in range(0,len(keys),2):
                            print(f"{Fore.MAGENTA}\t{i+1} -> {keys[i]}\t\t\t {i+2} -> {keys[i+1]}{Style.RESET_ALL}")
                    elif(len(keys)==1):
                        print(f"\t 1 -> {keys[0]}")
                    else:
                        
                        for i in range(0,len(keys)-1,2):
                            print(f"{Fore.MAGENTA}\t{i+1} -> {keys[i]}\t\t\t {i+2} -> {keys[i+1]}{Style.RESET_ALL}")
                        print(f"{Fore.MAGENTA}\t{i+3} -> {keys[i+2]}{Style.RESET_ALL}")
                    while(True):
                        try:
                            print()
                            serv_choice=int(input('Enter the Choice : '))
                            if(serv_choice<=0 or serv_choice>len(keys)):
                                print(Fore.RED+'Please Choose the option from the displayed only '+Style.RESET_ALL)
                            else:
                                break
                        except ValueError:
                            print('Invalid Input , Please try Again !!')
                            
                    server=keys[serv_choice-1]                
                    user_keys=list(vault_dict[server].keys())
                    print(Fore.YELLOW+'\n\t\t Please Choose the User Name \n'+Style.RESET_ALL)
                    
                    for i in range(len(user_keys)):
                        print(f"{Fore.MAGENTA}\t {i+1} -> {user_keys[i]}{Style.RESET_ALL}")
                    
                    while(True):
                        try:
                            print()
                            user_choice=int(input('Enter the Choice : '))
                            if(user_choice<=0 or user_choice>len(user_keys)):
                                print(Fore.RED+'Please Choose the option from the displayed only '+Style.RESET_ALL)
                            else:
                                break
                        except ValueError:
                            print('Invalid Input , Please try Again !!')
                    
                    
                    user=user_keys[user_choice-1]
                    if(choice==2):
                        value=vault_dict[server][user]
                        
                        psd=keyring.get_password(server,user)                   
                                              
                        if(pbkdf2_sha256.verify(psd,value)):
                            
                            pyperclip.copy(psd)
                            print()
                            print(Fore.GREEN+Style.BRIGHT+'\t The Password is copied to clipboard \n'+Style.RESET_ALL)
                            exi=input('\n Enter any Key to Exit : ')
                            
                        else:
                            
                            print(Fore.RED+" \n  Somebody has CHANGED password for {0} \n\n   Don't worry They didn't SEE your Password {1}".format(user,Style.RESET_ALL))
                            exi=input('\n Enter any Key to Exit : ')
                   
                    elif(choice==3):
                        print()
                        print('Please Enter the New Password')
                        orig,p=get_pasword()
                        vault_dict[server][user]=p
                        sub_string=server+','+user
                        for ele in range(len(server_details)):
                            if sub_string in server_details[ele]:
                                
                                server_details[ele]=sub_string+','+p
                        try: 
                            update_server_file(server_details)
                            keyring.delete_password(server,user)
                            keyring.set_password(server,user,orig)
                            print(Fore.GREEN+"\n\t\t Password Updated Successfully "+Style.RESET_ALL)
                            exi=input('\n Enter any Key to Exit : ')
                            break
                        except Exception :
                            print()
                            print(Fore.RED+' Failed to Update the Password , Please try Again '+Style.RESET_ALL)
                            exi=input('\n Enter any Key to Exit : ')
                            
                       
                    elif(choice==4):
                        try:
                            sub_string=server+','+user
                            for ele in range(len(server_details)):
                                if sub_string in server_details[ele]: 
                                    
                                    server_details.pop(ele)
                                    break
                            update_server_file(server_details)
                            keyring.delete_password(server,user)                   
                            
                            print(Fore.GREEN+"\n\t Password Deleted Successfully from the Vault "+Style.RESET_ALL)
                            exi=input('\n Enter any Key to Exit : ')
                            break
                        except Exception as e:
                            print()
                            print(Fore.RED+' Failed to Delete the Password , Please try again '+Style.RESET_ALL)
                            exi=input('\n Enter any Key to Exit : ')
            
            break
        
        except ValueError:
            print('Invalid Input , Please try Again !!')
except Exception as e:
    print(e)
    exi=input('Enter any key to exit ')
'''
import os

gt.write('Netflix,Daya,$pbkdf2-sha256$29000$UKp1LoXQWgtBKCXkvLe2lg$99cOQrcj9uwy8tytPcslaSpHRFl9ZJS5PIZ58OBgclQ')


open(os.getcwd()+'\\'+'server_names.sekret','a').write('\n')

open(os.getcwd()+'\\'+'server_names.sekret','a').write('Email,Daya,$pbkdf2-sha256$29000$y5mT0lpL6T3nXMuZEwLg/A$AAbXl1h58v/pffgqt6Q6P5E7oQo03wGc64OJs14dOmo')


open(os.getcwd()+'\\'+'server_names.sekret','r').read()
'''


