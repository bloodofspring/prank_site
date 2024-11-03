from flask import Flask, render_template
import telebot
from dotenv import load_dotenv
from os import environ

app = Flask(__name__)


@app.route("/<u_id>")
def home(u_id):
    try:
        load_dotenv()
        bot = (telebot.TeleBot(environ["bot_token"]))
        bot.send_message(int(u_id), "Кто-то перешел по пранк-ссылке!")
        bot_username = bot.get_me().username
    except:
        bot_username="<error>"

    return render_template("main.html", u_id=u_id, bot_username=bot_username)


if __name__ == "__main__":
    app.run()
