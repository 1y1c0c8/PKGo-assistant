import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent
from linebot.models import TextMessage, TextSendMessage
from linebot.models import LocationMessage, LocationSendMessage
from linebot.models import ImageMessage, ImageSendMessage
from linebot.models import VideoMessage, VideoSendMessage
from linebot.models import QuickReply, QuickReplyButton, MessageAction
from linebot.exceptions import LineBotApiError

# For crawler
# from crawler import getInfoTitle, getActivityUrl, mergeInfo
# For GPS
from geopy.geocoders import Nominatim
# # For OpenAI
# import openai
# For .env
from dotenv import load_dotenv
# For expression
import re

from pkmgo_assistant import appraise as aps
from pkmgo_assistant import crawler
from pkmgo_assistant import speaksman as sm

# from env import *

app = Flask(__name__)

load_dotenv()
token = os.getenv("channel_access_token")
secret = os.getenv("channel_secret")
project_url = os.getenv("project_url")

# Chennel access token
linebot_api = LineBotApi(token)
# Channel secret
handler = WebhookHandler(secret)


urlPkgHomePage = 'https://pokemongolive.com'
urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'
urlPkgTrainerClubHomePage = "https://pogotrainer.club"
urlPkgTrainerClubWorldwidePage = "https://pogotrainer.club/?sort=worldwide"

appraise_pattern = r'[0-9]{1,2}\s[0-9]{1,2}\s[0-9]{1,2}'

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
    # print(UserId)

    if(event.message.text == sm.ivk_check_msg()):
        linebot_api.reply_message(event.reply_token, sm.check_teaching_msg())
    elif(event.message.text == sm.resp_check_msg_acp()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.teach_msg()))
    # IV
    elif(event.message.text == sm.button_iv_msg()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text=sm.button_iv_resp()))
    # return IV
    elif(re.fullmatch(appraise_pattern, event.message.text)):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.recieve_iv_resp(event)))
    # Activities
    elif(event.message.text == sm.button_activity_msg()):
        # linebot_api.reply_message(event.reply_token, TextSendMessage(text=sm.button_activity_resp()))
        msg = sm.test_activity_msg()
        linebot_api.reply_message(event.reply_token, msg)
    
    # elif(event.message.text == '[連結地圖]'):
    #     linebot_api.reply_message(event.reply_token, TextMessage(text='請發送位置資訊📍'))
    
    # Freinds
    elif(event.message.text == sm.button_friend_msg()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.button_friend_resp()))
    
    elif(event.message.text == sm.button_weather_msg()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.button_weather_resp()))
    # Location
    elif(event.message.text == sm.button_location_msg()):
        linebot_api.reply_message(event.reply_token, sm.button_location_resp())
        # txt = TextSendMessage(text= str(project_url+"/static/Me_at_the_zoo.mp4"))
        # linebot_api.reply_message(event.reply_token, txt)
    
    elif(event.message.text == sm.recieve_right_location_msg):
        print('city correct')
        linebot_api.reply_message(
            event.reply_token, 
            TextSendMessage(
                text=f'Check recent weather or else?',
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(action=MessageAction(label='Weather', text='[Check weather]')),
                        QuickReplyButton(action=MessageAction(label='Else', text='[Check else]'))
                    ]
                )
            )
        )
    
    elif(event.message.text == sm.recieve_wrong_location_msg):
        linebot_api.reply_message(event.reply_token, TextMessage(text='請再次發送位置資訊📍'))
    
    #  Linktr
    elif(event.message.text == sm.button_linktr_msg()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text=sm.button_linktr_resp()))
    # Test msg
    elif(event.message.text == sm.test_msg()):
        linebot_api.reply_message(event.reply_token, TextMessage(text=sm.test_msg_resp()))
        # linebot_api.reply_message(event.reply_token, TextMessage(text='可以一次傳兩則訊息'))
    # Sticker
    elif(event.message.text == sm.test_msg_sticker()):
        linebot_api.reply_message(event.reply_token, sm.test_msg_sticker_resp())
    # test-Template
    elif(event.message.text == sm.test_template_msg()):
        linebot_api.reply_message(event.reply_token, sm.test_template_msg_resp())

    

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    if event.type == 'message':
        if event.message.type == 'location':
            # print('Location Message')
            UserId = str(event.source.user_id)
            print(UserId)

            geolocator = Nominatim(user_agent=f'{UserId}')
            
            location = geolocator.reverse(f'{event.message.latitude}, {event.message.longitude}')
            
            # print(f'location.address: {location.address}')
            # print(type(location.address))
            
            tokens = []
            tokens = location.address.split()
            # for token in tokens:
            print(tokens[-3])
            
            linebot_api.reply_message(
                event.reply_token, 
                TextSendMessage(
                    text=f'Get location message!\nYour User ID is [ {UserId} ]\n==-==-==-==-==-==-==-==-==-==-==\n'+
                        f'Current location:\n{location.address}\n==-==-==-==-==-==-==-==-==-==-==\n'+
                        f'{round(location.latitude, 6)}, {round(location.longitude, 6)}\n==-==-==-==-==-==-==-==-==-==-==\n'+
                        f'Are you at {tokens[-3]} right?',
                    quick_reply = QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(label='Yes', text='[City correct]')),
                            QuickReplyButton(action=MessageAction(label='No', text='[City wrong]'))
                        ]
                    )
                )
            )

        
            linebot_api.reply_message(event.reply_token, TextSendMessage(text=f'http://www.google.com/maps/place/{event.message.latitude},{event.message.longitude}'))




if __name__ == '__main__':
    # app.run(host="localhost", port=8010)
    app.run(host = '0.0.0.0', port=5002, debug=True)


    # linebot_api.reply_message(event.reply_token, TextSendMessage(text=''))