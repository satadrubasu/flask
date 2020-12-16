from flask import Flask , render_template , abort , jsonify
from model import db


## Represents our Application Object
app = Flask(__name__)


@app.route("/")
def welcome_view():
    ## the message is a Jinja variable and would be {{message}} in the template file - welcome.html
    return render_template("welcome.html",message="Jinja variable value fassed from render template !!")


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",card=card,index = index)
    except IndexError:
        abort(404)


@app.route("/countviews")
def countviews():
    global counter
    counter +=1
    return "View Counter : " + str(counter)


###### API Section ######

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        ## automatic Json response
        return db[index]
    except IndexError:
        abort(404)


## Note returning a list object doesnt get auto serialized
## Use jsonify on the list object
@app.route("/api/card/")
def api_card_list():
    return jsonify(db)

