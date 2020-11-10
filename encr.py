import base64
import os

def encode(clear):
    kunci=open('key')
    key = kunci.read()
    kunci.close()
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode(''.join(enc).encode()).decode()

def decode(enc):
    kunci=open('key')
    key = kunci.read()
    kunci.close()
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr(ord(enc[i]) - ord(key_c) % 256)
        dec.append(dec_c)
    return ''.join(dec)

def efile(path):
    if path[-4:]!='.enc':
        if os.path.exists(path):
            file=open(path,'r')
            enc=file.read()
            file.close()
            file=open(path,'w')
            file.write(encode(enc))
            file.close()
            os.rename (path,path+'.enc')
            print('file dienkripsi : '+path+'.enc')

def disfile(path):
    if os.path.exists(path):
        path=path
        f=open(path,'r')
        enc=f.read()
        f.close()
    return(decode(enc))

def dfile(path):
    if os.path.exists(path+'.enc'):
        path=path+'.enc'
        file=open(path,'r')
        enc=file.read()
        file.close()
        file=open(path,'w')
        file.write(decode(enc))
        file.close()
        os.rename (path,path[:-4])
        print('file dipulihkan : '+path[:-4])
