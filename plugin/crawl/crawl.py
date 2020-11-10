import requests
from bs4 import BeautifulSoup
import time
import os
import datetime
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
tahun = str(datetime.datetime.now().year)
tahunlalu =  str(int(datetime.datetime.now().year)-1)

#mengambil data dapodik di bloger
page = requests.get("https://verildatacrawl.blogspot.com/2020/10/blog-post.html", headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
x = soup.find("div", id="post-body-896453645053189824")
dapo = x.get_text()
dapolist=[]
for item in dapo.split('- '):
    if item!='\n' and item[:1]=='S':
        dapolist.append('- '+item)
dapo=''
dapo=dapo.join(dapolist)
dapo=dapo[2:].replace('- ','\n\n')
dapo=dapo.replace(' : ','\nLast Sync : ')
dapo=dapo.replace(tahun, tahun+'\nPada Pukul : ')
dapo=dapo.replace(tahunlalu, tahunlalu+'\nPada Pukul : ')
#cek apakah ada perubahan data
# print(os.path.exists('dapodik.txt'))
if os.path.exists('dapodik.txt')==False:
    print('file dapodik tidak ditemukan, file akan dibuat sekarang')
    f=open('dapodik.txt','w')
    f.write(dapo)
    f.close()
else:
    print('file dapodik ditemukan, mulai membandingkan data')
    f=open('dapodik.txt','r')
    test=f.read()
    f.close()
    if test==dapo:
        print('tidak ada perubahan data')
    else:
        print('ada perubahan data, file diupdate')
        f=open('dapodik.txt','w')
        f.write(dapo)
        f.close()

# print(dapolist)
# print(dapo)

page = requests.get("https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Kota%20Pasuruan&AreaID=501297&Prov=12", headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
x = soup.find("div", class_="prakicu-kabkota tab-v1 margin-bottom-30")
# alpane=[x] + x.find_next_siblings('div')
cuacajam=x.find_all("div",class_="cuaca-flex-child")
panel=[]
tanggalset=[]
tanggal=[]
jam=[]
cuaca=[]
kelembapan=[]
kecangin=[]
arangin=[]
suhu=[]
for item in cuacajam:
    pn=item.parent.parent['id']
    y=item.find('div', class_='service-block clearfix')
    jam.append(y.find('h2', class_='kota').get_text().replace('\xa0',' '))
    suhu.append(y.find('h2', class_='heading-md').get_text())
    a=y.find_all('p')[0].get_text()
    b=y.find_all('p')[1].get_text()
    c=y.find_all('p')[2].get_text().replace('\xa0',' ').replace('km/jam','km/jam dari ')
    #d=y.find_all('p')[3].get_text()
    panel.append(pn)
    cuaca.append(a)
    kelembapan.append(b)
    kecangin.append(c)

hari=x.find_all('li')
for item in hari:
    tanggalset.append(item.get_text())
for x in range(len(panel)):tanggal.append(x)
for x in range(len(panel)):
    a=x-1
    if panel[a]=='TabPaneCuaca1': tanggal[a]=tanggalset[0]
    if panel[a]=='TabPaneCuaca2': tanggal[a]=tanggalset[1]
    if panel[a]=='TabPaneCuaca3': tanggal[a]=tanggalset[2]
    if panel[a]=='TabPaneCuaca4': tanggal[a]=tanggalset[3]
    if panel[a]=='TabPaneCuaca5': tanggal[a]=tanggalset[4]
    if panel[a]=='TabPaneCuaca6': tanggal[a]=tanggalset[5]
    if panel[a]=='TabPaneCuaca7': tanggal[a]=tanggalset[6]
        
# 
# print(tanggalset)
# print(panel)
# print(len(panel))
# 
# print(tanggal)
# print(len(tanggal))
# print(jam)
# print(len(jam))
# print(cuaca)
# print(len(cuaca))
# print(kelembapan)
# print(len(kelembapan))
# print(kecangin)
# print(len(kecangin))
dafcu=[]

for x in range(len(panel)-1):
    dafcu.append(f'Cuaca Kota Pasuruan {tanggal[x]} pada jam {jam[x]} akan {cuaca[x]} dengan suhu mencapai {suhu[x]}, kelembaban sebesar {kelembapan[x]} dan kecepatan angin sebesar {kecangin[x]}')
#     print(f'Cuaca Kota Pasuruan {tanggal[x]} pada jam {jam[x]} akan {cuaca[x]} dengan suhu mencapai {suhu[x]}, kelembaban sebesar {kelembapan[x]} dan kecepatan angin sebesar {kecangin[x]} \n')
    
sdafcu=''
sdafcu=sdafcu.join(dafcu)
sdafcu=sdafcu.replace('Cuaca Kota','\nCuaca Kota')[1:]

if os.path.exists('cuaca.txt')==False:
    print('file cuaca tidak ditemukan, file akan dibuat sekarang')
    f=open('cuaca.txt','w')
    f.write(sdafcu)
    f.close()
else:
    print('file cuaca ditemukan, mulai membandingkan data')
    f=open('cuaca.txt','r')
    test=f.read()
    f.close()
    if test==sdafcu:
        print('tidak ada perubahan data')
    else:
        print('ada perubahan data, file diupdate')
        f=open('cuaca.txt','w')
        f.write(sdafcu)
        f.close()

