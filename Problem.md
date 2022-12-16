- **LineBot Api**
    - 每個event.message.text觸發之後，只能做一次reply
        > linebot_api.reply_message(event.reply_token, TextSendMessage(text=''))
    - 先確認```event.type```，再確認```event.message.type```
        > from linebot

- **Crawler**
    - 縮網址
        > 原地放棄

- **Automatically**
    - Send line message automatically and frequently
        > 原地放棄，改成「抓取單次資料」為目標

- **twpkinfo**
    - 找不到可以爬出來的位置資料 + 原來app早就可以通知高IV目標(但也沒說清楚附近是多遠 高IV是多高)
        > 媽的不如去睡覺
        > 阿不然就寄信去問 QQ，寄了媒人回 三個字超級可悲
        > 有現成api但沒看到可以給current location的，目前希望能用Selenium 的webdriver實現目標效果

- **Ngrok**
    - 下指令得到的URL結尾變成-free.app而非.io
        > 目前沒查到原因，但睡一覺早上就正常了==

- **openai api額度已達上限**
    - [ ] 創新帳號
    - [ ] 用selenium chrome webdriver把用戶訊息丟到chat GPT，再把chat GPT的回覆抓回來