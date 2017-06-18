# coding:utf-8

import smtplib
import poplib
import email
from email import parser
from email.mime.text import MIMEText
from email.header import decode_header
import os
import time


"""
此函数用来重置邮箱里面的内容，如果不重置，下次打开程序就会立即获取邮箱里面的命令（关机）
"""


def Reset():
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('kightjohn666@sina.com', 'wonengxing')
    content = MIMEText('')
    me = 'kightjohn666@sina.com'
    to = 'kightjohn666@sina.com'
    content['Subject'] = 'reset'
    content['To'] = 'kightjohn666@sina.com'
    content['From'] = 'kightjohn666@sina.com'
    content['Date'] = '2017-6-19'
    sent.sendmail(me, to, content.as_string())
    sent.close()

"""
用POP3来读取远程邮箱内容作为命令
"""
while True:
    host = 'pop.sina.com'
    duyoujian = poplib.POP3_SSL(host)
    duyoujian.user('kightjohn666@sina.com')
    duyoujian.pass_('wonengxing')

    # Get messages from server:
    # 获得邮件
    emails = [duyoujian.retr(i) for i in range(1, len(duyoujian.list()[1]) + 1)]
    # print len(emails)
    print emails
    print '\n\n'

    # Concat message pieces:
    messages = ["\n".join(mssg[1]) for mssg in emails]
    print messages
    print '\n\n'

    # 分析
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    print messages
    print '\n\n'

    # 邮件不为空
    if len(messages) > 0:
        # 只取最新的邮件
        titt = messages[len(messages) - 1].get('subject').strip()
        if titt == 'guanji':
            print titt
            Reset()
            os.system('shutdown -s -f -t 60')
            break

