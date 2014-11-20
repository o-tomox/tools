# -*- coding: utf-8 -*-

import glob
import smtplib
from datetime import datetime
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

import settings

def count_docs(day=None):
    u'''
    day（日付）に生成された怪文書の数を数える関数
    '''
    if day is None:
        day = datetime.now().strftime("%Y%m%d")

    target_file = "{0}/{1}*.png".format(settings.img_path, day)

    files = glob.glob(target_file)

    return len(files)

def mail(mail_to, num):
    u'''
    指定されたメールアドレスに送信する関数
    '''
    mail_from = "info@o-tomox.com"
    subject = u"怪文書ジェネレータ 定期メール"
    body = u"本日、生成された怪文書は {0} 件です。".format(num)
    msg = create_message(mail_from, mail_to, subject, body, "ISO-2022-JP")
    send(mail_from, mail_to, msg)

def create_message(from_addr, to_addr, subject, body, encoding):
    u'''
    日本語のメッセージを生成する関数
    '''
    msg = MIMEText(body, "plain", encoding)
    msg["Subject"] = Header(subject, encoding)
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Date"] = formatdate()
    return msg

def send(from_addr, to_addr, msg):
    u'''
    実際にメールを送信する関数
    '''
    s = smtplib.SMTP()
    s.connect()
    s.sendmail(from_addr, [to_addr], msg.as_string())
    s.close()

def main():
    u'''
    メイン関数
    '''
    num = count_docs()
    mail(settings.mail_address, num)


if __name__ == "__main__":
    main()
