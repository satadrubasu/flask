from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "BASIC Skeleton Hello Word [ Two Environment Varibles :" \
           "\n export FLASK_APP=flashcards.py " \
           "\n export FLASK_ENV=development " \
           "\n flask run"