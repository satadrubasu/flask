from flask import Flask , render_template
from model import db


## Represents our Application Object
app = Flask(__name__)


@app.route("/")
def welcome():
    ## the message is a Jinja variable and would be {{message}} in the template file - welcome.html
    return render_template("welcome.html",message="Jinja variable value fassed from render template !!")


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html",card=card)

counter = 0
@app.route("/countviews")
def countviews():
    global counter
    counter +=1
    return "View Counter : " + str(counter)