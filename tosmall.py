# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 18:53:30 2018

@author: yl
"""
from __future__ import unicode_literals

from yllab import *

for bigMod in [0,1,2,3]:
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
    dirr = pathjoin('small',className)
    if not isdir(dirr):
        os.makedirs(dirr)
    ps = glob(pathjoin(className,'img/*'))
    log = LogLoopTime(ps)
    for i,p in enumerate(ps):
        new = pathjoin(dirr, basename(p))
        new = pathjoin(dirr,b+'.jpg')
        if isfile(new):
            print i,'ok'
            continue
        if p[-3:] == 'txt':
            print p
            
            openwrite(openread(p),new)
        elif  p[-3:] == 'png':
            im = imread(p)
            sim = im[::2,::2,]
            b = filename(p)
            imsave(new,sim)
        else:
            pread-p
        print i,
        log(p)
    
    
    