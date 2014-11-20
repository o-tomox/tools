# -*- coding: utf-8 -*-


import settings

def count_docs(day=None):
    u'''
    day（日付）に生成された怪文書の数を数える関数
    '''
    pass

def mail(mail_to, num):
    u'''
    指定されたメールアドレスに送信する関数
    '''
    pass

def main():
    u'''
    メイン関数
    '''
    num = count_docs()
    mail(settings.mail_address, num)


if __name__ == "__main__":
    main()
