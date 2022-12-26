import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent
from linebot.models import TextMessage, TextSendMessage
from linebot.models import LocationMessage, LocationSendMessage
from linebot.models import ImageMessage, ImageSendMessage
from linebot.models import VideoMessage, VideoSendMessage
from linebot.exceptions import LineBotApiError

from linebot.models import QuickReply, QuickReplyButton, MessageAction
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
from pkmgo_assistant import crawler, wther_broadcaster
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

cityName = ''


urlPkgHomePage = 'https://pokemongolive.com'
urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'
urlPkgTrainerClubHomePage = "https://pogotrainer.club"
urlPkgTrainerClubWorldwidePage = "https://pogotrainer.club/?sort=worldwide"

appraise_pattern = r'adh\s[0-9]{1,2}\s[0-9]{1,2}\s[0-9]{1,2}'
weather_info_pattern = r"\[Check \{(.+?)\} weather\]"
location_pattern = r"I'm at ([\u4e00-\u9fff]+)"

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

    
    # init
    if(event.message.text == sm.resp_check_msg_acp()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.teach_msg()))
    elif(event.message.text == "help"):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.teach_msg()))    
    elif(event.message.text == "close"):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.teach_msg()))    
    #prompt IV
    elif(event.message.text == sm.button_iv_msg()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text=sm.button_iv_resp())) 
    # IV
    elif(re.fullmatch(appraise_pattern, event.message.text)):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.recieve_iv_resp(event),
                                                                     quick_reply = QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(label='Continue', text='[計算ＩＶ]')),
                            QuickReplyButton(action=MessageAction(label='Close', text='close'))
                        ]
                    )))
    # activities info
    elif(event.message.text == sm.button_activity_msg()):
        # linebot_api.reply_message(event.reply_token, TextSendMessage(text=sm.button_activity_resp()))
        msg = sm.test_activity_msg()
        linebot_api.reply_message(event.reply_token, msg)
    # add friends
    elif(event.message.text == sm.button_friend_msg()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.button_friend_resp(), 
                                                                     quick_reply = QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(label='Continue', text='[新增好友]')),
                            QuickReplyButton(action=MessageAction(label='Close', text='close'))
                        ]
                    )))
    # prompt location
    elif(event.message.text == sm.button_weather_msg()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.button_weather_resp()))
    # weather & location info
    elif(re.fullmatch(location_pattern, event.message.text)):
        match = re.search(location_pattern, event.message.text)
        # print(f'cityName: {match.group(1)[0:3]}')
        message = match.group(1)[0:3] + ':\n'
        message += wther_broadcaster.getCityWeather(match.group(1)[0:3])
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = message, 
                                                                     quick_reply = QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(label='Continue', text='[近日天氣]')),
                            QuickReplyButton(action=MessageAction(label='Close', text='close'))
                        ]
                    )
                )
            )
    
    elif(event.message.text == sm.button_location_msg()):
        linebot_api.reply_message(event.reply_token, sm.button_location_resp())
    
    #  Linktr
    elif(event.message.text == sm.button_linktr_msg()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text=sm.button_linktr_resp(), 
                                                                     quick_reply = QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(label='Close', text='close'))
                        ]
                    )))
    
    # teach
    elif(event.message.text == sm.ivk_check_msg()):
        linebot_api.reply_message(event.reply_token, sm.check_teaching_msg())
    elif(event.message.text == sm.resp_check_msg_acp()):
        linebot_api.reply_message(event.reply_token, TextSendMessage(text = sm.teach_msg()))
    # Test msg
    # elif(event.message.text == sm.test_msg()):
    #     linebot_api.reply_message(event.reply_token, TextMessage(text=sm.test_msg_resp()))
    #     # linebot_api.reply_message(event.reply_token, TextMessage(text='可以一次傳兩則訊息'))

    

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    # location check
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
            cityName = tokens[-3][0:3]
            print(cityName)
            print(type(cityName))
            
            linebot_api.reply_message(
                event.reply_token, 
                TextSendMessage(
                    text=f'Get location message!\nYour User ID is [ {UserId} ]\n==-==-==-==-==-==-==-==-==-==-==\n'+
                        f'Current location:\n{location.address}\n==-==-==-==-==-==-==-==-==-==-==\n'+
                        f'{round(location.latitude, 6)}, {round(location.longitude, 6)}\n==-==-==-==-==-==-==-==-==-==-==\n'+
                        f'Are you at {tokens[-3]} right?',
                    quick_reply = QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(label='Yes', text=f'I\'m at {tokens[-3][0:3]}')),
                            QuickReplyButton(action=MessageAction(label='No', text='[近日天氣]'))
                        ]
                    )
                )
            )

        
            linebot_api.reply_message(event.reply_token, TextSendMessage(text=f'http://www.google.com/maps/place/{event.message.latitude},{event.message.longitude}'))




if __name__ == '__main__':
    app.run(host="localhost", port=5002)
    # app.run(port=80,debug=True)


    # linebot_api.reply_message(event.reply_token, TextSendMessage(text=''))