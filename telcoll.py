import os
from twilio.rest import Client
import time



def coll():
    account_sid = (os.environ['SID']) # 環境設定で書き換え
    auth_token  = (os.environ['TOKEN'])  # 環境設定で書き換え

    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to=(os.environ['TO']),
        from_=(os.environ['FROM']),
        url="http://demo.twilio.com/docs/voice.xml" #サーバー起動時に書き換えておく
    )

    print('成功' + call.sid)
    return
        

