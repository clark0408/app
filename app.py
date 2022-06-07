from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('VIeEbyQM8SLX3OSwK12JU7miv0bQ0MtlTiJW3QbmoXL6kqS3Cc6eHHtLFvfP7Zk0WEGJBqzFnyLo59ZalEmpbAkTiGDxEhMPQJ+Vu3CzLVILliI3QbF4jux3QfGpZ1MRIuSCLkVWreOEYG2CdG3HpgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('29669c503a4fb5ae249afaa62fd5bb36')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='吵喔'))


if __name__ == "__main__":
    app.run()