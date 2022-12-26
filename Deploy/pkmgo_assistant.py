import requests, bs4 
from linebot.models import TextSendMessage, VideoSendMessage, StickerSendMessage
from linebot.models import TemplateSendMessage
from linebot.models import ButtonsTemplate, MessageTemplateAction
from linebot.models import CarouselTemplate, CarouselColumn, URIAction, MessageAction
from linebot.models import QuickReply, QuickReplyButton

import os
from dotenv import load_dotenv
from linebot.exceptions import LineBotApiError


urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'
urlPkgHomePage = 'https://pokemongolive.com'
urlPkgTrainerClubHome = "https://pogotrainer.club"
urlPkgTrainerClubWorldwide = "https://pogotrainer.club/?sort=worldwide"

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-01E5C04E-C74A-40E3-B75A-B07D9AFBCF84&format=JSON'
data = requests.get(url)
data_json = data.json()
city_cor = {
        '嘉義縣':0, '新北市':1, '嘉義市':2, 
        '新竹縣':3, '新竹市':4, '臺北市':5, 
        '臺南市':6, '宜蘭縣':7, '苗栗縣':8, 
        '雲林縣':9, '花蓮縣':10, '臺中市':11, 
        '臺東縣':12, '桃園市':13, '南投縣':14,
        '高雄市':15, '金門縣':16, '屏東縣':17,
        '基隆市':18, '澎湖縣':19, '彰化縣':20,
        '連江縣':21
    }


load_dotenv()
project_url = os.getenv("project_url")


class appraise:
    def aps_compute(tokens):

        total = int(tokens[0])+int(tokens[1])+int(tokens[2])
        
        if(total == 45):
            return 100
        elif(total<45 and total>=43):
            return 10+total*2
        elif(total<43 and total>=39):
            return 10+total*2-1
        elif(total<39 and total>=34):
            return 10+total*2-2
        elif(total<34 and total>=30):
            return 10+total*2-3
        elif(total<30 and total>=25):
            return 10+total*2-4
        elif(total<25 and total>=21):
            return 10+total*2-5
        elif(total<21 and total>=16):
            return 10+total*2-6
        elif(total<16 and total>=12):
            return 10+total*2-7
        elif(total<12 and total>=7):
            return 10+total*2-8
        elif(total<7 and total>=3):
            return 10+total*2-9
        elif(total<3 and total>0):
            return 10+total*2-10

    def star_check(iv):
        if(iv < 48.9):
            return '☆☆☆'
        elif(iv < 64.4):
            return '★☆☆'
        elif(iv < 80):
            return '★★☆'
        elif(iv < 97.8):
            return '★★★'
        else:
            return '  ♛  '

class crawler():
    def getInfoTitle(url):
        requestGet = requests.get(url)
        html = bs4.BeautifulSoup(requestGet.text, "html.parser")
        
        titles = html.find_all("div", class_="blogList__post__content__title")

        return titles
            

    def getActivityUrl(url):
        requestGet = requests.get(url)
        html = bs4.BeautifulSoup(requestGet.text, "html.parser")

        blocks = html.find_all("a", class_='blogList__post')

        return blocks

    def getActivityContentUrl(url):
        requestGet = requests.get(url)
        html = bs4.BeautifulSoup(requestGet.text, "html.parser")

        links = html.find_all("a", class_ ='blogList__post')
        
        for link in links:
            print(link.herf())

    def getActivityImg(url):
        requestGet = requests.get(url)
        html = bs4.BeautifulSoup(requestGet.text, "html.parser")
        imgs = html.find_all("img", class_="image")

        return imgs


    def getTrainerNames(url):
        requestGet = requests.get(urlPkgTrainerClubWorldwide)
        html = bs4.BeautifulSoup(requestGet.text, "html.parser")

        userNames = html.find_all("h4", class_='media-heading')

        return userNames

    def getTrainerID(url):
        requestGet = requests.get(urlPkgTrainerClubWorldwide)
        html = bs4.BeautifulSoup(requestGet.text, "html.parser")

        userIDs = html.find_all("a", class_="TCLink")

        for userID in userIDs:
            userID = userID.text

        return userIDs[:3]

    def mergeInfo():
        userNames = crawler.getTrainerNames(urlPkgTrainerClubWorldwide)
        userIDs = crawler.getTrainerID(urlPkgTrainerClubWorldwide)

        userInfos = []

        for index in range(3):
            userInfos.append(str(userNames[index].text)+'\n'+str(userIDs[index].text))
            
        INFO = f'㊝【Trainers】㊝\n{userInfos[0]}\n==-==-==-==-==-==\n{userInfos[1]}\n==-==-==-==-==-==\n{userInfos[2]}\n==-==-==-==-==-=='
        return INFO

class tailor:
    def trimed(string, maxLen):
        if(len(string) <= maxLen):
            return string
        else:
            return string[:maxLen-5]+'...'

class wther_broadcaster():
    
    def getCityWeather(city):
        # print(data_json['records']['location'][city_cor[cityName]]['weatherElement'][1]['time'][2]['parameter']['parameterName'])
        weatherInfos = {}
        for cityInfo in data_json['records']['location']:
            cityName = cityInfo['locationName']
            for feature in cityInfo['weatherElement']:
                weather = feature['elementName']

                if cityName not in weatherInfos:
                    weatherInfos[cityName] = {weather: feature}

                if weather not in weatherInfos[cityName]:
                    weatherInfos[cityName][weather] = feature
        weather = "CI"
       
        elementName = weatherInfos[city]["CI"]["elementName"]
        print(elementName)
        time = weatherInfos[city]["CI"]["time"]
        message = ''
        for info in time:
            st = info['startTime']
            et = info["endTime"]
            ds = info['parameter']['parameterName']
            message += f'from {st}\nto {et}\n{ds}\n'
        message += '\b'
        return message
        # print(f'{city}\n\t{weatherInfos[city]["CI"]}')
        
        
        
    

class speaksman:

    def ivk_check_msg():
        return "教學"

    def resp_check_msg_acp():
        return ":好啊笑死"

    def resp_check_msg_den():
        return ":你也把比雕丟在常磐森林嗎？"

    # 靠北喔圖怎麼無法顯示
    def check_teaching_msg():
        message = TemplateSendMessage(
            alt_text="New-User-Msg",
            template=ButtonsTemplate(
                title="前面出現了奇怪的人...",
                text="是否願意接受真新鎮康妮的挑戰？",
                # thumbnail_image_url="https://github.com/1y1c0c8/PKGo-assistant/blob/main/src/Chain-of-Kenny_trimed.png",
                thumbnail_image_url="https://github.com/1y1c0c8/PKGo-assistant/blob/main/src/RR_QRcode.png",
                actions=[
                    MessageTemplateAction(
                        label="好",
                        text=":好啊笑死"
                    ),
                    MessageTemplateAction(
                        label="不要",
                        text=":你也把比雕丟在常磐森林嗎？"
                    )
                ]
            )

        )
        return message

    def teach_msg():
        return "打開圖文選單:\n\t\t計算機圖示->計算寶可夢IV\n\t\t心電圖圖示->查看最近活動\n\t\t定位點圖示->正常功能/彩蛋\n\t\t三個人圖示->顯示三個訓練師ID\n\t\t晴雲雨圖示->取得附近天氣資料\n\t\tlinktr圖示->查看製作者資料\n輸入help以查看指令說明"

# ============================

    def button_iv_msg():
        return "[計算ＩＶ]"
    
    def button_activity_msg():
        return "[最近活動]"

    def button_location_msg():
        return "[連結地圖]"

    def button_friend_msg():
        return "[新增好友]"

    def button_weather_msg():
        return "[近日天氣]"
    
    def button_linktr_msg():
        return "[ＩＮＦＯ]"


    def recieve_right_location_msg():
        return '[City correct]'
    def recieve_wrong_location_msg():
        return '[City wrong]'
    def request_check_weather(cityName):
        return f"[Check {cityName} weather]"
    def request_check_else(cityName):
        return f"[Check {cityName} info]"
    
    def city_weather_info(cityName):
        wther_broadcaster.getCityWeather(cityName)
        
    
# ============================
    def button_iv_resp():
        return "請輸入以下格式：adh 攻擊數值 防禦數值 HP數值"

    def recieve_iv_resp(event):
        tokens = event.message.text.split()
        pkm_iv = appraise.aps_compute(tokens[1:4])
        star = appraise.star_check(pkm_iv)
        
        return  f'⭐【ＩＶ】⭐\nThis pokemn\'s IV is {star} {pkm_iv} !'

    def button_activity_resp():
        titles = crawler.getInfoTitle(urlPkgNewsPage)
        blocks = crawler.getActivityUrl(urlPkgNewsPage)

        titles_in_string_format = "⌛【Activities】⌛"

        index=0
        # {index+1}.
        for title in titles[:3]:
            titles_in_string_format += f'{title.string}{urlPkgHomePage}{blocks[index]["href"]}\n'
            titles_in_string_format += '==-==-==-==-==-==-==-==-==-==-=='
            index += 1
        
        return titles_in_string_format

    # 圖、第二個title
    def test_activity_msg():
        titles = crawler.getInfoTitle(urlPkgNewsPage)
        blocks = crawler.getActivityUrl(urlPkgNewsPage)
        imgs = crawler.getActivityImg(urlPkgNewsPage)

        links = imgs[2:5]
    
        requestGet1 = requests.get(f'{urlPkgHomePage}{blocks[0]["href"]}')
        html1 = bs4.BeautifulSoup(requestGet1.text, "html.parser")
        try:
            content1 = html1.find("div", class_ = 'blogPost__post__body')
            act1 = CarouselColumn(
                thumbnail_image_url=imgs[2]["src"],
                title = tailor.trimed(titles[0].string, 40),
                # text = tailor.trimed(content1.text, 50),
                text = tailor.trimed(content1.text, 55),
                actions=[
                    URIAction(
                        label="More info...",
                        uri= f'{urlPkgHomePage}{blocks[0]["href"]}'
                    )
                ]
            )
        except:
            act1 = CarouselColumn(
                thumbnail_image_url=imgs[2]["src"],
                title = tailor.trimed(titles[0].string, 40),
                text = '$ 請點擊More info...以查看更多',
                actions=[
                    URIAction(
                        label="More info...",
                        uri= f'{urlPkgHomePage}{blocks[0]["href"]}'
                    )
                ]
            )


        requestGet2 = requests.get(f'{urlPkgHomePage}{blocks[1]["href"]}')
        html2 = bs4.BeautifulSoup(requestGet2.text, "html.parser")
        try:
            content2 = html2.find("div", class_ = 'blogPost__post__body')
            act2 = CarouselColumn(
                thumbnail_image_url=imgs[3]["src"],
                title = tailor.trimed(titles[1].string, 40),
                text= tailor.trimed(content2.text, 55),
                actions=[
                    URIAction(
                        label="More info...",
                        uri=f'{urlPkgHomePage}{blocks[1]["href"]}'
                    )
                ]
            )
        except:
            act2 = CarouselColumn(
                thumbnail_image_url=imgs[3]["src"],
                title = tailor.trimed(titles[1].string, 40),
                text= '$ 請點擊More info...以查看更多',
                actions=[
                    URIAction(
                        label="More info...",
                        uri=f'{urlPkgHomePage}{blocks[1]["href"]}'
                    )
                ]
            )
            

        requestGet3 = requests.get(f'{urlPkgHomePage}{blocks[2]["href"]}')
        html3 = bs4.BeautifulSoup(requestGet3.text, "html.parser")
        try:
            content3 = html3.find("div", class_ = 'blogPost__post__body')
            act3 = CarouselColumn(
                thumbnail_image_url=imgs[4]["src"],
                title = tailor.trimed(titles[2].string, 40),
                # text= tailor.trimed(content3.text, 50),
                text= tailor.trimed(content3.text, 55),
                actions=[
                    URIAction(
                        label="More info...",
                        uri=f'{urlPkgHomePage}{blocks[2]["href"]}'
                    )
                ]
            )
        except:
            act3 = CarouselColumn(
                thumbnail_image_url=imgs[4]["src"],
                title = tailor.trimed(titles[2].string, 40),
                # text= tailor.trimed(content3.text, 50),
                text= '$ 請點擊More info...以查看更多',
                actions=[
                    URIAction(
                        label="More info...",
                        uri=f'{urlPkgHomePage}{blocks[2]["href"]}'
                    )
                ]
            )
        
        message = TemplateSendMessage(
            alt_text = "Activity Info",
            template=CarouselTemplate(
                columns=[
                    act1, act2, act3
                ]
            )
        )

        return message

    def button_location_resp():
        Me_at_the_zoo = VideoSendMessage(
            original_content_url= project_url + "/static/Me_at_the_zoo.mp4",
            preview_image_url= project_url + "/static/Me_at_the_zoo.png"
        )
        
        return Me_at_the_zoo
    
    def function_choose_base_location():
        message = TextSendMessage(
                    text=f'Check recent weather or else?',
                    quick_reply = QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(label='Weather', text='[Check weather]')),
                            QuickReplyButton(action=MessageAction(label='Else', text='[Check else]'))
                        ]
                    )
                )
        return message
    
    def button_friend_resp():
        return crawler.mergeInfo()

    def button_weather_resp():
        return '請發送位置資訊📍'

    def button_linktr_resp():
        return "https://linktr.ee/hoffffoh"

# ============================

    def test_msg():
        return "wake up it's hoff on the board"
    
    def test_msg_resp():
        return "做動ing"