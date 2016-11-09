from pymongo import MongoClient
from flask import Flask, render_template, jsonify

#MongoBD
client = MongoClient()
db = client.ussa

#Flask
app = Flask(__name__)

#Request to mongo and sort
def sort():
    global base
    base=[]
    proof = []
    i=0

    cities = list(db.us_cont.find().sort('pop', -1)) #limit can >50
    while len(proof) < 21:
        # dont repeat
        if cities[i]["city"] not in proof:
            proof.append(cities[i]["city"])
            base.append({"label": cities[i]["city"], "value": str(cities[i]["pop"])})
        i += 1

#request main
@app.route('/')
def index_view():
    return render_template('index.html')

#request json
@app.route('/get-cities')
def json():
    sort()
    return jsonify(list(base))


if __name__ == '__main__':
  app.run()
