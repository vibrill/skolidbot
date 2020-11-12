import random
from encr import disfile, encode

def ranstring(length):
    password = 'QWERTYUPASDFGHJKLZXCVBNM2345678923456789'
    result = ''.join(random.choice(password) for i in range(length))
    return result

def createOps(kode,namas):
    a='OPS'+kode+'-'+ranstring(5)+'-'+ranstring(5)+'-'+ranstring(5)+'-'+ranstring(5)+'\n'
    b=disfile('shortskulist.txt.enc')
    print(b)
    b+=a
    print(b)
    f=open('shortskulist.txt.enc','w')
    f.write(encode(b))
    f.close()
    c=disfile('givenlist.txt.enc')
    c+=kode+'_'+namas.replace(' ','_')+'\n'
    print(c)
    f=open('givenlist.txt.enc','w')
    f.write(encode(c))
    f.close()
    print(b)
    return a[:-1]

def delOps(kode):
    b=''
    a=disfile('shortskulist.txt.enc').replace('\n',' \n')
    a=a.split('\n')
    for x in range(len(a)):
        if a[x][3:7]==kode:
            a.pop(x)
            break
    print(b.join(a).replace(' ','\n'))
    f=open('shortskulist.txt.enc','w')
    f.write(encode(b.join(a).replace(' ','\n')))
    f.close()
    
    b=''
    a=disfile('givenlist.txt.enc').replace('\n',' \n')
    a=a.split('\n')
    for x in range(len(a)):
        if a[x][:4]==kode:
            a.pop(x)
            x='skolidbot/'+str(a[x])[5:]
            if len(x)>11:
                try:
                    import shutil
                    shutil.rmtree(x)
                except:
                    print('no folder founded')
            break
    print(b.join(a).replace(' ','\n'))
    f=open('givenlist.txt.enc','w')
    f.write(encode(b.join(a).replace(' ','\n')))
    f.close()