#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os.path
import datetime
import smtplib
import email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_message(from_addr, to_addr, subject, body, mine, attach_file):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr

    body = MIMEText(body)
    msg.attach(body)

    attachment = MIMEBase(mine['type'],mine['subtype'])


    file = open(attach_file['path'], 'rb+')
    attachment.set_payload(file.read())
    file.close()
    email.encoders.encode_base64(attachment)
    msg.attach(attachment)
    attachment.add_header("Content-Dispositon","attachment",filename=attach_file['name'])

    return msg

def sendGmail(from_addr, to_addr, msg):
    smtp = smtplib.SMTP_SSL(host)
    smtp.ehlo()
    smtp.login(username, password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    host = 'smtp.gmail.com'#gmail login
    username, password = 'xxxx@gmail.com', 'password'#gメールアカウントを使うためアドレスとパスワードを入力
    from_addr = "somebody@gmail.com"#メールに表示させる送り主（何でも良い）
    to_addr = " xxxx@xx.com" #送り先のアドレス
    subject = "外出しました。確認してください"#件名
    body = "neko（camera1）20時　url:https://・・・・"#メールの中身
    mine={'type':'image','subtype':'jpeg'}#どんなコンテンツかどんな拡張子か
    attach_file={'name':'neko.jpg','path':'neko.jpg'}#コンテンツのファイル名とパス

    msg = create_message(from_addr, to_addr, subject, body, mine,attach_file)
    sendGmail(from_addr, to_addr, msg)
