#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:28:27 2018

@author: yanglei
"""
from __future__ import unicode_literals
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from seleniumChrome import getImgHrefs
from yllab import *
from bs4 import BeautifulSoup 
bs = BeautifulSoup
import webbrowser as wb
import requests
from requests import *
rq = requests
import hashlib,json
from collections import Counter
from proxy import *
md5 = lambda x:hashlib.md5(x).hexdigest()

def saveJson(path, dic):
    with open(path,'w') as f:
        json.dump(dic,f)
def loadJson(path,):
    with open(path,) as f:
        return json.load(f)
        
def gett(url,img=False):
    while 1:
        try:
#            return seleHtml(url)
            r = proxyget(url,timeout=5,)

#            time.sleep(TIME_GAP+randfloat()*TIME_GAP)
#            r = rq.get(url,timeout=5,)
            g.r = r
            if img:
                return r.content
            return r.text
        except (rq.exceptions.RequestException)as e:
            pred-'requests Error!!'
            print e
            pass
def save_data(data, name='Python_pickle'):  #保存进度
    import pickle
    name = name
    f = open(name, "wb")
    pickle.dump(data,f)
    f.close()
def load_data(name='Python_pickle'):  #载入数据
    import pickle
    name = name
    if not os.path.isfile(name):
        print '在',os.path.abspath('.'),'目录下,“'+name+'”文件不存在，操作失败！'
        return
    f = open(name,"rb")
    data = pickle.load(f)
    f.close()
    return data
def utf8(s):
    if isinstance(s,unicode):
        s = s.encode('utf-8')
    return s
def rmhtml(url):
    href = url
    md5c = md5(href)
    path = pathjoin(HTML_CACHE, md5c)
    if not isfile(path):
        pred-'passed %s'%path
        return
    pred - 'rm %s'%path
    os.remove(path)
def gethtml(href):
    md5c = md5(href)
    path = pathjoin(HTML_CACHE, md5c)
    listt = os.listdir(HTML_CACHE)
    if md5c in listt:
        return tounicode(openread(path))
    raw = gett(href)
#    if 'charset=gbk' in raw:
#        raw.decode('gbk')
    text = tounicode(raw)
    openwrite(utf8(text), path)
    return text
_HREF_COUNT = [-1]
def getHrefs(href):
    _HREF_COUNT[0] += 1
    md5c = md5(href)
    path = pathjoin(IMG_HREF_CACHE, md5c)
    listt = os.listdir(IMG_HREF_CACHE)
    if md5c in listt:
        return (load_data(path))
    
    pblue-'try selenium %dth url:%s'%(_HREF_COUNT[0],href)
    hrefs = getImgHrefs(href, n=SHOW_IMG_N)
    save_data(hrefs , path)
    return hrefs

def readCacheImg(path):
    try:
        return imread(path)
    except IOError as e:
        pred-'IOError'
        print e
        os.remove(path)
        raise IOError
def getImg(href):
    md5c = md5(href)
    path = pathjoin(IMG_CACHE, md5c)
    listt = os.listdir(IMG_CACHE)
    if md5c in listt:
        return readCacheImg(path)
    img = gett(href, img=True)
    with open(path, 'wb') as f:
        f.write(img)
    return readCacheImg(path)

#def getImgs(hrefs):
#    md5cs = map(md5,hrefs)
#    paths = map(lambda md5c:pathjoin(IMG_CACHE, md5c), md5cs)
#    listt = os.listdir(IMG_CACHE)
#    
#    
#    if md5c in listt:
#        return readCacheImg(path)
#    img = gett(href, img=True)
#    with open(path, 'wb') as f:
#        f.write(img)
#    return readCacheImg(path)

def see(respon):
    txt = respon
    if typestr(respon) == 'requests.models.Response':
        txt = respon.text
    txt = txt.replace('charset=gbk','charset=utf-8')
    openwrite(utf8(txt),'/tmp/see.html')
    wb.open_new('http://127.0.0.1/see.html')
    
def splitTo2(text):
    ind = text.index(u"：")
    k, v = text[:ind],text[ind+1:].strip()
    return k,v
getTexts = lambda soupList:[sp.text for sp in soupList]
ton1 = lambda n1,level=5,size='':n1.replace('n%d/%sjfs'%(level,size and 's%dx%d_'%(size,size)),'n1/s%dx%d_jfs'%(imgsize,imgsize))

HTML_CACHE ='cache/html'
IMG_HREF_CACHE = 'cache/imghref'
IMG_CACHE = 'cache/img'
SHOW_IMG_N = 15
TIME_GAP = 2

listroot = 'https://list.jd.com'
itemroot = 'https://item.jd.com'
urlmat = 'https://item.jd.com/%d.html'


proxies = {
  "http": "http://127.0.0.1:1080",
}


totaln = 300
pages = totaln//60+1
imgsize = 1000
DowloadImg = True
if 1:
    bigMod = 0
    bigMod = 1
    bigMod = 2
    bigMod = 3
#for bigMod in [0,1,2,3]:
    if bigMod == 0:
        className = 'milk'
        pagemat = 'https://list.jd.com/list.html?cat=1320,1585,9434&page={page}&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main'    
    
    if bigMod == 1:
        className = 'drink'
        pagemat = 'http://list.jd.com/list.html?cat=1320,1585,1602&page={page}&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main'    
    
    if bigMod == 2:
        className = 'paper'
        pagemat = 'https://list.jd.com/list.html?cat=1316,1625,1671&page={page}&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main'    
    
    if bigMod == 3:
        className = 'noodles'
        pagemat = 'http://list.jd.com/list.html?cat=1320,1584,2679&ev=1107_83261&page={page}&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main'
    if bigMod == 4:
        className = 'wine'
        pagemat = 'https://list.jd.com/list.html?cat=12259,12260&page={page}&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main'    
    
    JSON_DIR = pathjoin(className,'json')
    IMG_DIR = pathjoin(className,'img')
    if not isdir(className):
        os.makedirs(JSON_DIR)
        os.makedirs(IMG_DIR)
    if __name__ == '__main__':
        urls = [pagemat.format(page=p+1) for p in range(pages)]
        htmls = []
        for url in urls:
            html = gethtml(url)
        #    see(html)
            htmls.append(html)
        
        hrefs = []
        for html in htmls:
            sp = bs(html).find(class_='gl-warp clearfix')
            divs = sp.find_all(class_="gl-item")
            divs = [div.find(class_="p-name") for div in divs]
            hrefs += ['https:%s'%d.a['href'] for d in divs]
        
        ids = [findints(h)[0] for h in hrefs][:][:totaln]
        
        repeats = [(k,v) for k,v in Counter(ids).items() if v !=1]
        if len(repeats):    
            pred-"repeats:%d"%(len(repeats),)
            tree-dict(repeats)
        urls = [urlmat%i for i in ids][:]
    
#        hrefss = map(getHrefs,urls,)
        hrefss = mapmt(getHrefs,urls[::-1],pool=8)
#        print Counter(map(len,hs))
        1/0
        
        pblue('Begin to selenium %d pages'%len(ids))
        showurlss = urls
        #showurlss = map(getHrefs,urls)
        js = dicto()
        for rank,(idd,showurls) in enumerate(zip(ids,showurlss)):
            print rank,idd,
            jsonPath = pathjoin(JSON_DIR,str(idd))
            if isfile(jsonPath):
                pass
            j = dicto()
            url = urlmat%idd
            html = gethtml(url)
            #%%
            sp = bs(html)
            introh = sp.find(class_='p-parameter')
            intro = dict([(splitTo2(li.text)) for li in introh.find_all('li')])
            
            infoh = sp.find(class_='Ptable-item')
            if infoh:
                info = dict(zip(getTexts(infoh.find_all('dt')),getTexts(infoh.find_all('dd')),))
                intro.update({'2'+k:v for k,v in info.items()})
        #    time.sleep(.5+2*randfloat())
            ul = sp.find(id="spec-list").ul
            simgurls = ['http:%s'%im['src'] for im in ul.find_all('img',)]
            imgurls = [ton1(u) for u in simgurls]
            imgurl = imgurls[0]
        #    imgs = mapmt(getImg, imgurls)
            
        #    showurls = [ton1(u,1,76) for u in showurls][:15]
        #    showimgs = mapmt(getImg, showurls)
            j.rank,j.id = rank,idd
            j.intro = intro
            j.imgurls = imgurls
            j.title = sp.find(class_='sku-name').text.strip()
#            tree-j
            js[idd] = j
            saveJson(jsonPath, j)
            pblue- 'imgn:%d dict:%d'%(len(j.imgurls),len(j.intro))
#            break
        import analysisJson
        reload(analysisJson)
        
    
    
    
    
    
    
    
