import pandas as pd
import os
import telepot
import time
from datasearch import datapick, personlist, simpeldatake, simpledachange, simplepersonlist
from randomstring import ranstring, createOps, delOps
from arsiper import arsipkan
from shutil import copyfile
from encr import efile, dfile, decode, encode, disfile
import openpyxl
from unmersis import unmersis, delearn
from datetime import datetime, date, timedelta
import subprocess
import wikis
import pijar

command=''
def cekDA():
    u1='plugin/dapodik.txt'
    u2='plugin/dapotest.txt'
    beda=[]
    with open(u1) as f:
        a=f.read()
        a=a.split('\n\n')
    with open(u2) as f:
        b=f.read()
        b=b.split('\n\n')
    for item in a:
        if item not in b:
            beda.append(item+'_x_')
    return beda

# def cekcounter():
#     import random
#     while True:
#         time.sleep(7) #give main thread finish the algorithm if it in startup process
#         a=cekDA()
#         if a!=[]:
#             global command
#             command =
#             print('send command 1')
#         
#         print('send command 2')
#         time.sleep(300) #3600 = 1 hour, 300 = 5 minutes
# 
# import threading
# t = threading.Thread(target=cekcounter, daemon=True) #cekcounter
# t.start()

#my chat id writen in myID file
with open('myID') as f:
    myID=int(f.read())
    

def handle(msg):
#     print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg,'chat')
    #dibawah hiden for editing only
    #print(content_type, chat_type, chat_id)
#------------------------------------------------------------------------
    if content_type == 'text': #jika pesan berupa text
        command = msg['text']
        log=[]
        if os.path.exists('user/'+str(chat_id)):
            if simpeldatake('user/'+str(chat_id),6)!='empty':
                print(content_type+' from '+simpeldatake('user/'+str(chat_id),6)+' : '+command)
                log.append(content_type+' from '+simpeldatake('user/'+str(chat_id),6)+' : '+command+'\n')
                if len(log)>200:
                    l=''
                    with open('logfile','w') as f:
                        f.write(l.join(log))
                    log=[]
            else:
                print (content_type+' from '+str(chat_id)+' : '+command)
                log.append(content_type+' from '+str(chat_id)+' : '+command+'\n')
                if len(log)>200:
                    l=''
                    with open('logfile','w') as f:
                        f.write(l.join(log))
                    log=[]
        else:
            print (content_type+' from '+str(chat_id)+' : '+command)
            log.append(content_type+' from '+str(chat_id)+' : '+command+'\n')
    else:
        command = ('empty')
#------------------------------------------------------------------------    
    
    if command.lower() == 'cekupdate':
        a=cekDA()
        with open('ops.list','r') as f:
            c=f.read()
            c=c.split('\n')
            d=''
            for userid in c:
                if userid!='':
                    userid=int(userid)
                    bot.sendMessage(userid,'Update sinkronisasi terbaru :\n\n'+d.join(a).replace('_x_','\n\n')+'klik /menu untuk mengakses menu utama')
        with open('plugin/dapodik.txt','r') as f:
            b=f.read()
        with open('plugin/dapotest.txt','w') as f:
            f.write(b)
    
    if command == '/start':
        if os.path.exists('user/'+str(chat_id)):
            bot.sendMessage(chat_id,'user telah terdaftar\ntekan /menu untuk mengakses menu utama')
        else:
            #membuat file user
            print('membuat file identitas user '+str(chat_id))
            f=open('user/'+str(chat_id),'w+')
            for _ in range (13):
                f.write('empty\n')
            #print('selesai membuat file user')
            f.close()
            bot.sendMessage(chat_id,'masukkan kode yang telah anda terima\ncontoh : INICNTH-789SD-45SDE-DER54-THT41')
#------------------------------------------------------------------------    
    if command == 'INICNTH-789SD-45SDE-DER54-THT41':
        bot.sendMessage(chat_id,'ini hanya contoh bos, pake kode yang telah diberikan OPS atau Admin.')
#------------------------------------------------------------------------    
    if command[0:3].upper() == 'OPS' and len(command)==31:
        #decode ini file givenlist dan shortskulist
        givenlist=disfile('givenlist.txt.enc')
        sslist=disfile('shortskulist.txt.enc')
        #mengubah string hasil decode menjadi list
        givenlist= givenlist.split('\n')
        sslist= sslist.split('\n')
#         print(sslist)
        #mencocokan command dengan list shortskulist
        a=0
        for kode in sslist:
            a+=1
            if command==kode:
                #--------set ops.list---------
                #membaca file list OPS.
                listops=set()
                f= open('ops.list')
                ax=f.read()
                f.close()
                
                ax=ax.split('\n')
                for item in ax:
                    if item != '':
                        listops.add(item)
                #mengupdate file list OPS
                ad=str(chat_id)
                listops.add(ad)
                listops=list(listops)
                b=''
                
                for item in listops:
                    b+=item+'\n'
                
                f= open('ops.list','w')
                f.write(b)
                f.close()
                #------eo ops.list-----------    
                idt = command[:3] # mengambil ID OPS atau NON
                sekl=command[3:7] # mengambil ID sekolah
                namasd=''
                for sekolah in givenlist:
                    if sekl==sekolah[:4]:
                        namasd=sekolah[5:]
                        simpledachange(sekl,'user/'+str(chat_id),5)
                        print (namasd)
                        print (sekl)
                        break
                
                #print('post count')
                #mencatat id pass dan SD
                simpledachange('valid','user/'+str(chat_id),1)
                simpledachange(idt,'user/'+str(chat_id),2)
                simpledachange(encode(command),'user/'+str(chat_id),3)
                simpledachange(namasd,'user/'+str(chat_id),4)
                #membuat folder sekolah
                if os.path.exists('skolidbot/'+namasd):
                    #memastikan hanya satu user_id / OPS yang dapat mengakses folder sekolah
                    if os.path.exists('skolidbot/'+namasd+'/'+str(chat_id)):
                        bot.sendMessage(chat_id,'sekolah telah didaftarkan')
                        simpledachange('valid','user/'+str(chat_id),1)
                    else:
                        bot.sendMessage(chat_id,'anda sudah terdaftar OPS di sekolah lain, anda tidak memiliki wewenang menggunakan password OPS ini')
                        simpledachange('blocked','user/'+str(chat_id),1)
                        f=open('user/blocklist','a+')
                        f.write(str(chat_id))
                        f.close()
                elif simpeldatake('user/'+str(chat_id),1)=='valid':
                    print (f'folder {namasd} dibuat')
                    os.mkdir('skolidbot/'+namasd) 
                    simpledachange('valid','user/'+str(chat_id),1)
                    f=open('skolidbot/'+namasd+'/'+str(chat_id),'w')
                    f.write('OPS')
                    f.close()
                if simpeldatake('user/'+str(chat_id),1)=='valid':
                    bot.sendMessage(chat_id,'''
silahkan upload di sini tiga file Dapodik berikut:
- daftar guru,
- daftar tendik, dan
- daftar siswa,
File tersebut akan digunakan sebagai database untuk melayani request data dari lembaga anda.
''')
                break
                
            if a==len(sslist):
                if simpeldatake('user/'+str(chat_id),1) == 'empty':
                    simpledachange('3','user/'+str(chat_id),1)
                    bot.sendMessage(chat_id,'kode yang anda masukkan salah, jatah memasukkan kode tersisa : '+simpeldatake('user/'+str(chat_id),1))
                elif simpeldatake('user/'+str(chat_id),1) != 'blocked' and simpeldatake('user/'+str(chat_id),1) != 'valid' :
                    x = int(simpeldatake('user/'+str(chat_id),1))
                    if x > 0:
                        #print('ini string '+str(a))
                        simpledachange(str(x-1),'user/'+str(chat_id),1)
                        bot.sendMessage(chat_id,'kode yang anda masukkan salah, jatah memasukkan kode tersisa : '+simpeldatake('user/'+str(chat_id),1))
                    else:
                        simpledachange('blocked','user/'+str(chat_id),1)
                        f=open('user/blocklist','a+')
                        f.write(str(chat_id))
                        f.close()
                        bot.sendMessage(chat_id,'anda terblokir, hubungi operator untuk memulihkan')
                else:
                    bot.sendMessage(chat_id,'kode yang anda masukkan tidak terdaftar, please contact vbrillianto@gmail.com to get access')
#------------------------------------------------------------------------                            
#------------------------------------------------------------------------    
    if command[4:10] == 'SKLDBT':
        givenlist=disfile('givenlist.txt.enc')
        givenlist=givenlist.split('\n')
        a=0
        for sekolah in givenlist:
            a+=1
            if sekolah[:4] == command[:4]:
                if simpeldatake("user/"+str(chat_id),2)!='OPS':
                    #simpledachange('valid','user/'+str(chat_id),1)
                    simpledachange(sekolah[5:],'user/'+str(chat_id),4)
                    simpledachange('NON','user/'+str(chat_id),2)
                    simpledachange(command[:4],'user/'+str(chat_id),5)
                    simpledachange(encode(command),'user/'+str(chat_id),3)
                    if os.path.exists("skolidbot/"+sekolah[5:]+'/csv/listguru.txt.enc'):
                        listguru = disfile("skolidbot/"+sekolah[5:]+'/csv/listguru.txt.enc')
                        listguru = listguru.split('\n')
                        for nama in listguru:
                            if command == nama[-22:]:
                                simpledachange('valid','user/'+str(chat_id),1)
                                simpledachange('NON','user/'+str(chat_id),2)
                                simpledachange(str(nama[3:-23]).replace('_',' '),'user/'+str(chat_id),6)
                                bot.sendMessage(chat_id,'Terimakasih telah menggunakan bot ini silahkan cek data anda dengan mengetik atau klik -> /check')
                                break
                        if simpeldatake('user/'+str(chat_id),1) == 'empty':
                            simpledachange('3','user/'+str(chat_id),1)
                            bot.sendMessage(chat_id,'kode yang anda masukkan salah, jatah memasukkan kode tersisa : '+simpeldatake('user/'+str(chat_id),1))
                        elif simpeldatake('user/'+str(chat_id),1) != 'blocked':
                            try:
                                a = int(simpeldatake('user/'+str(chat_id),1))
                                if a > 0:
                                    #print('ini string '+str(a))
                                    simpledachange(str(a-1),'user/'+str(chat_id),1)
                                    bot.sendMessage(chat_id,'kode yang anda masukkan salah, jatah memasukkan kode tersisa : '+simpeldatake('user/'+str(chat_id),1))
                                else:
                                    simpledachange('blocked','user/'+str(chat_id),1)
                                    bot.sendMessage(chat_id,'anda terblokir, hubungi operator untuk memulihkan')
                                    f=open('blocklist','a+')
                                    f.write(str(chat_id))
                                    f.close()
                            except:
                                print('user already valid')
                    else:
                        if simpeldatake('user/'+str(chat_id),1) == 'empty':
                            simpledachange('3','user/'+str(chat_id),1)
                            bot.sendMessage(chat_id,'kode yang anda masukkan salah, jatah memasukkan kode tersisa : '+simpeldatake('user/'+str(chat_id),1))
                        elif simpeldatake('user/'+str(chat_id),1) != 'blocked':
                            x = int(simpeldatake('user/'+str(chat_id),1))
                            if x > 0:
                                #print('ini string '+str(a))
                                simpledachange(str(x-1),'user/'+str(chat_id),1)
                                bot.sendMessage(chat_id,'kode yang anda masukkan salah, jatah memasukkan kode tersisa : '+simpeldatake('user/'+str(chat_id),1))
                            else:
                                simpledachange('blocked','user/'+str(chat_id),1)
                                f=open('user/blocklist','a+')
                                f.write(str(chat_id))
                                f.close()
                                bot.sendMessage(chat_id,'anda terblokir, hubungi operator untuk memulihkan')
                else:
                    for nama in simplepersonlist("skolidbot/"+simpeldatake(urlb,4)+'/csv/listguru.txt'):
                        if command[:] == nama[-23:-1]:
                            simpledachange(str(nama[3:-24]).replace('_',' '),'user/'+str(chat_id),6)
                            bot.sendMessage(chat_id,'anda sudah terdaftar sebagai OPS '+simpeldatake('user/'+str(chat_id),4).replace('_',' '))
                break
            
        if a==len(givenlist):
                if simpeldatake('user/'+str(chat_id),1) == 'empty':
                    simpledachange('3','user/'+str(chat_id),1)
                    bot.sendMessage(chat_id,'kode yang anda masukkan salah, jatah memasukkan kode tersisa : '+simpeldatake('user/'+str(chat_id),1))
                elif simpeldatake('user/'+str(chat_id),1) != 'blocked':
                    x = int(simpeldatake('user/'+str(chat_id),1))
                    if x > 0:
                        #print('ini string '+str(a))
                        simpledachange(str(x-1),'user/'+str(chat_id),1)
                        bot.sendMessage(chat_id,'kode yang anda masukkan salah, jatah memasukkan kode tersisa : '+simpeldatake('user/'+str(chat_id),1))
                    else:
                        simpledachange('blocked','user/'+str(chat_id),1)
                        f=open('user/blocklist','a+')
                        f.write(str(chat_id))
                        f.close()
                        bot.sendMessage(chat_id,'anda terblokir, hubungi operator untuk memulihkan')
        
#------------------------------------------------------------------------
#list path
#------------------------------------------------------------------------    
    urla = "skolidbot/"+simpeldatake("user/"+str(chat_id),4)+'/'
    urla2 = "skolidbot/"+simpeldatake("user/"+str(chat_id),4)#skolidbot/nama_sekolah
    urlb = "user/"+str(chat_id)#user/user_id
    urld="skolidbot/"+simpeldatake(urlb,4)+'/csv/GURU.csv'
    urle="skolidbot/"+simpeldatake(urlb,4)+'/csv/TENDIK.csv'
    urlf="skolidbot/"+simpeldatake(urlb,4)+'/csv/listguru.txt'
    urlg="skolidbot/"+simpeldatake(urlb,4)+'/csv/SISWA.csv'
#------------------------------------------------------------------------    
#jika pesan berupa document            
    if content_type == 'document':
        if simpeldatake(urlb,2)=='OPS':
            file_id=msg['document']['file_id'] #get file_id
            file_name=msg['document']['file_name'] #get file name
            # file_name[:9] daftar-gu daftar_pd daftar-te, ini adalah file yang diharapkan
            # file_name[-4:] xlsx, ini adalah ektensi file yang diharapkan
            #print (file_name[-4:])
            if file_name[-4:]=='xlsx':
                if file_name[:9]=='daftar-gu' or file_name[:9]=='daftar_pd' or file_name[:9]=='daftar-te':
                    #memisahkan dan membuat nama file berdasarkan uplodan
                    if file_name[:9]=='daftar-gu':
                        namafile='GURU.xlsx'
                    elif file_name[:9]=='daftar_pd':
                        namafile='SISWA.xlsx'
                    elif file_name[:9]=='daftar-te':
                        namafile='TENDIK.xlsx'
                    
                    #mendownload file pada folder lembaga yang terkoneksi pada user
                    if os.path.exists(urla2) == True:
                        bot.download_file(file_id, urla+namafile)
                        if namafile=='SISWA.xlsx':
                            unmersis(urla+namafile)
                            delearn(urla+namafile)
                    else :
                        bot.sendMessage(chat_id,'data sekolah tidak ditemukan, silahkan ketik atau tekan /start dan ikuti petunjuk yang diberikan')
                    
                    #convert file ke csv
                    #list nama file di folder skolidbot
                    filelist=[x for x in os.listdir(urla2) if x.endswith(".xlsx")]
                    for f in filelist:
                        read_file = pd.read_excel (urla+f)
                        if os.path.exists(urla+'csv') != True:
                            os.mkdir(urla+'csv')
                        read_file.to_csv (urla+'csv/'+f[:-5]+'.csv', index = None, header = True)# -5 untuk membuang ekstesi .xlsx untuk diganti .csv
                        print('file csv sukses dibuat')
                    bot.sendMessage(chat_id,file_name+' telah dihubungkan dengan database '+simpeldatake(urlb,4))
                    if os.path.exists(urla+'csv/GURU.csv') and os.path.exists(urla+'csv/TENDIK.csv'):
                        bot.sendMessage(chat_id,'klik /securelist untuk membuat daftar user/password GTK, mengenkripsi database dan menghapus data mentah demi keamanan')
                else:
                    bot.sendMessage(chat_id,'Kami hanya menggunakan database dari Dapodik untuk menjamin validitas data')
            else:
                bot.sendMessage(chat_id,'Kami hanya memproses file excel (.xlsx)')
        else:
            bot.sendMessage(chat_id,'hanya data dari OPS yang kami diproses')
#------------------------------------------------------------------------            
    if command == '/securelist':
        if os.path.exists(urld) and os.path.exists(urle):
            if simpeldatake(urlb,2)=='OPS':
                if os.path.exists(urla+'GURU.xlsx'): os.remove(urla+'GURU.xlsx');
                if os.path.exists(urla+'TENDIK.xlsx'): os.remove(urla+'TENDIK.xlsx');
                if os.path.exists(urla+'SISWA.xlsx'): os.remove(urla+'SISWA.xlsx');
                bot.sendMessage(chat_id,'data mentah telah terhapus \nDaftar user telah dibuat \nPassword telah digenerate')
                print('data mentah telah dihapus')
                if os.path.exists(urlf+'.enc') == False:
                    f=open(urlf,'a+')
                    counter=0
                    for i in range (len(personlist(urld))): #urld = link guru.csv
                        b=personlist(urld)[i]
                        no = str(i+1)
                        if len(no) == 1:
                            no='0'+no
                        #print(no+' '+b.replace(' ','_'))
                        f.write(no+' '+b.replace(' ','_')+f' {simpeldatake(urlb,5)}SKLDBT{ranstring(12)}\n')
                        counter=i
                    f.close()
                        #tendik
                    f=open(urlf,'a+')
                    for i in range (len(personlist(urle))): #urle = link tendik.csv
                        b=personlist(urle)[i]
                        no= str(i+2+counter)
                        if len(no) == 1:
                            no='0'+no
                        #print(no+' '+b.replace(' ','_'))
                        f.write(no+' '+b.replace(' ','_')+f' {simpeldatake(urlb,5)}SKLDBT{ranstring(12)}\n')
                    f.close()
                dfile(urlf)
                f=open(urlf,'r')
                bot.sendMessage(chat_id,(f.read().replace('\n','\n\n')).replace(' ','\n'))
                efile(urld)
                efile(urle)
                efile(urlf)
                efile(urlg)
                #end write file list
                
            else:
                bot.sendMessage(chat_id,'hanya OPS yang bisa membuat list data')
        elif os.path.exists(urld+'.enc') and os.path.exists(urle+'.enc'):
            bot.sendMessage(chat_id,'maaf password dan user hanya bisa dibuat sekali, tekan /proses untuk melanjutkan')
        else:
            bot.sendMessage(chat_id,'file tidak lengkap, silahkan upload daftar guru dan daftar tendik terlebih dahulu, atau tunggu semua file terupload sempurna.')
       
        #-----------------------------------------------------------------------------------------------
        #  pemrosesan data siswa dimulai
        #-----------------------------------------------------------------------------------------------
        
        if os.path.exists(urlg+'.enc') or os.path.exists(urlg):
            try:
                os.mkdir(urla+'dsiswa')
            except:
                print('dsiswa already created')
            try:
                os.mkdir(urla+'dsiswa/rombel')
            except:
                print('dsiswa/rombel already created')
            try:
                os.mkdir(urla+'dsiswa/datasort')
            except:
                print('dsiswa/datasort already created')
            try:
                os.mkdir(urla+'dsiswa/sortleter')
            except:
                print('dsiswa/sortleter already created')
            try:
                os.mkdir(urla+'dsiswa/sortage')
            except:
                print('dsiswa/sortage already created')
                '''
                
                os.mkdir(urla+'dsiswa/terimaKPS')
                os.mkdir(urla+'dsiswa/terimaKIP')
                os.mkdir(urla+'dsiswa/layakPIP')
                '''
           
            dfile(urlg)
            rowcomp = 3
            try:
                listf=os.listdir(urla+'dsiswa/datasort')
                for file in listf:
                    os.remove(urla+'dsiswa/datasort/'+file)
            except:
                print('nofile')
                
            listf=[x for x in os.listdir(urla+'dsiswa') if x.endswith(".e")]
            for file in listf:
                os.remove(urla+'dsiswa/'+file)
           
            namalumnik=''
            namalumnisn=''
            namalumnipd=''
            namalpip=''
            namakip=''
            namakps=''
            varlistal=[namalumnik,namalumnisn,namalumnipd,namakip,namakps,namalpip]
            listal=['namalumnik','namalumnisn','namalumnipd','namakip','namakps','namalpip']
            
            nama1='';nama2='';nama3='';nama4='';nama5='';nama6='';
            nama1a='';nama2a='';nama3a='';nama4a='';nama5a='';nama6a='';
            nama1b='';nama2b='';nama3b='';nama4b='';nama5b='';nama6b='';
            rombel=['kelas1a','kelas2a','kelas3a','kelas4a','kelas5a','kelas6a','kelas1b','kelas2b','kelas3b','kelas5b','kelas6b','kelas1','kelas2','kelas3','kelas4','kelas5','kelas6']
            varrombel=[nama1a,nama2a,nama3a,nama4a,nama5a,nama6a,nama1b,nama2b,nama3b,nama4b,nama5b,nama6b,nama1,nama2,nama3,nama4,nama5,nama6]
            
            A='';B='';C='';D='';E='';F='';G='';H='';I='';J='';K='';L='';M='';N='';O='';P='';Q='';R='';S='';T='';U='';V='';W='';X='';Y='';Z='';
            huruf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            dafthuruf= [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
            
            U5='';U6='';U7='';U8='';U9='';U10='';U11='';U12='';U13='';U14='';U15='';U16='';U17='';U18='';U19='';U20='';
            umur=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            varumur=[U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20]
                 
            for jmlsis in range (500):
                if datapick(urlg,1,jmlsis+1+rowcomp)[1]!='':
                    filesiswa=''
                    namasiswa=datapick(urlg,1,jmlsis+1+rowcomp)[1].replace('.','')+'\n'
                    for data in range(62):
                        #print(str(data)+' map to '+str(datapick(urlg,data,jmlsis+1+rowcomp)))
                        if datapick(urlg,data,jmlsis+1+rowcomp)[0]!='':# and datapick(urlg,data,jmlsis+1+rowcomp)[1]!='': #buka siswa.csv jika kolom keterangan dan isi tidak kosong
                            filesiswa=filesiswa+(str(datapick(urlg,data,jmlsis+1+rowcomp))[1:-1].replace(',',':').replace("'",'')+'\n')
                                        
                        if data == 1:# nama
                            for a in range(len(huruf)):
                                nama =(datapick(urlg,data,jmlsis+1+rowcomp)[1])[:1]
                                if nama.upper()[:1]==huruf[a]:
                                    dafthuruf[a]+=namasiswa
                        
                        if data == 6: #tgl lahir
                            tahun = int((datapick(urlg,data,jmlsis+1+rowcomp)[1])[:4])
                            sekarang = datetime.now()
                            usia = sekarang.year-tahun
                            for x in range(len(umur)):
                                if usia == umur[x]:
                                    varumur[x]+=namasiswa
                        
                        if data == 7: #NIK
                            if datapick(urlg,data,jmlsis+1+rowcomp)[1]=='':
                                varlistal[0]+=namasiswa
                        
                        if data == 4: # NISN
                            if datapick(urlg,data,jmlsis+1+rowcomp)[1]=='':
                                varlistal[1]+=namasiswa
                                
                        if data == 2: #NIPD
                            if datapick(urlg,data,jmlsis+1+rowcomp)[1]=='':
                                varlistal[2]+=namasiswa
                                
                        if data == 22: #Penerima KPS
                            if datapick(urlg,data,jmlsis+1+rowcomp)[1]=='Ya':
                                varlistal[4]+=namasiswa+'No.KPS:'+datapick(urlg,23,jmlsis+1+rowcomp)[1]+'\n\n'
                                
                        if data == 42: #penerima KIP
                            if datapick(urlg,data,jmlsis+1+rowcomp)[1]=='Ya':
                                varlistal[3]+=namasiswa+'No.KIP:'+datapick(urlg,43,jmlsis+1+rowcomp)[1]+'\n\n'
                                
                        if data == 50: #layak PIP
                            if datapick(urlg,data,jmlsis+1+rowcomp)[1]=='Ya':
                                varlistal[5]+=namasiswa+'Alasan:'+datapick(urlg,51,jmlsis+1+rowcomp)[1]+'\n\n'
                        
                        if data == 39: #Rombel
                            for x in range(6):
                                print(str(datapick(urlg,data,jmlsis+1+rowcomp)[1])[-2:].lower().replace(' ','').replace('s',''))
                                if str(datapick(urlg,data,jmlsis+1+rowcomp)[1])[-2:].lower().replace(' ','').replace('s','')==str(x+1)+'a':
                                    varrombel[x]+=namasiswa
                                    break
                                elif str(datapick(urlg,data,jmlsis+1+rowcomp)[1])[-2:].lower().replace(' ','').replace('s','')==str(x+1)+'b':
                                    varrombel[x+6]+=namasiswa
                                    break
                                elif str(datapick(urlg,data,jmlsis+1+rowcomp)[1])[-2:].lower().replace(' ','').replace('s','')==str(x+1):
                                    varrombel[x+11]+=namasiswa
                                    break
                        
                    f=open(urla+'dsiswa/'+(str(datapick(urlg,1,jmlsis+1+rowcomp)[1]).replace('.',''))+'.e','w')
                    f.write(encode(filesiswa))
                    f.close()
                #except:
                    #break
            
            for x in range(len(varlistal)):
                f=open(urla+'dsiswa/datasort/'+listal[x],'w')
                f.write(encode(varlistal[x]))
                f.close()
                
                
            for x in range(len(rombel)):
                testa=urla+'dsiswa/rombel/'+rombel[x]
                print(len(rombel))
                print(x)
                print(rombel[x])
                print(testa)
                f=open((urla+'dsiswa/rombel/'+rombel[x]),'w')
                varsplit=varrombel[x].split('\n')
                for y in range(len(varsplit)):
                    if varsplit[y]=='':
                        varsplit.pop(y)
                usiasiswa=[]
                jk=[]
                daftarusia=set()
                jumlahL=0
                for siswa in varsplit:
                    filesiswa =urla+'dsiswa/'+str(siswa)+'.e'
                    data=disfile(urla+'dsiswa/'+str(siswa)+'.e')
                    data=data.split('\n')
                    if data[3]=='JK: L':
                        jumlahL+=1
                    tahun = int(data[6][15:19])
                    sekarang = datetime.now()
                    usia = sekarang.year-tahun
                    jk.append(data[3][-1:])
                    usiasiswa.append(usia)
                    daftarusia.add(usia)
                stringu=''
                stringjk=''
                for z in range(len(jk)):
                    stringjk=stringjk+str(usiasiswa[z])+str(jk[z])+','
                listjk=stringjk.split(',')
                #print(str(z)+'L')
                for c in daftarusia:
                    cl=str(c)+'L'
                    cp=str(c)+'P'
                    stringu=stringu+f'{usiasiswa.count(c)} anak berusia {c} tahun (L = {listjk.count(cl)}, P = {listjk.count(cp)})\n'
                #-------------------------------------------eonewcode        
                f.write(encode(f'''{varrombel[x]}

Jumlah Siswa : {len(varsplit)} (L : {jumlahL}, P : {len(varsplit)-jumlahL})

{stringu}
'''))
                f.close()
             
            for ke in range(len(dafthuruf)):
                if dafthuruf[ke] !='':
                    f=open(urla+'dsiswa/sortleter/'+huruf[ke],'w')
                    f.write(encode(dafthuruf[ke]))
                    f.close()
            
            for ke in range(len(varumur)):
                if varumur[ke] !='':
                    f=open(urla+'dsiswa/sortage/'+str(umur[ke]),'w')
                    f.write(encode(varumur[ke]))
                    f.close()
                    
                    
            bot.sendMessage(chat_id,'\nketik atau klik -> /proses untuk membuat data dan user GTK')
            efile(urlg)
        
#------------------------------------------------------------------------    
    if command == '/proses':
        dfile(urld)
        dfile(urle)
        dfile(urlf)
        if simpeldatake(urlb,2)=='OPS':
            #mengirim nama App data guru dan passw
            bot.sendMessage(chat_id,'silahkan memforward pesan berikut ini kepada yang bersangkutan untuk mendapatkan kode akses')
            try :
                for a in range (50):
                    if simpeldatake(urlf,a+1)!='':
                        bot.sendMessage(chat_id,f'''
t.me/Skolidbot
Nama : {str(simpeldatake(urlf,a+1)).split(' ')[1]}
Kode : {str(simpeldatake(urlf,a+1)).split(' ')[2]}
''')
            except:
                print('err')
            bot.sendMessage(chat_id,'ketik atau tekan -> /menu untuk menuju menu utama')
            #membuat file individu
            try:
                os.mkdir(urla+'dataguru')
            except:
                print('directory available')
                #membuat file guru
            nourutguru=0
            for person in personlist(urld):#urld = guru.csv di csv
                #print(person)
                #mencari urutan guru
                for guru in simplepersonlist(urlf):#urlf = listguru di csv
                    nama = str(guru[3:-24])
                    nama = nama.replace('_',' ')
                    #print(nama)
                    if person==nama:
                        nourutguru+=1
                        #print(str(nourutguru))
                        #print('gotcha '+nama)
                        f=open(urla+'dataguru/'+nama,'w+')
                        f.write(f'Data {nama} sesuai dapodik ({simpeldatake(urld,4)[:25]}) yang diupload di server kami:\n\n')
                        f.close()
                        f=open(urla+'dataguru/'+nama,'a+')
                        for a in range (50) : #50 dan a+1 menghindari menuliskan kolom nomor
                            b = (datapick(urld,a+1,nourutguru))
                            if b[1]!='' and b[1]!='\n':# and b[1]!='Tidak':
                                b=str(b)
                                b=b.replace("'",'')
                                b=b.replace("(",'')
                                b=b.replace(")",'')
                                b=b.replace(",",' : ')
                                f.write(b+'\n')
                        f.close()
                        efile(urla+'dataguru/'+nama)
                        break
                    #mencari urutan tendik
            nouruttendik=0
            for person in personlist(urle):#tendik.csv di csv
                for guru in simplepersonlist(urlf):#urlf = listguru di csv
                    nama = str(guru[3:-24])
                    nama = nama.replace('_',' ')
                    if person==nama:
                        nouruttendik+=1
                        #print('gotcha '+nama)
                        f=open(urla+'dataguru/'+nama,'w+')
                        f.write(f'Data {nama} sesuai dapodik ({simpeldatake(urld,4)[:25]}) yang diupload di server kami:\n\n')
                        f.close()
                        f=open(urla+'dataguru/'+nama,'a+')
                        for a in range (50) : #50 dan a+1 menghindari menuliskan kolom nomor
                            b = (datapick(urle,a+1,nouruttendik)) #urle = data tendik.csv
                            if b[1]!='' and b[1]!='\n':# and b[1]!='Tidak':
                                b=str(b)
                                b=b.replace("'",'')
                                b=b.replace("(",'')
                                b=b.replace(")",'')
                                b=b.replace(",",' : ')
                                f.write(b+'\n')
                        f.close()
                        efile(urla+'dataguru/'+nama)
                        break
        else:
            bot.sendMessage(chat_id,'hanya OPS yang bisa memproses data')
        efile(urld)
        efile(urle)
        efile(urlf)
        
#------------------------------------------------------------------------    
    if command == '/arsipall':
        if simpeldatake(urlb,2)=='OPS':
            try:
                os.remove('arsip/webapp.zip')
            except:
                print('file arsip not found')
            arsipkan('/home/pi/Desktop/runapp',f'/home/pi/Desktop/runapp{datetime.now()}.zip')
            #copyfile('F:/webapp.zip', 'arsip/webapp.zip')
            bot.sendMessage(chat_id,'file telah diarsipkan')
#------------------------------------------------------------------------    
    if command[0:7].lower() =='/mesall':
#         print('ok')
        if chat_id == myID: #memastikan hanya saya yang bisa mengetik untuk semua
            pesan = (str(command.split(' ', 1)[1]))
            kirimlist=[x for x in os.listdir("user/")]
#             print(kirimlist)
            for f in kirimlist:
#                 print (str(f))
                bot.sendMessage(int(f),pesan)
            del pesan
        else:
            bot.sendMessage(chat_id,'hanya admin yang bisa mengirim pesan kepada semua user. kembali -> /menu')
#------------------------------------------------------------------------    
    if command=='/id':
        bot.sendMessage(chat_id,'ID anda adalah : '+str(chat_id))
#------------------------------------------------------------------------        
    if command=='/gtk':
        if simpeldatake(urlb,2)=='OPS':
            bot.sendMessage(chat_id,'''
/LIST_GTK
menampilkan daftar GTK

/NIK_GTK
menampilkan daftar NIK

/NUPTK_GTK
menampilkan daftar NUPTK

/NIP_GTK
menampilkan daftar NIP

/TTL_GTK
menampilkan daftar Tempat/ Tanggal lahir

/HP_GTK
menampilkan daftar Nomor HP

/NPWP_GTK
menampilkan daftar NPWP

/KARPEG_GTK
menampilkan daftar Karpeg

/KARISSU_GTK
menampilkan daftar Karis/ Karsu
''')
    
    if command=='/LIST_GTK':
        if simpeldatake(urlb,2)=='OPS':
            bot.sendMessage(chat_id,'pilih salah satu untuk melihat datanya')
            lista=''
            for PTK in os.listdir(urla+'dataguru'):
                lista+='/'+PTK+'\n'
            bot.sendMessage(chat_id,lista.replace(' ','_').replace('.enc','')+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
            bot.sendMessage(chat_id,'Ada '+str(len(os.listdir(urla+'dataguru')))+' GTK terdaftar, jika tidak sesuai jumlah di Dapodik silahkan ketik atau klik -> /proses')
        else :
            bot.sendMessage(chat_id,'hanya OPS yang bebas mengakses data semua PTK')

#------------------------------------------------------------------------    
    namaPTK=command[1:].replace('_',' ')+'.enc'
    if os.path.exists(urla+'dataguru/'+namaPTK):
        if simpeldatake(urlb,6)==command[1:] or simpeldatake(urlb,2)=='OPS':
            gtk=disfile(urla+'dataguru/'+namaPTK)
            bot.sendMessage(chat_id,gtk)
            bot.sendMessage(chat_id,'ketik atau tekan -> /menu untuk kembali pada menu utama')
        else :
            bot.sendMessage(chat_id,'fitur ini hanya untuk OPS')
        
#------------------------------------------------------------------------
    if command == '/check':
        if simpeldatake(urlb,1)=='valid':
            gtk=disfile(urla+'dataguru/'+simpeldatake(urlb,6)+'.enc')
            bot.sendMessage(chat_id,gtk+'\n/menu untuk kembali pada menu utama')
#------------------------------------------------------------------------    
    if command == '/infobot':
        f=open('info.txt')
        bot.sendMessage(chat_id,f.read()+'\nUntuk perkembangan fitur bisa dilihat di /whats_new?')
        f.close()
#------------------------------------------------------------------------    
    if command == '/whats_new':
        f=open('whats_new.txt')
        bot.sendMessage(chat_id,f.read())
        f.close()

    if command == '/menu':
        if simpeldatake(urlb,1)=='valid':
            if chat_id==myID:
                bot.sendMessage(chat_id,'''
berikut command untuk mengakses data

/admin  : menu admin
/gtk    : Daftar GTK
/siswa  : Daftar Siswa
/ops    : menu ops
/info   : menu info bot
''')
            elif simpeldatake(urlb,2)=='OPS':
                bot.sendMessage(chat_id,'''
berikut command untuk mengakses data

/gtk    : daftar GTK
/siswa  : daftar Siswa
/ops    : menu OPS
/info   : menu info bot
''')
            elif simpeldatake(urlb,2)=='NON':
                bot.sendMessage(chat_id,'''
berikut command untuk mengakses data

/check  : melihat info pribadi
/siswa  : daftar siswa
/info   : menu info bot
''')
            else:
                bot.sendMessage(chat_id,'akses ilegal')
            
    if command == '/sortum':
        if simpeldatake(urlb,1)=='valid':
            umur = ''
            for a in range (5,20):
                if os.path.exists(urla+'dsiswa/sortage/'+str(a)):
                    umur=umur+'/siswa_umur_'+str(a)+'\n'
            bot.sendMessage(chat_id,umur)
                
    if command == '/siswa':
        if simpeldatake(urlb,2)=='OPS':
            bot.sendMessage(chat_id,'''
/kelas  : daftar siswa per kelas
/nonik  : siswa tanpa NIK
/kip    : siswa menerima KIP
/kps    : siswa penerima KPS
/lpip   : siswa layak PIP
/nonipd : siswa belum punya No Induk
/nonisn : siswa belum punya NISN
/alfasi : siswa berdasar huruf awal
/sortum : siswa berdasarkan umur
''')
        else :
            bot.sendMessage(chat_id,'''
/kelas  : daftar siswa per kelas
/kip    : siswa menerima KIP
/kps    : siswa penerima KPS
/alfasi : siswa berdasar huruf awal
/sortum : siswa berdasarkan umur
''')
        
    if command[:12] == '/siswa_umur_':
        if simpeldatake(urlb,1)=='valid':
            try:
                f=open(urla+'dsiswa/sortage/'+command[-2:],'r')
            except:
                f=open(urla+'dsiswa/sortage/'+command[-1:],'r')
            x='/_'+decode(f.read()).replace(' ','_').replace('\n','\n/_')[:-2]
            bot.sendMessage(chat_id,x+'\n\n tekan /sortum untuk kembali ke daftar abjad\n tekan /menu untuk kembali ke menu utama')
            f.close()
    
    if command == '/alfasi':
        if simpeldatake(urlb,1)=='valid':
            huruf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            siswa =''
            for a in range(len(huruf)):
                try:
                    f = open(urla+'dsiswa/sortleter/'+str(huruf[a]),'r')
                    x=f.read()
                    if x!='':
                        siswa=siswa+'/siswa__'+huruf[a]+'\n'
                    f.close()
                except:
                    print('nofollder')
            bot.sendMessage(chat_id,siswa+'\n tekan /menu untuk kembali ke menu utama')
    
    if command[:8] == '/siswa__':
        if simpeldatake(urlb,1)=='valid':
            f=open(urla+'dsiswa/sortleter/'+command[-1],'r')
            x='/_'+decode(f.read()).replace(' ','_').replace('\n','\n/_')[:-2]
            bot.sendMessage(chat_id,x+'\n\n tekan /alfasi untuk kembali ke daftar abjad\n tekan /menu untuk kembali ke menu utama')
            f.close()
    
    if command == '/nonik':
        if simpeldatake(urlb,2)=='OPS':
            if os.path.exists(urla+'dsiswa/datasort/namalumnik'):
                f=open(urla+'dsiswa/datasort/namalumnik')
                isi = decode(f.read())
                if isi !='':
                    bot.sendMessage(chat_id,'/_'+isi.replace(' ','_').replace('\n','\n/_')[:-2]+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                else :
                    bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                f.close()
            else:
                bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /menu untuk kembali ke menu utama')
        
    if command == '/kip':
        if simpeldatake(urlb,2)=='OPS':
            if os.path.exists(urla+'dsiswa/datasort/namakip'):
                f=open(urla+'dsiswa/datasort/namakip','r')
                isi = decode(f.read())
                if isi !='':
                    bot.sendMessage(chat_id,'/_'+isi.replace(' ','_').replace('\n\n','\n\n/_')[:-2]+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                else :
                    bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                f.close()
            else:
                bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /menu untuk kembali ke menu utama')
        
    if command == '/kps':
        if simpeldatake(urlb,2)=='OPS':
            if os.path.exists(urla+'dsiswa/datasort/namakps'):
                f=open(urla+'dsiswa/datasort/namakps','r')
                isi = decode(f.read())
                if isi !='':
                    bot.sendMessage(chat_id,'/_'+isi.replace(' ','_').replace('\n\n','\n\n/_')[:-2]+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                else :
                    bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                f.close()
            else:
                bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /menu untuk kembali ke menu utama')
            
    if command == '/lpip':
        if simpeldatake(urlb,2)=='OPS':
            if os.path.exists(urla+'dsiswa/datasort/namalpip'):
                f=open(urla+'dsiswa/datasort/namalpip','r')
                isi = decode(f.read())
                if isi !='':
                    bot.sendMessage(chat_id,'/_'+isi.replace(' ','_').replace('\n\n','\n\n/_')[:-2]+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                else :
                    bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                f.close()
            else:
                bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /menu untuk kembali ke menu utama')
    
    if command == '/nonipd':
        if simpeldatake(urlb,2)=='OPS':
            if os.path.exists(urla+'dsiswa/datasort/namalumnipd'):
                f=open(urla+'dsiswa/datasort/namalumnipd','r')
                isi = decode(f.read())
                if isi !='':
                    bot.sendMessage(chat_id,'/_'+isi.replace(' ','_').replace('\n','\n/_')[:-2]+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                else :
                    bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                f.close()
            else:
                bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /menu untuk kembali ke menu utama')
        
    if command == '/nonisn':
        if simpeldatake(urlb,2)=='OPS':
            if os.path.exists(urla+'dsiswa/datasort/namalumnisn'):
                f=open(urla+'dsiswa/datasort/namalumnisn','r')
                isi = decode(f.read())
                if isi !='':
                    bot.sendMessage(chat_id,'/_'+isi.replace(' ','_').replace('\n','\n/_')[:-2]+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                else :
                    bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\n tekan /menu untuk kembali ke menu utama')
                f.close()
            else:
                bot.sendMessage(chat_id,'tidak ada siswa di daftar ini\n\ntekan /menu untuk kembali ke menu utama')
        
    if command == '/kelas':
        if simpeldatake(urlb,1)=='valid':
            kelasberisi =[x for x in os.listdir(urla+'dsiswa/rombel')]
            ukuran= [os.path.getsize(urla+'dsiswa/rombel/'+x) for x in os.listdir(urla+'dsiswa/rombel')]
            kelastampil=[]
            for kelas in range(len(kelasberisi)):
                print(kelasberisi[kelas]+':'+str(ukuran[kelas]))
                if ukuran[kelas]>85:
                    kelastampil.append(kelasberisi[kelas])
            kelastampil.sort()        
            print(kelastampil)
            strklst=''
            strklst=strklst.join(kelastampil)
            print(strklst)
            if simpeldatake(urlb,1)=='valid':
                bot.sendMessage(chat_id,strklst.replace('kelas','\n/kelas_')[1:])
    
    if command[:7] == '/kelas_':
        if simpeldatake(urlb,1)=='valid':
            if os.path.exists(urla+'dsiswa/rombel/'+command[1:].replace('_','')):
                f = open(urla+'dsiswa/rombel/'+command[1:].replace('_',''),'r')
                nama = decode(f.read())
                nama = nama.split('\n\n')
                isi = '/_'+nama[0].replace(' ','_').replace('\n','\n/_')+'\n'+nama[1]+'\n\n'+nama[2]
                
                bot.sendMessage(chat_id,'Daftar Siswa kelas '+command[-2:].replace('s','').replace('_','')+'\n\n'+isi)#+'\nJumlah siswa = '+str(len(listsis)-1)+'\nJumlah laki-laki = '+str(hitungL)+'\nJumlah Perempuan = '+str(len(listsis)-hitungL-1)+'\n\n'+stringu+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
                f.close()
            
    if os.path.exists(urla+'dsiswa/'+command[2:].replace('_',' ')+'.e'):
        if simpeldatake(urlb,1)=='valid':
            f=open(urla+'dsiswa/'+command[2:].replace('_',' ')+'.e')
            bot.sendMessage(chat_id,decode(f.read())+'\n\n tekan /kelas untuk kembali ke pilihan kelas\n tekan /menu untuk kembali ke menu utama')
            f.close()
    
    if command[:7].lower() == 'deluser': #menghapus akses user
        if simpeldatake(urlb,2)=='OPS':
            #get user ID
            target = command[8:]
            a = simpeldatake('user/'+target,4)
            b = simpeldatake(urlb,4)
            if a==b:
                simpledachange('blocked','user/'+target,1)
                bot.sendMessage(chat_id,f'user {command[-10:]} telah di block')
    
    if command[:7].lower() == 'revuser': #mengembalikan akses user
        if simpeldatake(urlb,2)=='OPS':
            #get user ID
            target = command[8:]
            a = simpeldatake('user/'+target,4)
            b = simpeldatake(urlb,4)
            if a==b:
                simpledachange('valid','user/'+target,1)
                bot.sendMessage(chat_id,f'user {command[-10:]} telah di pulihkan')
                
    if command=='/mintakode':
        if chat_id == myID:
            f=disfile('shortskulist.txt.enc')
            a=f.split('\n')
            for x in range(len(a)):
                if a[x]!='':
                    bot.sendMessage(chat_id,a[x])
    
    if command == '/codelist':
        if chat_id == myID:
            a=disfile('shortskulist.txt.enc')
            bot.sendMessage(chat_id,a)
    
    if command[:9] == 'createOps':
        if chat_id == myID:
            a=command.split(' ')
            ada=False
            try:
                f=disfile('givenlist.txt.enc')
                f=f.split('\n')
                for daftar in f:
                    if daftar[:4]==a[1] or daftar[5:]==a[2]:
                        bot.sendMessage(chat_id,'kode sekolah/ sekolah telah terdaftar cek /codelist')
                        ada=True
            except:
                print('err')
            if len(a)!=3:
                bot.sendMessage(chat_id,'format createOps<spasi>4 kode sekolah<spasi>nama sekolah tanpa spasi\ncontoh : createOps ANU1 SDN_Anurejo_1')
            elif ada==False:
                createOps(a[1],a[2])
                bot.sendMessage(chat_id,'kode telah dibuat klik /codelist')
                
                
    if command[:6]=='delOps':
        if chat_id == myID:
            a=command.split(' ')
            delOps(a[1])
            bot.sendMessage(chat_id,'perintah disampaikan ke server, klik /codelist untuk melihat list terkini')
        
    
    if command == '/progres':
        if simpeldatake(urlb,1)=='valid':
            f = open('plugin/dapodik.txt','r')
            dapox = f.read()
            f.close()
            bot.sendMessage(chat_id,dapox + '\n\nTekan /menu untuk kembali ke menu utama')
    
    if command == '/cuaca':
        cualist=[]
        f=open('plugin/cuaca.txt','r')
        cuacal=f.read()
        f.close
        cualist=cuacal.split('\n')
        tanggalsekarang=str(date.today().strftime("%d"))
        listharian=[]
        strharian=''
        for item in cualist:
            if item[25:27]==tanggalsekarang:
                listharian.append(item[37:]+'_')
        bot.sendMessage(chat_id,strharian.join(listharian).replace('_','\n\n')+'\nTekan /menu untuk kembali ke menu utama')
    
    if command == '/syscapt':
        if chat_id == myID:
            subprocess.call(["python3", "plugin/crawl/bloger.py"])
            bot.sendMessage(chat_id,'screenshot uploaded \ncek : https://verildatacrawl.blogspot.com/2020/10/blog-post_30.html')
    
    if command[:6].lower() == 'wikis ':
        text = command[6:]
        slist=wikis.search(text)
        stringa=''
        for x in range(len(slist)):
            #mengubah karakter agar setiap item menjadi clickable command
            stringa=stringa+'/wikis'+'_'+slist[x]
            stringa=stringa.replace(')','_kt_')
            stringa=stringa.replace('(','_kb_')
            stringa=stringa.replace(':','_td_')
            stringa=stringa.replace(';','_tk_')
            stringa=stringa.replace('.','_tt_')
            stringa=stringa.replace(',','_km_')
            stringa=stringa.replace('"','_tp_')
            stringa=stringa.replace('?','_as_')
            stringa=stringa.replace('-','__')
            stringa=stringa.replace('–','___')
            stringa=stringa.replace("'",'_sp_')
            stringa=stringa.replace(' ','_')+'\n'
        bot.sendMessage(chat_id,stringa)
    
    if command[:7]== '/wikis_':
        text=command[7:]
        text=text.replace('_kt_',')')
        text=text.replace('_kb_','(')
        text=text.replace('_td_',':')
        text=text.replace('_tk_',';')
        text=text.replace('_tt_','.')
        text=text.replace('_km_',',')
        text=text.replace('_tp_','"')
        text=text.replace('_as_','?')
        text=text.replace('__','-')
        text=text.replace('___','–')
        text=text.replace('_sp_',"'")
        text=text.replace('_',' ')
        x=wikis.open(text) #[title,content1,content2,content3,url,link]
        bot.sendMessage(chat_id,f'''
{x[0]}
{x[1]}
{x[2]}
''')
        x=wikis.link(text)
        bot.sendMessage(chat_id,'gali lebih dalam :\n'+x+'\n\n tekan /menu untuk kembali ke menu utama')
    
    if command == '/NIK_GTK':
        if simpeldatake(urlb,2)=='OPS':
            filelist=[x for x in os.listdir(urla+'dataguru') if x.endswith(".enc")]
    #         print(filelist)
            peritem=[]
            viewt=''
            for item in filelist:
    #             print(urla+'dataguru/'+item)
                x=disfile(urla+'dataguru/'+item)
                x=x.split('\n')
                index=[a for a in x if a.startswith('NIK ')]
                if len(index)==0:
                    index=['tidak punya NIK']
                peritem.append(str(item)[:-4]+ '\n'+ index[0]+'\n\n')
            bot.sendMessage(chat_id,viewt.join(peritem))
    
    
    if command == '/NUPTK_GTK':
        if simpeldatake(urlb,2)=='OPS':
            filelist=[x for x in os.listdir(urla+'dataguru') if x.endswith(".enc")]
    #         print(filelist)
            peritem=[]
            viewt=''
            for item in filelist:
    #             print(urla+'dataguru/'+item)
                x=disfile(urla+'dataguru/'+item)
                x=x.split('\n')
                index=[a for a in x if a.startswith('NUPTK ')]
                if len(index)==0:
                    index=['tidak punya NUPTK']
                peritem.append(str(item)[:-4]+ '\n'+ index[0]+'\n\n')
            bot.sendMessage(chat_id,viewt.join(peritem))
    
    
    if command == '/NIP_GTK':
        if simpeldatake(urlb,2)=='OPS':
            filelist=[x for x in os.listdir(urla+'dataguru') if x.endswith(".enc")]
    #         print(filelist)
            peritem=[]
            viewt=''
            for item in filelist:
    #             print(urla+'dataguru/'+item)
                x=disfile(urla+'dataguru/'+item)
                x=x.split('\n')
                index=[a for a in x if a.startswith('NIP ')]
                if len(index)==0:
                    index=['tidak punya NIP']
                peritem.append(str(item)[:-4]+ '\n'+ index[0]+'\n\n')
            bot.sendMessage(chat_id,viewt.join(peritem))
    
    if command == '/TTL_GTK':
        if simpeldatake(urlb,2)=='OPS':
            filelist=[x for x in os.listdir(urla+'dataguru') if x.endswith(".enc")]
    #         print(filelist)
            peritem=[]
            viewt=''
            for item in filelist:
    #             print(urla+'dataguru/'+item)
                x=disfile(urla+'dataguru/'+item)
                x=x.split('\n')
                indexa=[a for a in x if a.startswith('Tempat Lahir ')]
                indexb=[a for a in x if a.startswith('Tanggal Lahir ')]
                if len(indexa)==0 or len(indexb)==0:
                    indexa=['TTL invalid']
                    indexb=[' ']
                peritem.append(str(item)[:-4]+ '\n'+ indexa[0][15:]+', '+indexb[0][16:]+'\n\n')
            bot.sendMessage(chat_id,viewt.join(peritem))
    
    if command == '/HP_GTK':
        if simpeldatake(urlb,2)=='OPS':
            filelist=[x for x in os.listdir(urla+'dataguru') if x.endswith(".enc")]
    #         print(filelist)
            peritem=[]
            viewt=''
            for item in filelist:
    #             print(urla+'dataguru/'+item)
                x=disfile(urla+'dataguru/'+item)
                x=x.split('\n')
                indexa=[a for a in x if a.startswith('HP ')]
                if len(indexa)==0:
                    indexa=['Nomor HP tidak terdaftar']
                peritem.append(str(item)[:-4]+ '\n'+ indexa[0]+'\n\n')
            bot.sendMessage(chat_id,viewt.join(peritem))
    
    
    if command == '/NPWP_GTK':
        if simpeldatake(urlb,2)=='OPS':
            filelist=[x for x in os.listdir(urla+'dataguru') if x.endswith(".enc")]
    #         print(filelist)
            peritem=[]
            viewt=''
            for item in filelist:
    #             print(urla+'dataguru/'+item)
                x=disfile(urla+'dataguru/'+item)
                x=x.split('\n')
                indexa=[a for a in x if a.startswith('NPWP ')]
                if len(indexa)==0:
                    indexa=['Tidak memiliki NPWP']
                peritem.append(str(item)[:-4]+ '\n'+ indexa[0]+'\n\n')
            bot.sendMessage(chat_id,viewt.join(peritem))
    
    
    if command == '/KARPEG_GTK':
        if simpeldatake(urlb,2)=='OPS':
            filelist=[x for x in os.listdir(urla+'dataguru') if x.endswith(".enc")]
    #         print(filelist)
            peritem=[]
            viewt=''
            for item in filelist:
    #             print(urla+'dataguru/'+item)
                x=disfile(urla+'dataguru/'+item)
                x=x.split('\n')
                indexa=[a for a in x if a.startswith('Karpeg ')]
                if len(indexa)==0:
                    indexa=['Tidak memiliki Karpeg']
                peritem.append(str(item)[:-4]+ '\n'+ indexa[0]+'\n\n')
            bot.sendMessage(chat_id,viewt.join(peritem))
    
    
    if command == '/KARISSU_GTK':
        if simpeldatake(urlb,2)=='OPS':
            filelist=[x for x in os.listdir(urla+'dataguru') if x.endswith(".enc")]
    #         print(filelist)
            peritem=[]
            viewt=''
            for item in filelist:
    #             print(urla+'dataguru/'+item)
                x=disfile(urla+'dataguru/'+item)
                x=x.split('\n')
                indexa=[a for a in x if a.startswith('Karis/Karsu ')]
                if len(indexa)==0:
                    indexa=['Tidak memiliki Karis atau Karsu']
                peritem.append(str(item)[:-4]+ '\n'+ indexa[0]+'\n\n')
            bot.sendMessage(chat_id,viewt.join(peritem))
    
    
    if command[:7].lower()=='opsbaru':
        if simpeldatake(urlb,2)=='OPS':
            if os.path.exists('user/'+command[8:]):
                simpledachange('OPS','user/'+command[8:],2)
                bot.sendMessage(chat_id,'menu user '+command[8:]+' telah diganti menu OPS')
                bot.sendMessage(int(command[8:]),'menu OPS telah diaktifkan pada akun anda, \ntekan /menu untuk melanjutkan')
            else:
                bot.sendMessage(chat_id,'invalid user ID : '+command[8:])
    
    if command[:7].lower()=='gtkbaru':
        if simpeldatake(urlb,2)=='OPS':
            print('merubah gtk '+command[8:])
            if os.path.exists('user/'+command[8:]):
                simpledachange('NON','user/'+command[8:],2)
                bot.sendMessage(chat_id,'menu user '+command[8:]+' telah diganti ke NON OPS')
                bot.sendMessage(int(command[8:]),'menu NON OPS telah diaktifkan pada akun anda, \ntekan /menu untuk melanjutkan')
            else:
                bot.sendMessage(chat_id,'invalid user ID : '+command[8:])
    
    if command=='/ops':
        if simpeldatake(urlb,2)=='OPS':
            bot.sendMessage(chat_id,'''
/progres : progres dapodik Kec. Puspo
/proses : mendapatkan list user

opsbaru[spasi][userID]
untuk menambahkan menu ops pada user

gtkbaru[spasi][userID]
untuk mengubah menu user ke menu GTK

deluser[spasi][userID]
untuk menghapus akses user

revuser[spasi][userID]
untuk mengembalikan akses user
''')
    
    if command=='/info':
        bot.sendMessage(chat_id,'''
/infobot  : menampilkan info bot
/id     : ID anda pada bot ini
/cuaca  : cuaca kota pasuruan berdasar BMKG
/pusmenjar : menampilkan publikasi pusmenjar

wikis[spasi][input text]
untuk mencari artikel wikipedia
contoh : wikis rantai makanan
''')
    
    if command=='/admin':
        if chat_id==myID:
            bot.sendMessage(chat_id,'''
/skulist : baca shortskulist
/givenlist : baca givenlist
/liSkul: get folder school list
/lisuser : get user folder list
/mintakode : get individual mesage ops code
/codelist : get all registered ops code list
/syscapt : upload screenshot to bloger
/arsipall : mengarsipkan App dan Data

mesall[spasi][pesan]
kirim pesan ke semua User
contoh : mesall pembaharuan bot telah dirilis

createOps[spasi][empat kode sekolah][spasi][nama sekolah tanpa spasi]
membuat kode OPS
contoh : createOps PSM2 SDNPusungmalang2

delOps[spasi]
menghapus kode OPS
contoh : delOps PSM2
''')
    
    if command == '/skulist':
        if os.path.exists('shortskulist.txt.enc'):
            a=disfile('shortskulist.txt.enc')
            a=a.split('\n')
            bot.sendMessage(chat_id,a)
    
    if command == '/givenlist':
        if os.path.exists('givenlist.txt.enc'):
            a=disfile('givenlist.txt.enc')
            a=a.split('\n')
            bot.sendMessage(chat_id,a)
    
    if command == '/liSkul':
        a=[x for x in os.listdir('skolidbot')]
        b=''
        for item in a:
            b+=item+'\n'
        bot.sendMessage(chat_id,b)
    
    if command == '/lisuser':
        a=[x for x in os.listdir('user')]
        b=''
        for item in a:
            b+='/user_'+item+'\n'
        bot.sendMessage(chat_id,b)
    
    if command[:6] == '/user_':
        if os.path.exists(command.replace('_','/')[1:]):
            with open(command.replace('_','/')[1:]) as f:
                bot.sendMessage(chat_id,f.read())
    
    if command=='/pusmenjar':
         bot.sendMessage(chat_id,'''
Berikut ini adalah publikasi pusmenjar yang telah difilter
berdasarkan kategori :
/Buku_Saku
/Buletin_Assesment
/Materi_Paparan
/Model_Penilaian_Pendidikan
/Modul_Asesmen_Awal
/Rilis_UN

berdasarkan tahun :
/pub_tahun_2020
/pub_tahun_2019
/pub_tahun_2018

/all_publikasi
''')
    
    if command=='/Buku_Saku':
        bot.sendMessage(chat_id,pijar.katjudurl(0)+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/Buletin_Assesment':
        bot.sendMessage(chat_id,pijar.katjudurl(1)+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/Materi_Paparan':
        bot.sendMessage(chat_id,pijar.katjudurl(2)+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/Model_Penilaian_Pendidikan':
        bot.sendMessage(chat_id,pijar.katjudurl(3)+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/Modul_Asesmen_Awal':
        bot.sendMessage(chat_id,pijar.katjudurl(4)+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/Rilis_UN':
        bot.sendMessage(chat_id,pijar.katjudurl(5)+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/pub_tahun_2020':
        bot.sendMessage(chat_id,pijar.tahjudurl('2020')+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/pub_tahun_2019':
        bot.sendMessage(chat_id,pijar.tahjudurl('2019')+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/pub_tahun_2018':
        bot.sendMessage(chat_id,pijar.tahjudurl('2018')+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')
    if command=='/all_publikasi':
        bot.sendMessage(chat_id,pijar.judurl()+'\n\n tekan /pusmenjar untuk kembali ke menu publikasi\ntekan /menu untuk kembali ke menu utama')

#this token file consist two bot tokens from botfather, token[0] just for test, token[1] is deployment token
with open('token') as f:
    token=f.read()
token=token.split('\n')          
bot = telepot.Bot(token[0])#testbot
#bot = telepot.Bot(token[1])#skolidbot
bot.message_loop(handle)
print('i am listening..')
bot.sendMessage(myID,'system online!')

while 1:
    time.sleep(0.1)


