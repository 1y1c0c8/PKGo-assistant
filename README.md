# PKGo-assistant
![image](https://github.com/1y1c0c8/PKGo-assistant/blob/main/src/parrot.gif)
![image](https://github.com/1y1c0c8/PKGo-assistant/blob/main/src/RR_QRcode.png)


### Link to add friend
https://line.me/R/ti/p/%40919wftug

### Introduction
- 起因
    - 因為在玩Pokemon Go時希望某些功能能夠集成，所以藉此機會開發PKGo Assistant
- FSM
    - [](https://github.com/1y1c0c8/PKGo-assistant/blob/main/src/321238339_551179120382787_3088986884276905712_n.jpg)
- 基本功能
    - 計算寶可夢IV(appraise)
        - 純粹一推倒公式計算appraise
    - 抓取最近活動資訊
        - 利用bs4爬蟲，從官網獲得最新活動資訊
    - 地點資訊
        > 最後來不及做完，所以變成類彩蛋qq
        - 利用VideoSendMessage，這真的不是Rick Roll
    - 新增訓練家好友
        - 從trainer club交流網站抓取玩家暱稱以及ID
    - 近日天氣
        - 利用中央氣象局提供之api獲取資訊
    - 創作者資訊
        -Linktr，助教有興趣可以follow我的攝影帳號



## Reference
- **LineBot + Falsk**
    - [Python and LINE Bot 系列 by. peiiiii](https://ithelp.ithome.com.tw/m/users/20151448/ironman/5396)
    - [【ngrok 教學】 webhook 直接在本地端測起來，Debug沒煩惱！](https://learn.markteaching.com/ngrok-webhook/)
    - [[30 天教你如何玩弄 Line bot API] 第 8 天：各種被嘴的方法 by. Clarence (mr_clarence)](https://ithelp.ithome.com.tw/articles/10219503)
    - [用 Python 暢玩 Line bot - 22：使用者資訊](https://ithelp.ithome.com.tw/articles/10282156)
        > User ID應該是認~~裝置~~帳號的，因為機器人關掉重開，得到的User ID還是同一個
- **Crawler**
    - [爬蟲怎麼爬 從零開始的爬蟲自學 系列 by. 早安您好 (SeanWei)](https://ithelp.ithome.com.tw/users/20140149/ironman/4278)
- **Access OpenStreetMap(OSM)**
    - [台灣寶可夢資訊站: Pokemon GO遊戲資訊網站](https://twpkinfo.com/ipoke.aspx)
    - [【OSM】是什麼？OpenStreetMap，一個不竊取個資的免費地圖！iOS／Android](https://kikinote.net/161141)
    - [How to integrate Geoapify into your Python data science toolbox](https://www.geoapify.com/integrate-geoapify-python-data-science-toolbox)
    - [從 OSM 撈有趣的座標資料： 網站與工具](https://newtoypia.blogspot.com/2015/05/overpass-api.html)

- **About location application**
    - [How do I link to Google Maps with a particular longitude and latitude?](https://stackoverflow.com/questions/1801732/how-do-i-link-to-google-maps-with-a-particular-longitude-and-latitude)
- **Basic Python**
    - [Python如何控制小數點後面的小數位數](https://www.796t.com/content/1549397542.html)
        > Trim latitude & longitude
- **OpenAI**
    - [LINE BOT 串接 OpenAI ( 讓 AI 回覆訊息 )](https://steam.oxxostudio.tw/category/python/example/line-bot-openai-1.html#a2)
        > 我還沒研究完這篇
- **Selenium webdriver**
    - [【Day 27】網路爬蟲 - Selenium篇](https://ithelp.ithome.com.tw/articles/10307735)
- **.env**
    - [【 Python 】利用 .env 與環境變數隱藏敏感資訊](https://learningsky.io/python-use-environmental-variables-to-hide-sensitive-information/)
- **正規表達式**
    - []()
    - []()
        > By openai
- **分割字串**
    - [在 Python 中的空格上拆分字符串](https://www.techiedelight.com/zh-tw/split-string-whitespace-python/)
- **圖文選單**
    - [圖文選單 官方帳號操作手冊](https://tw.linebiz.com/manual/line-official-account/oa-manager-richmenu/)
- **Template**
    - [Line Messaging API 的各種訊息格式](https://ithelp.ithome.com.tw/articles/10198142?sc=rss.qu)
    - [[Python+LINE Bot教學]提升使用者體驗的按鈕樣板訊息(Buttons template message)實用技巧](https://www.learncodewithmike.com/2020/07/line-bot-buttons-template-message.html)
- **Deploy**
    - Render
    - Docker
        - Dockerfile
            - [How to run and host Flask in a Docker container](https://youtu.be/9tErxxGpOM4)

