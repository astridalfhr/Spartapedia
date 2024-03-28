from http import client
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb://Astridalifiah:Jaemin@ac-llkhiiw-shard-00-00.kcbmqee.mongodb.net:27017,ac-llkhiiw-shard-00-01.kcbmqee.mongodb.net:27017,ac-llkhiiw-shard-00-02.kcbmqee.mongodb.net:27017/?ssl=true&replicaSet=atlas-uh2qmt-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
db = client.dbspartaa

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST request!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET request!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)