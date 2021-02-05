import setuptool.py #setuptool.pyから必要変数を取得
import time
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http

class GDop():
    def __init__(self):
        pass

    def savefiles(self):#SendFiles内のファイルをすべてGDに送信します
        pass

    def sendfiles(self):#GD_to_files内にGDのデータを全取得していれます。いわゆるgd間同期
        pass
if __name__ == '__main__':
    op = GDop()
