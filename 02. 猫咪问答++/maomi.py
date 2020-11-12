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
