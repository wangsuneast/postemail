#!/usr/bin/python
#-*-coding:UTF-8-*-
import json 
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from conf import confs
c =  confs("mail")
 
def send_mail(receve, mail_subject, mail_context):
    status = {}
    mail_user = c["sender"]
    mail_pass = c["password"]
    mail_host = c["host"]
    mail_port = c["port"]
    msg = MIMEMultipart()
    msg['From'] = mail_user
    msg['To'] = receve
    msg['Subject'] = mail_subject
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
    txt = MIMEText(mail_context, "plain", "utf-8")
    msg.attach(txt)
    try: 
        smtp = smtplib.SMTP()
        smtp.connect('{}:{}'.format(mail_host, mail_port))
        smtp.login(mail_user, mail_pass) 
        smtp.sendmail(mail_user, receve, msg.as_string())
        smtp.quit()
        status["code"] = True
        status["msg"]  = ""
        status["data"] = "发送成功"
        return json.dumps(status, ensure_ascii=False)
    except Exception as e:
        status["code"] = False
        status["msg"]  = "发送失败"
        status["data"] = {}
        return json.dumps(status, ensure_ascii=False)
 
if __name__ == '__main__':
    import sys
    receve = sys.argv[1]
    mail_subject = sys.argv[2]
    mail_context = sys.argv[3]
    print send_mail(receve, mail_subject, mail_context)
