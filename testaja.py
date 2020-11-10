from encr import efile, dfile
import os

#enkripsifile
if os.path.exists('givenlist.txt') :
    efile('givenlist.txt')
    efile('shortskulist.txt')
else:
    dfile('givenlist.txt')
    dfile('shortskulist.txt')

'''hanya untuk test saja
import time
turu = 4
namafile = 'info.txt'
for i in range (10):
    try:
        if i % 2 == 0:
            efile(namafile)
            time.sleep(turu)
        else:
            dfile(namafile)
            time.sleep(turu)
    except:
        print('filenotfon')
'''
