# 京东爬虫

这不是工程项目 只是个人所需 生猛硬糙地写了个爬虫 所有内容仅为了方便日后个人查阅与理解

### 爬的内容：
* milk drink paper noodle 4大类目的销量排行榜前300SKU的详细信息 并自动生成xlsx
* 下载每个SKU京东提供所有的图片
* 下载每个SKU前20张买家秀图片

### 使用技术
* 自动缓存
* selenium 操纵浏览器 or `PhantomJS`
* 免费代理池
* 多线程加快速度

### 使用
1. 先下载并运行 [代理池](https://github.com/jhao104/proxy_pool)
1. 运行crawlJD.py 及其他


### 可复用部分
* 异常类的父类(`.__base__`)来统一`except` 再 `retry`
* `proxy.py` 中可用代理池(`goodList`) 及守护线程(`pushGoodWhile`)对其的维护
* `cache` 设计
* 多线程 `mapmt` 的使用
*  `see(html)` 函数将html保存到`/tmp` 并自动用浏览器打开  来可视化(网页为gbk 的话则乱码)


### 心得
* `requests.get(url)` 的 `.content` 要考虑编码问题 而 `.text` 则自动转换为了 `unicode`
* 爬虫更好的设计模式应该是 `callback` 型,   不过架构得完全重新设计
