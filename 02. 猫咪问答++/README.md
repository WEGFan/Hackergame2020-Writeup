# 猫咪问答++

> 以下编程语言、软件或组织对应标志是哺乳动物的有几个？  
> Docker，Golang，Python，Plan 9，PHP，GNU，LLVM，Swift，Perl，GitHub，TortoiseSVN，FireFox，MySQL，PostgreSQL，MariaDB，Linux，OpenBSD，FreeDOS，Apache Tomcat，Squid，openSUSE，Kali，Xfce.

好麻烦，先跳过了

> 第一个以信鸽为载体的 IP 网络标准的 RFC 文档中推荐使用的 MTU (Maximum Transmission Unit) 是多少毫克？

搜索第一个以信鸽为载体的 IP 网络标准的 RFC 文档，可以找到对应的文档是 RFC 1149，搜索文档编号找到原文页面 <https://tools.ietf.org/html/rfc1149>，打开后搜索 MTU，找到 “A typical MTU is 256 milligrams”，所以答案是 256

> USTC Linux 用户协会在 2019 年 9 月 21 日自由软件日活动中介绍的开源游戏的名称共有几个字母？

搜索 USTC Linux 用户协会，找到 <https://news.ustclug.org/>，往下翻找到标题为 2019 软件自由日中国科大站的活动记录 <https://news.ustclug.org/2019/09/2019-sfd-ustc/>，在最后可以找到 “最后一项是李文睿同学介绍了开源游戏 Teeworlds”，共有 9 个字母，所以答案是 9

> 中国科学技术大学西校区图书馆正前方（西南方向） 50 米 L 型灌木处共有几个连通的划线停车位？

打开百度地图，搜索中国科学技术大学西校区图书馆，然后打开全景功能数一下即可 <https://j.map.baidu.com/8f/6RS>，所以答案是 9

> 中国科学技术大学第六届信息安全大赛所有人合计提交了多少次 flag？

在比赛首页下方找到学生Linux用户协会第六届信息安全大赛完美收官的新闻稿 <https://young.ustc.edu.cn/2020/0727/c17198a439807/page.htm>，打开后找到 “比赛期间所有人合计提交了 17098 次 flag”，所以答案是 17098

最后剩下第一题，写个脚本直接爆破即可，答案是 12

```python
# -*- coding: utf-8 -*-
import re

import requests

SESSION = '' or input('session: ')

count = len('Docker，Golang，Python，Plan 9，PHP，GNU，LLVM，Swift，Perl，GitHub，TortoiseSVN，FireFox，MySQL，PostgreSQL，MariaDB，Linux，OpenBSD，FreeDOS，Apache Tomcat，Squid，openSUSE，Kali，Xfce'.split('，'))

for i in range(count + 1):
    answers = [i, 256, 9, 9, 17098]
    response = requests.post(
        'http://202.38.93.111:10001',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        cookies={
            'session': SESSION
        },
        data={
            f'q{i + 1}': answer
            for (i, answer) in enumerate(answers)
        }
    )
    flag = re.search(r'flag{.*?}', response.text)
    if flag:
        print(f'answer is {i}')
        print(flag.group())
        break
```
