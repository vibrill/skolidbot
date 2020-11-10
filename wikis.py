import wikipedia
import urllib.request, urllib.error

wikipedia.set_lang('id')

def search(text):
    searchlist = wikipedia.search(text)
    return searchlist

def open (text):
    a = wikipedia.page(text)
    x = a.content.strip().split('\n')
    title = a.title.upper()
    content1 = x[0]
#     content2 = x[1]
#     content3 = x[2]
    url = a.url
    print(title+'\n'+content1+'\n'+url)
    return [title,content1,url]

def link(text):
    a = wikipedia.page(text).links
    link =''
    hitung = 0
    count = 0
    for item in a:
        try:
            con=urllib.request.urlopen('https://id.wikipedia.org/wiki/'+item.replace(' ','_'))
#             response=request.get('https://id.wikipedia.org/wiki/'+item)
            print('sukses ping page')
            hitung+=1
            link = link+'/wikis_'+item
            link=link.replace(')','_kt_')
            link=link.replace('(','_kb_')
            link=link.replace(':','_td_')
            link=link.replace(';','_tk_')
            link=link.replace('.','_tt_')
            link=link.replace(',','_km_')
            link=link.replace('"','_tp_')
            link=link.replace('?','_as_')
            link=link.replace('-','__')
            link=link.replace('–','___')
            link=link.replace("'",'_sp_')
            link=link.replace(' ','_')+'\n'
            if hitung==10:break 
        except:
            print(Exception)
            if len(a)!=0:
                print('https://id.wikipedia.org/wiki/'+item+' : not reachable')
            else:
                print('link kosong')
            count+=1
            if count == 20: break
    print(link)
    
    return link


# searchlist = search(input('masukkan text yang hendak dicari : '))
# for x in range(len(searchlist)):
#     print(str(x)+' '+searchlist[x])
# pilih = input('masukkan no index title yang ingin diakses : ')
# pilih=searchlist[int(pilih)]
# a = wikipedia.page(pilih)
# print(a.title.upper())
# print(a.content.split('\n')[0])
# print(a.url)
# print('\n\nExternal links:')
# for x in range(len(a.links)):
#     print(str(x)+' '+a.links[x])
#     if x==7:
#         break