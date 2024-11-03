from flask import Flask, render_template
import telebot
from dotenv import load_dotenv
from os import environ

app = Flask(__name__)


@app.route("/<u_id>")
def home(u_id):
    try:
        load_dotenv()
        telebot.TeleBot(environ["bot_token"]).send_message(int(u_id), "Кто-то перешел по пранк-ссылке!")
    except:
        pass
    return render_template("main.html", u_id=u_id)


if __name__ == "__main__":
    app.run()
