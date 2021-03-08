# web app
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

# 權杖
# access 存取 秘密
line_bot_api = LineBotApi('oEp6naQ2t+jeE/tJLYTp2K/c11MPgvzA9YlHSa+o5gsYQ5eTG/DvHukLc8k9DeTHmrVco59NOAHYdKmmqI8wgnGVogGd3pYJYEekfmC780gFuwD4LZH+lIfejs8/q3EQkfUCix+v0c6WU6WV0sJ1bwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('44d9d8e7bcc2d8808e6685dde80e7fc6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    x = '很抱歉,你說甚麼'

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002768'
        )

        line_bot_api.reply_message(
                event.reply_token,
                sticker_message)
        return

    if msg in ['yoyo', 'hi']:
        x = '你好'
    elif msg == '你吃飽了嗎':
        x = '還沒'
    elif msg == '你是誰':
        x = '我是機器人'
    elif '訂位' in msg:
        x = '你想訂位,是嗎?'

    


if __name__ == "__main__":
    app.run()