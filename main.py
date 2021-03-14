from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request



app = Flask(__name__)


#Creation of chatbot with Chatterbot library
my_bot = ChatBot(name='Mysterybot', read_only=True)


#Trained with given french corpus
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.french')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(my_bot.get_response(userText))


if __name__ == "__main__":
    app.run()

'''
while(True):
    prompt = str(input())
    if prompt == "stop":
        break
    print(my_bot.get_response(prompt))
'''