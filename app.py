from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from crawler import getInfoTitle

app = Flask(__name__)

# Chennel access token
linebot_api = LineBotApi('aWTrEwZVA3XLmWzRnyYM0akO2YA8pkbROsAtAI69ZENz0VwF26vRel1b7PAPs5GaaU5+fe70YHFBqi31PE0Q3hXFTGtHC1FuXsyKYfOQ3JI/xyip3OUjrjhubSrgk5gyiAYf7cLIadEQ7wQc0iQFNQdB04t89/1O/w1cDnyilFU=')
# Channel secret
handler = WebhookHandler('e0c3a441bef0e556f6f5717f0b61bbd4')

urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'


# @app.route('/')
# def homepage():
#     return 'Success!'

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text = True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if(event.message.text == '[計算ＩＶ]'):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入以下格式：-m 攻擊數值 防禦數值 HP數值'))
    elif(event.message.text == '[最近活動]'):
        linebot_api.reply_message(event.reply_token, TextMessage(text='最近的活動如下：'))

        titles = getInfoTitle(urlPkgNewsPage)

        

        for title in titles[:3]:
            linebot_api.reply_message(event.reply_token, TextMessage(text='x'))

    elif(event.message.text == '[連結地圖]'):
        linebot_api.reply_message(event.reply_token, TextMessage(text='請將裝置的定位開啟'))
        
        # Check GPS



        # linebot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))




if __name__ == '__main__':
    app.run()