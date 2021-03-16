from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request



app = Flask(__name__)


#Creation of chatbot with Chatterbot library
my_bot = ChatBot(name='Mysterybot', read_only=True)


#Trained with given french corpus
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(my_bot.get_response(userText))

@app.route("/setenglish")
def set_english_response():
    my_bot = ChatBot(name='Mysterybot', read_only=True)
    corpus_trainer = ChatterBotCorpusTrainer(my_bot)
    corpus_trainer.train('chatterbot.corpus.english')
    return 'Hi I am Mark Jackson!'

@app.route("/setfrench")
def set_french_response():
    my_bot = ChatBot(name='Mysterybot', read_only=True)
    corpus_trainer = ChatterBotCorpusTrainer(my_bot)
    corpus_trainer.train('chatterbot.corpus.french')
    return 'Hi I am Jean Claude!'

@app.route("/setspanish")
def set_spanish_response():
    my_bot = ChatBot(name='Mysterybot', read_only=True)
    corpus_trainer = ChatterBotCorpusTrainer(my_bot)
    corpus_trainer.train('chatterbot.corpus.spanish')
    return 'Hi I am Estabon Zaragoza!'


if __name__ == "__main__":
    app.run()

'''
while(True):
    prompt = str(input())
    if prompt == "stop":
        break
    print(my_bot.get_response(prompt))
'''