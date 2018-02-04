#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:13:38 2018

@author: yanglei
"""

from __future__ import unicode_literals

from selenium.webdriver.common.by import By
from yllab import *
from bs4 import BeautifulSoup 
bs = BeautifulSoup
import webbrowser as wb
import requests,selenium
from requests import *
rq = requests
import hashlib

md5 = lambda x:hashlib.md5(x).hexdigest()
sleep = time.sleep
url = u'https://item.jd.com/2922989.html'
gg=dicto()
from selenium import webdriver
def utf8(s):
    if isinstance(s,unicode):
        s = s.encode('utf-8')
    return s

def waite(f,t=1):
    while 1 :
        if inBrowser(f):
            return True
        time.sleep(t)
BROWSER = [None]
b = BROWSER
TIME_OUT = 30
def inBrowser(f, browser=None):
    try :
        if f():
            return True
    except selenium.common.exceptions.NoSuchElementException:
        pred- 'waite NoSuchElementException'
        pass
    return False    


def getBrowser():
    BROWSER[0] = webdriver.Chrome()
#    BROWSER[0] = webdriver.PhantomJS()
    BROWSER[0].set_page_load_timeout(TIME_OUT)
    return BROWSER[0]
WebDriver = selenium.webdriver.chrome.webdriver.WebDriver
WebDriver.__exit__ = lambda *l:l[0].close()
WebDriver.__enter__ = lambda self:self
#browser = webdriver.Firefox()
def seleHtml(url,n=30):
    while 1:
        with getBrowser() as browser:
            b = browser
            try:
                browser.get(url)
                html = b.page_source
                return html
            except selenium.common.exceptions.TimeoutException:
                pred- 'TimeoutException'
#                browser.close()
    #            browser.refresh()
                continue
def getHtmlBySe(url,n=30):
    while 1:
        with getBrowser() as browser:
            b = browser
            try:
                browser.get(url)
            except selenium.common.exceptions.TimeoutException:
                pred- 'TimeoutException'
#                browser.close()
    #            browser.refresh()
                continue
            
            for i in range(20):
                sleep(.1)
                js="document.documentElement.scrollTop=%d"%(i*150)
                b.execute_script(js)
            
            sleep(1)
            g.sppj = b.page_source
            
            if inBrowser(lambda:b.find_element_by_class_name('yuyue')):
                pred- '\n\nJD global return empty !!! \n\n\n'
                return ['global',url]
                b.find_element(By.XPATH, '//li[text()="评价"]').click()
#                print u"评价"
                g.li = b.find_element(By.XPATH, '//li[text()="有晒单的评价"]')
                
                raise Exception
                for i in range(10):
                    inb = inBrowser(lambda:b.find_element_by_class_name('comments-item'))
                    if inb:
                        break
                    sleep(1)
                if inb:
                    html = b.page_source
                    sp = bs(html)
                    imgs = sp.find(class_= 'com-table-main').find_all('img',class_='J-thumb-img')
                    imghref = ['http:%s'%img['src'] for img in imgs]
                    return imghref
                continue
            b.find_element(By.XPATH, '//li[text()="商品评价"]').click()
            for i in range(10):
                inb = inBrowser(lambda:b.find_element_by_class_name('percent-con'))
                if inb:
                    break
                sleep(1)
                
            if inb:
                sleep(1)
                b.find_element(By.XPATH, '//a[text()="晒图"]').click()
                
                waite(lambda :b.find_element_by_class_name('J-photo-img'))
                
                for i in range(n//10):
                    sleep(1)
                    b.find_element_by_class_name('J-thumb-next').click()
                
                html = b.page_source
                return html
            pred-'reflash'

def getImgHrefs(url,n=30):
    while 1:
        try :
            html = getHtmlBySe(url,n)
            if isinstance(html,list):
                imghref = html
            else:
                g.html = html
                sp = bs(html)
                gg.sp = sp
                imgs = sp.find(class_='comments-showImgSwitch-wrap').find_all('img')
                imghref = ['http:%s'%img['src'] for img in imgs]
            if len(imghref):
                return imghref[:n]
            pred-'lis is None!!!!'
        except selenium.common.exceptions.WebDriverException as e:
            pred-"WebDriverException:retry"
            g.e = e
            print g.e.__str__()
        except Exception as e:
            pred-"retry"
            g.e = e
            print g.e.__str__()

#browser.close()
if __name__ == '__main__':
    hrefs = getImgHrefs(url)
    print len(hrefs),hrefs[:2]