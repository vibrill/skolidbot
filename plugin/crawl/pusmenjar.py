import requests
from bs4 import BeautifulSoup
import time
import os
import datetime
import urllib.request, urllib.error

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
tahun = str(datetime.datetime.now().year)
tahunlalu =  str(int(datetime.datetime.now().year)-1)

filenya=[]
linknya=[]
for numa in range(3):
    page = requests.get("https://pusmenjar.kemdikbud.go.id/publikasi/?halaman="+str(numa+1), headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    x = soup.find("tbody")
    y = x.find_all("tr")
    for num in range(len(y)):
        publikasi = y[num].find_all('td')
        l = y[num].find('a')
        link = l['href']
        linknya.append('https://pusmenjar.kemdikbud.go.id'+link)
        for ang in range(len(publikasi)):
            filenya.append(publikasi[ang].text)
# print(filenya)
# print(linknya)
tahun=[]
judul=[]
kategori=[]
# counter=[]
item=5
for num in range(len(filenya)):
    if num==0 or num%5==0:
        tahun.append(filenya[num])
    if num==1 or num%5==1:
        judul.append(filenya[num])
    if num==2 or num%5==2:
        kategori.append(filenya[num])
#     if num==4 or num%5==4:
#         counter.append(filenya[num])
print(tahun)
print(judul)
print(kategori)
# print(counter)
print(linknya)
listall=[]
stringall=''
for num in range(len(judul)):
    dicty={'tahun':tahun[num],'judul':judul[num],'kategori':kategori[num],'url':linknya[num]}
    listall.append(dicty)
    stringall+='tahun : '+tahun[num]+'\n'+'judul : '+judul[num]+'\n'+'kategori : '+kategori[num]+'\n'+'url : '+linknya[num]+'\n\n'
    
# print(stringall)
try:
    f=open('pusmenjar.txt','r')
    a=f.read()
    f.close()
    if a==stringall:
        print('file terdeteksi, tidak ada perubahan')
    else:
        f=open('pusmenjar.txt','w')
        f.write(stringall)
        f.close()
        print('file terdeteksi, ada perubahan, file diupdate')
except:
    f=open('pusmenjar.txt','w')
    f.write(stringall)
    f.close()
    print('file tidak terdeteksi, file telah dibuat')