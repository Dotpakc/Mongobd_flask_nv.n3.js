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

    cities = list(db.us_cont.find().sort('pop', -1).limit(50)) #limit can >50
    for cut in cities:
        # dont repeat
        if cut["city"] not in proof:
            #only 20 cities
            if len(proof)<21:
                proof.append(cut["city"])
                base.append({"label":cut["city"],"value":str(cut["pop"])})
            else:break

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
