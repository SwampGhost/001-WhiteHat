import string
import binascii
import time 

#--- original ---
def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)
#-----

def encrypt(char):
 #   print ("testing math") 
    return(123 * char + 18) % 256

def decipher_w_loops(msg):
    og_msg=[]
    for byte in msg:
  #      print ('uncheck char is: ', byte)
        for i in range (1,129):
  #              #print ('cheking encrypt compare')
                encrypted = encrypt(i)
                if encrypted == byte:
  #                 print ('passed char is: ', chr(i))
                    og_msg.append(chr(i))

    return ''.join(og_msg)

with open ('msg.enc') as f:
    msg = binascii.unhexlify(f.read())
    print ('file content: ', msg)

    start = time.perf_counter()
    deciphered_w_loops = decipher_w_loops(msg)
    stop = time.perf_counter()
    loop_time= (stop - start) * 1000

print ('the message: ', deciphered_w_loops)

```