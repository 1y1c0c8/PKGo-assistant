- LineBot Api
    - 每個event.message.text觸發之後，只能做一次reply
        > linebot_api.reply_message(event.reply_token, TextSendMessage(text=''))
- Crawler
    - 縮網址
        > 原地放棄