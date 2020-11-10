def alljudul():
    f=open('plugin/pusmenjar.txt','r')
    text=f.read()
    f.close()
    listfile=text.split('\n')
    listfile=[x for x in listfile if x.startswith('judul')]
    listal=[]
    for item in listfile:
        listal.append(item.replace('judul : ',''))
    return listal

def allkategori():
    f=open('plugin/pusmenjar.txt','r')
    text=f.read()
    f.close()
    listfile=text.split('\n')
    listfile=[x for x in listfile if x.startswith('kategori')]
    listal=[]
    for item in listfile:
        listal.append(item.replace('kategori : ',''))
    return listal

def alltahun():
    f=open('plugin/pusmenjar.txt','r')
    text=f.read()
    f.close()
    listfile=text.split('\n')
    listfile=[x for x in listfile if x.startswith('tahun')]
    listal=[]
    for item in listfile:
        listal.append(item.replace('tahun : ',''))
    return listal

def allurl():
    f=open('plugin/pusmenjar.txt','r')
    text=f.read()
    f.close()
    listfile=text.split('\n')
    listfile=[x for x in listfile if x.startswith('url')]
    listal=[]
    for item in listfile:
        listal.append(item.replace('url : ',''))
    return listal

def tahun(thn):
    f=open('plugin/pusmenjar.txt','r')
    text=f.read()
    f.close()
    listfile=text.split('\n')
    listfile=[x for x in listfile if x.endswith(thn) and len(x)<13]
    listal=[]
    for item in listfile:
        listal.append(item.replace('tahun : ',''))
    return listal

def judurl():
    a=alljudul()
    b=allurl()
    e=alltahun()
    c=[]
    for num in range(len(a)):
        c.append(a[num]+' : '+e[num]+'\n'+b[num]+'\n\n')
    d=''
    d=d.join(c)
    return d

def tahjudurl(thn):
    a=alljudul()
    b=allurl()
    c=alltahun()
    d=[]
    for num in range(len(c)):
        if c[num]==thn:
            d.append(a[num]+'\n'+b[num]+'\n\n')
    e=''
    e=e.join(d)
    return e

def katset():
    a=allkategori()
    b=set()
    for item in a:
        b.add(item)
    c=list(b)
    c.sort()
    return c

def katjudurl(index):
    a=alljudul()
    b=allurl()
    c=allkategori()
    d=katset()
    e=[]
    for num in range(len(c)):
        if c[num]==d[index]:
            e.append(a[num]+'\n'+b[num]+'\n\n')
    f=''
    f=f.join(e)
    return f
    
