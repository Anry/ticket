# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

def sendmail():
    msg_from = 'XXXXX'  # 发送方邮箱
    passwd = 'XXXXX'  # 填入发送方邮箱的授权码
    msg_to = 'XXXXX'  # 收件人邮箱

    subject = "抢到票了"  # 主题
    content = "抢到票了"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except s.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()