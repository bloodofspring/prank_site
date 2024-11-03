from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<u_id>")
def home(u_id):
    return render_template("main.html", u_id=u_id)


@app.route("/popalsa/<u_id>")
def prank(u_id):
    return render_template("prank.html", bot_username="testing_158258358_bot")


if __name__ == "__main__":
    app.run()
