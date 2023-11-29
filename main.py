# Import Flask library.
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create chatbot instance
tourism_bot = ChatBot(
    name="Touria",
    read_only=True,
    logic_adapters=["chatterbot.logic.BestMatch"]
)

# Training the bot on small talk
small_talk = [
    "Hello",
    "Hi There",
    "How are you?",
    "I'm well thank you. How can I help?"
]

list_trainer = ListTrainer(tourism_bot)
for item in small_talk:
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(tourism_bot)
corpus_trainer.train('chatterbot.corpus.english')

# List of cities supported to be replaced by SQL statement
cities_list = ['Lake District National Park', 'Corfe Castle', 'The Cotswolds', 'Cambridge', 'Bristol',
               'Oxford', 'Norwich', 'Stonehenge', 'Watergate Bay', 'Birmingham']



# Standard code block to run Flask.
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    bot_response = tourism_bot.get_response(usertext)
    return str(bot_response)

if __name__ == "__main__":
    app.run()