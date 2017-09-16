from flask import Flask, render_template, redirect, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random

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
        
        im = random.randint(1, 5)
        im2 = random.randint(1, 5)
        if im == im2:
            im2 = im%5+1
        answeeer="Do you want to buy  this? <img src=\"\\static\\images\\TV"+str(im)+".jpg\" alt=\"Mountain View\" style=\"width:304px;height:228px;\"> <p> or this</p> <img src=\"\\static\\images\\TV"+str(im2)+".jpg\" alt=\"Mountain View\" style=\"width:304px;height:228px;\">"
        
    if "getmoney" in query:

        answeeer="<img src=\"\\static\\images\\giphy.gif\" alt=\"Mountain View\" style=\"width:304px;height:228px;\"> "

    if "stop" in query:
        return render_template("page2.html",answer=answeeer)

    return render_template("index.html",answer=answeeer)

@app.route("/get/")
def get_raw_response_empty():
    return render_template("index.html",answer="You type nothing IDIOT!")




if __name__ == "__main__":
    app.run()
