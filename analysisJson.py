#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:21:57 2018

@author: yanglei
"""
import re


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

from crawlJD import *
tosmall = lambda x:x[::10,::10]
ps = glob(pathjoin(JSON_DIR,'*'))

js = dicto()
for p in ps:
    j = dicto(loadJson(p))
    js[j.id] = j

#[j.intro.update([('id',j.id)]) for j in js.values()]
[j.intro.update([('rank',j.rank)]) for j in js.values()]
[j.intro.update([('url',urlmat%j.id+'')]) for j in js.values()]
[j.intro.update([('title',j.title)]) for j in js.values()]
df = pd.DataFrame([j.intro for j in js.values()],index=[j.id for j in js.values()])
df.sort_values('rank', inplace=True)
DF_P = pathjoin(className,'%s.xlsx'%className)


begin = ['rank','url','title',u'商品名称', ]
count = df.count().sort_values(ascending=False)
l = list(count.index)
map(l.remove, begin)
df = df[begin+l]
writer = pd.ExcelWriter(r'file.xlsx', engine='xlsxwriter',options={'strings_to_urls': True})


df.to_excel(DF_P)


DowloadImg = 0
DowloadShowImg = 1
if __name__ == '__main__' and DowloadImg:
    log = LogLoopTime(list(df.index))
    for ind,row in df.iterrows():
        j = js[ind]
        simgs = []
        name = row[u'商品名称']
        name = validateTitle(name)
        rank = row['rank']
        kind = 'img'
        print colorFormat.r%('rank:%s,%s'%(rank,name,)),
        paths = map(lambda i:pathjoin(IMG_DIR,'%d_%s_%s_sku-%d_%dth.png'%(rank,kind,name,ind,i)), range(len(j.imgurls)))
        if all(map(isfile,paths)):
            log(ind)
            continue
        imgs = mapmt(getImg,j.imgurls,pool=len(j.imgurls))
#        imgs = map(getImg,j.imgurls)
        for path,img in zip(paths,imgs):
            if isfile(path):
                continue
#            print path
#            img = getImg(href,img=True)
            imsave(path,img)
            simgs.append(tosmall(img))
        print path,
        if len(simgs):
            show(simgs)
        log(ind)
        
        
if __name__ == '__main__' and DowloadShowImg:
    log = LogLoopTime(list(df.index))
    for ind,row in list(df.iterrows())[::]:
        j = js[ind]
        url = urlmat%ind
        simgs = []
        name = row[u'商品名称']
        name = validateTitle(name)
        rank = row['rank']
        kind = 'show'
        hrefs = getHrefs(url)
        hrefs = hrefs[:SHOW_IMG_N]
        print colorFormat.r%('rank:%s,%s'%(rank,name,)),
        paths = map(lambda i:pathjoin(IMG_DIR,'%d_%s_%s_sku-%d_%dth.png'%(rank,kind,name,ind,i)),
                    range(len(hrefs)))
        if all(map(isfile,paths)):
            log(ind)
            continue
        if hrefs[0] == 'global':
            pred- '\n\nid:%d is JD global\n'%ind
            tmpp = '%s is JD global.txt'%paths[0]
            openwrite(url,tmpp)
            continue
        hrefs = [ton1(h,1,76) for h in hrefs]
        while 1 :
            try:
                imgs = mapmt(getImg,hrefs,pool=len(hrefs))
                break
            except IOError as e:
                pred-'\n\nmapmt IOError'
                print e
        for path,img in zip(paths,imgs):
            if isfile(path):
                continue
#            print path
#            img = getImg(href,img=True)
            imsave(path,img)
            simgs.append(tosmall(img))
        print path,
        if len(simgs):
            show(simgs)
        log(ind)
#        break
        

















