import requests
from flask import Flask, render_template, request, jsonify, flash
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
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


@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'GET':
        return render_template('signUp.html')

    else:
        userId = request.form['userId']
        userName = request.form['userName']
        password = request.form['pass1']
        password_check = request.form['pass2']
        email = request.form['email']
        exist_user = db.members.find_one({"userId": userId})
        if exist_user:
            return ({'msg': "이미 존재하는 아이디 입니다.", "result": "fail"})
        if password != password_check:
            return ({'msg': "패스워드를 확인해 주세요", "result": "fail"})

        doc = {
            "userId": userId,
            "userName": userName,
            "password": password,
            "email": email,
            "userImage": "https://mblogthumb-phinf.pstatic.net/MjAyMDExMDFfMyAg/MDAxNjA0MjI5NDA4NDMy.5zGHwAo_UtaQFX8Hd7zrDi1WiV5KrDsPHcRzu3e6b8Eg.IlkR3QN__c3o7Qe9z5_xYyCyr2vcx7L_W1arNFgwAJwg.JPEG.gambasg/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EA%B8%B0%EB%B3%B8%ED%94%84%EB%A1%9C%ED%95%84_%ED%8C%8C%EC%8A%A4%ED%85%94.jpg?type=w800"
        }
        db.members.insert_one(doc)

        return ({'msg': '회원가입 성공!', "result": "success"})


# port 는 자신이 사용할 port 지정
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
