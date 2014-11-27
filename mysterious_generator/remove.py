# -*- coding: utf-8 -*-

import glob
import datetime
import os

import settings

def remove(limitation="9999"):
    u'''
    削除する関数
    '''
    
    target_file = "{0}/*.png".format(settings.img_path)
    limitation = "{0}/{1}".format(settings.img_path, limitation)

    files = glob.glob(target_file)

    for afile in files:
        if afile < limitation:
            os.system("rm -f {0}".format(afile))

def main():
    u'''
    メイン関数
    '''
    
    limitation = (datetime.date.today() - datetime.timedelta(7)).strftime("%Y%m%d")
    remove(limitation)


if __name__ == '__main__':
    main()
