import requests
from flask import Flask, render_template, request, jsonify, flash
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
# 준영님 코드
import certifi

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

#login
@app.route('/login')
def login():

    return render_template('login.html')

#signup
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
        
#board
@app.route('/board')
def board():
    return render_template('board.html')


@app.route("/board_save", methods=["POST"])
def board_post():
    writer_receive = request.form["writer_give"]
    comment_receive = request.form["comment_give"]
    date_receive = request.form["date_give"]

    if writer_receive != '':
        count = 1
        for i in range(10):
            doc = {
                'num': count,
                'writerId': writer_receive,
                'comment': comment_receive,
                'date': date_receive
            }
            db.board.insert_one(doc)
            count += 1
    return jsonify({'msg': '댓글 작성 완료!'})


@app.route("/boards", methods=["GET"])
def board_get():
    board_list = list(db.board.find({},{'_id':False}))
    return jsonify({'board_list':board_list})

# port 는 자신이 사용할 port 지정
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
