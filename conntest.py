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


import mysql.connector

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


conn = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = 'yuuto1207',
    database = 'test_database'
)

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

# 接続できているかどうか確認
print(conn.is_connected())

cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS `test_table`")#テーブル作成前にテーブルが存在していれば作成前に削除する
cur.execute("""CREATE TABLE IF NOT EXISTS `test_table` (
    `id` int(11) NOT NULL,
    `name` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` int(11) NOT NULL,
    PRIMARY KEY (id)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")#テーブル作成

#データを追加
cur.execute("INSERT INTO test_table VALUES(%s,%s,%s)",(1,'camera1',20))



cur.close()
conn.commit()
conn.close()#pythonは自動的にファイルクローズ、ＤＢコミットしないためクローズ/コミット処理をかく

url = "https://www.apple.com/jp/"


#本当は分岐させるが今はデータ追加時メール送信
if __name__ == '__main__':
    host = 'smtp.gmail.com'
    username, password = 'qwertyuuto@gmail.com', 'yuuto1207'#Gメールアカウントを使ってメール送信
    from_addr = "somebody@gmail.com"#送り主（何でも良い）
    to_addr = " yuutoqwert@icloud.com" #送り先
    subject = "動物が外出しました。確認してください"#件名をかく
    body = "neko（camera1）20時　url:{}".format(url)#urlを埋め込んだメール内容をかく
    mine={'type':'image','subtype':'jpeg'}#コンテンツのタイプ
    attach_file={'name':'neko.jpg','path':'neko.jpg'}#コンテンツのファイル名とファイルの場所をかく

    msg = create_message(from_addr, to_addr, subject, body, mine,attach_file)
    sendGmail(from_addr, to_addr, msg)
