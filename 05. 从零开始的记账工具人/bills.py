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
