#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:28:27 2018

@author: yanglei
"""
from __future__ import unicode_literals

from crawlJD import *
from yllab import *
from bs4 import BeautifulSoup 
bs = BeautifulSoup
import webbrowser as wb
import requests
from requests import *
rq = requests
import hashlib,json
from collections import Counter

md5 = lambda x:hashlib.md5(x).hexdigest()

def saveJson(path, dic):
    with open(path,'w') as f:
        json.dump(dic,f)
def loadJson(path,):
    with open(path,) as f:
        return json.load(f)
        
def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content
def gett(url,img=False):
    while 1:
        try:
            time.sleep(TIME_GAP+randfloat()*TIME_GAP)
#            return seleHtml(url)
            r = rq.get(url,timeout=5,proxies=proxies)
            g.r = r
            return r.content
        except (rq.exceptions.RequestException)as e:
            pred-'requests Error!!'
            print e
            pass

def getGood(*l):
    while 1:
        proxy =  requests.get("http://127.0.0.1:5010/get/").content
        try:
            r = requests.get('http://baidu.com',proxies={"http": "http://{}".format(proxy)},timeout=.5)
            g.c = r.content
            if "url=http://www.baidu.com/" in tounicode(r.content):
                return proxy
        except requests.exceptions.RequestException as e:
#                pred-'find good proxy error %s'%proxy
                pass
proxies = {
  "http": "http://127.0.0.1:1080",
}

goodpath = 'goodProxy.list'


goodp =  openread(goodpath).split()
goodList = goodp if len(goodp) else ["127.0.0.1:1080","127.0.0.1:1088"]

LENN = 50
def pushGood():
    l = goodList
    n = len(l)
    if LENN != n:
        new = mapmt(getGood,[0]*abs(LENN-n),pool=abs(LENN-n))
        goodList.extend(new)
    

def pushGoodWhile():
    while 1:
        pushGood()
        time.sleep(1)
setTimeOut(pushGoodWhile)

            


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
    if proxy in goodList :
        goodList.remove(proxy)

def getOne():
    l = goodList
    n = len(l)
    if not n:
        pred - 'waite pushGood!'
        setTimeOut(pushGood)
    while 1:
        try:
            return l[0]
        except IndexError:
            pass
        time.sleep(.1)
    

import random
GOOD_PROXY = True*0
def proxyget(url,**kv):
    # ....
#    proxy = get_proxy()
    proxy = getOne()
    for i in range(5):
        retry_count = 2
        while retry_count > 0:
            try:
                html = requests.get(url,proxies={"http": "http://{}".format(proxy)},**kv)
                if proxy not in goodp:
                    with open(goodpath,'a') as f:
                        f.write(proxy+'\n')
                return html
            except requests.exceptions.RequestException as e:
                retry_count -= 1
                pred-'proxy error %s'%proxy
                print e
        delete_proxy(proxy)
        proxy = getOne()

    return requests.get(url, proxies={"http": "http://{}".format(proxy)},**kv)
    

if __name__ == '__main__':
    print len(goodp)
    for i in range(10):
        print i,
        html = proxyget('http://baidu.com', timeout=1)
    print 'goodpath len:',len(openread(goodpath).split())



#    openwrite('\n'.join((Counter(openread(goodpath).split())).keys()),goodpath)


