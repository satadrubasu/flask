
from flask import Flask, render_template, abort, jsonify, Response
from model import db

import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Counter

#from prometheus_flask_exporter import PrometheusMetrics



graphs = {}
graphs['smfReq'] = Counter('myapp_smfReq_req_total','Total number of processed requests')
graphs['amfReq'] = Counter('myapp_amfReq_req_total','Total number of processed requests')
graphs['nrfReq'] = Counter('myapp_nrfReq_req_total','Total number of processed requests')

## Represents our Application Object
app = Flask(__name__)
## How PrometheuMetrics is wrapping on app
#metrics = PrometheusMetrics(app)

# static information as metric
#metrics.info('app_info', 'Application info', version='0.1.0')


@app.route("/")
def welcome_view():
    graphs['smfReq'].inc()
    graphs['amfReq'].inc(3)
    graphs['nrfReq'].inc(15)
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

########## METRICS Variants ###########

@app.route("/skip")
#@metrics.do_not_track()
def skip_view():
    pass # default metrics are not collected

#### prometheus client metrics ####

@app.route('/metrics')
def app_metrics():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res,mimetype="text/plain")