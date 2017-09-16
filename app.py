from flask import Flask, render_template, redirect, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")
textDum = ""

@app.route("/")
def home():
    return render_template("index.html",answer=textDum)


@app.route("/get/<string:query>/")
def get_raw_response(query):
    answeeer=str(english_bot.get_response(query))
    if "TV" in query:
    	answeeer="Do you want to buy an Xbox"

    if "buy" in query:
        answeeer="💸💳"


    return render_template("index.html",answer=answeeer)




if __name__ == "__main__":
    app.run()
