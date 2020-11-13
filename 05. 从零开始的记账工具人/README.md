# 从零开始的记账工具人

首先为了方便处理数据，将下载下来的文件在 Excel 里转换成 .csv 格式

然后使用 Python 的 [cn2an](https://pypi.org/project/cn2an/) 库进行数字转换，不过目前这个库还不支持大写人民币到数字的转换，需要自己分割单位后处理

注意转换成 .csv 文件后在 Python 里打开文件的编码问题，我这里是 GB2312，不同电脑会不一样（可能直接省略 `encoding` 参数用系统默认编码也行？）

最后输出的结果会有浮点数的误差，直接保留两位小数即可

```python
# -*- coding: utf-8 -*-
import csv
import re

import cn2an

ans = 0

with open('./bills.csv', 'r', encoding='gb2312') as f:
    reader = csv.DictReader(f)
    for row in reader:
        (price, num) = row.values()
        match = re.search(r'((.*?)元)?((.*?)角)?((.*?)分)?', price)
        (yuan, jiao, fen) = [match.group(i) or '零' for i in [2, 4, 6]]
        price_num = sum(cn2an.cn2an(v, 'smart') / 10 ** i for (i, v) in enumerate([yuan, jiao, fen]))
        ans += price_num * int(num)

print('flag{%.2f}' % ans)
```
