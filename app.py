import requests
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 준영님 코드
import certifi

# DB 커넥션
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.zhropba.mongodb.net/?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.sparton
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/profile')
def profileHome():
    return render_template('profile.html')
@app.route("/profile/save", methods=["POST"])
def profileMod():
    id_receive = request.form['id_give']
    image_receive = request.form['image_give']
    nick_receive = request.form['nick_give']
    about_receive = request.form['about_give']
    job_receive = request.form['job_give']
    techStack_receive = request.form['techStack_give']
    email_receive = request.form['email_give']
    gitUrl_receive = request.form['gitUrl_give']

    doc = {
        'userId': id_receive,
        'userImg': image_receive,
        'userName': nick_receive,
        'info': about_receive,
        'job': job_receive,
        'stack': techStack_receive,
        'email': email_receive,
        'github': gitUrl_receive,
    }

    db.card.insert_one(doc)

    return jsonify({'msg': '내용 저장 완료'})

# port 는 자신이 사용할 port 지정
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
