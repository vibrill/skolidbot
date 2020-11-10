def datapick(file_url,kolom_ke,baris_ke): #khusus data dapodik
    ket=''
    objek=''
    f=open(file_url, "r")
    #mencari header file
    for a in range(10):
        try:
            b = f.readline()
            if b[0:2].upper()=='NO':
                break
        except :
            break
    ket = b.split(',')[kolom_ke]
    f.close()
    #mencari isi data
    f=open(file_url, "r")
    for _ in range (1+a+baris_ke):
        isi=f.readline()
    f.close()
    try :
        objek = (isi.split(',')[kolom_ke])
    except :
        print('out of range err')
    return (ket,objek)

def personlist(file_url):#khusus data dapodik
    hasil=[]
    f=open(file_url, "r")
    a=0
    for _ in range (30):
        a+=1
        c=f.readline()
        try:
            x=c.split(',')[1]
            if len(x)>3:
                if a>5: #memastikan list ditulis pada baris ke lima
                    hasil.append(x);
        except:
            break
    return hasil

def simplepersonlist(file_url):#list biasa
    hasil=[]
    f=open(file_url, "r")
    for _ in range (30):
        c=f.readline()
        if c != '':
            hasil.append(c);
        else:
            break
    return hasil

#untuk mengambil data berdasarkan baris dari data simpel berisi satu data per baris
def simpeldatake(url,baris_ke):
    f=open(url, "r")
    for _ in range(baris_ke): #data baris ke tiga
        hasil=f.readline()[:-1]
    f.close()
    return hasil

#untuk mengganti pesan pada baris ke y pada file dengan url yang telah ditentukan max 13 baris
def simpledachange(pesan,url,baris_ke):
    f=open(url, "r")
    p1=f.readline()
    p2=f.readline()
    p3=f.readline()
    p4=f.readline()
    p5=f.readline()
    p6=f.readline()
    p7=f.readline()
    p8=f.readline()
    p9=f.readline()
    p10=f.readline()
    p11=f.readline()
    p12=f.readline()
    p13=f.readline()
    if baris_ke==1: p1=pesan+'\n'
    if baris_ke==2: p2=pesan+'\n'
    if baris_ke==3: p3=pesan+'\n'
    if baris_ke==4: p4=pesan+'\n'
    if baris_ke==5: p5=pesan+'\n'
    if baris_ke==6: p6=pesan+'\n'
    if baris_ke==7: p7=pesan+'\n'
    if baris_ke==8: p8=pesan+'\n'
    if baris_ke==9: p9=pesan+'\n'
    if baris_ke==10: p10=pesan+'\n'
    if baris_ke==11: p11=pesan+'\n'
    if baris_ke==12: p12=pesan+'\n'
    if baris_ke==13: p13=pesan+'\n'
    f.close()
    f=open(url,'w')
    f.write(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13)
    f.close()
    

