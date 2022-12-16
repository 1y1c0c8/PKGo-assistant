import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent
from linebot.models import TextMessage, TextSendMessage
from linebot.models import LocationMessage, LocationSendMessage
from linebot.models import ImageMessage, ImageSendMessage
from linebot.models import VideoMessage, VideoSendMessage

# For crawler
from crawler import getInfoTitle, getActivityUrl
# For GPS
from geopy.geocoders import Nominatim
# # For OpenAI
# import openai
# For .env
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
token = os.getenv("channel_access_token")
secret = os.getenv("channel_secret")
# Chennel access token
linebot_api = LineBotApi(token)
# Channel secret
handler = WebhookHandler(secret)


urlPkgHomePage = 'https://pokemongolive.com'
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
    UserId = str(event.source.user_id)
    print(UserId)


    if(event.message.text == '[計算ＩＶ]'):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入以下格式：-m 攻擊數值 防禦數值 HP數值'))
        linebot_api.reply_message(event.reply_token, TextSendMessage(text='1'))
        # linebot_api.reply_message(event.reply_token, TextSendMessage(text='2'))
        # linebot_api.reply_message(event.reply_token, TextSendMessage(text='3'))

        # if(event.message.text):
        #     cmd = event.message.text
        #     if "-m" in cmd :
        #         linebot_api.reply_message(event.reply_token, TextSendMessage(text='-m'))

    elif(event.message.text == '[最近活動]'):
        titles = getInfoTitle(urlPkgNewsPage)
        blocks = getActivityUrl(urlPkgNewsPage)

        titles_in_string_format = "⌛【Activities】⌛"

        index=0
        # {index+1}.
        for title in titles[:3]:
            titles_in_string_format += f'{title.string}{urlPkgHomePage}{blocks[index]["href"]}\n'
            # titles_in_string_format += '==========================='
            titles_in_string_format += '==-==-==-==-==-==-==-==-==-==-=='
            index += 1

        linebot_api.reply_message(event.reply_token, TextMessage(text=titles_in_string_format))

    elif(event.message.text == '[連結地圖]'):
        linebot_api.reply_message(event.reply_token, TextMessage(text='請發送位置資訊📍'))
    elif(event.message.text == "測試訊息"):
        linebot_api.reply_message(event.reply_token, TextMessage(text='做動ing'))
        # linebot_api.reply_message(event.reply_token, TextMessage(text='可以一次傳兩則訊息'))
    elif(event.message.text == "甩頭鸚鵡"):
        # image_message = ImageSendMessage(
        #     original_content_url= "https://imgur.com/gallery/cf8cZdA",
        #     preview_image_url= "https://imgur.com/gallery/cf8cZdA"
        # )
        video_message = VideoSendMessage(
            original_content_url= "https://youtu.be/f67WbPVPIWc",
            preview_image_url= "https://youtu.be/f67WbPVPIWc"
        )
        linebot_api.reply_message(event.reply_token, video_message)



@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    if event.type == 'message':
        if event.message.type == 'location':
            UserId = str(event.source.user_id)
            print(UserId)

            geolocator = Nominatim(user_agent=f'{UserId}')
            
            location = geolocator.reverse(f'{event.message.latitude}, {event.message.longitude}')
            linebot_api.reply_message(event.reply_token, TextSendMessage(
                text=f'Get location message!\nYour User ID is [ {UserId} ]\n==-==-==-==-==-==-==-==-==-==-==\nCurrent location:\n{location.address}\n==-==-==-==-==-==-==-==-==-==-==\n{round(location.latitude, 6)}, {round(location.longitude, 6)}\n==-==-==-==-==-==-==-==-==-==-=='))

            # linebot_api.reply_message(event.reply_token, TextSendMessage(text=f'http://www.google.com/maps/place/{event.message.latitude},{event.message.longitude}'))




if __name__ == '__main__':
    app.run(host="localhost", port=8000)


    # linebot_api.reply_message(event.reply_token, TextSendMessage(text=''))