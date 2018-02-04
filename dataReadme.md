爬好的图片已上传好了 https://drive.google.com/drive/u/1/folders/1r3DnFD3_Ew4pdISZQLtNQhZ0NPlghLTm
在每个文件夹下 对应名称的zip里面 解压后如图


我爬取了每个SKU的京东自己的图片 以及 20张买家秀图片 
图片命名规则：
    '%d_%s_%s_sku-%d_%dth.png'%(rank,kind,name,id,i)
说明：
    rank: 销量排名
    kind: `img` or `show`，京东自己的图片 或 买家秀
    name: 商品名称
    id: 京东的SKU
    i: 该SKU的第几张

图片有点多 对于每个SKU的 大家从京东自己的图和买家秀图中 各选一张最好的复制出来即可

补充： 
    1. 少量图比较特殊 我的代码没有下载到高清版 需要人为整理 下载高清版本(下载后注意命名规范)
    2. 商品页的标题已经加入 .xlsx 文件
