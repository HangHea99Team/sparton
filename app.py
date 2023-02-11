import requests
from flask import Flask, render_template, request, jsonify, flash, session
from bson.json_util import dumps
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
app.secret_key = "secret"

@app.route('/')
def home():
    return render_template('index.html')
@app.route("/card", methods=["GET"])
def card_get():
    card_list = list(db.card.find({},{'_id':False}))
    return jsonify({'card':card_list})
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
    like_receive = request.form['like_give']

    doc = {
        'userId': id_receive,
        'userImg': image_receive,
        'userName': nick_receive,
        'info': about_receive,
        'job': job_receive,
        'stack': techStack_receive,
        'email': email_receive,
        'github': gitUrl_receive,
        'like': int(like_receive),
    }

    db.card.insert_one(doc)

    return jsonify({'msg': '내용 저장 완료'})

@app.route("/card/detail", methods=["GET"])
def getUserInfo():
    userId = request.args.get('search_id')
    userInfo = db.card.find_one({'userId':userId})
    return jsonify({'userInfo':dumps(userInfo), 'msg': '사용자 정보 불러오기 완료'})
@app.route("/card/likeUser", methods=["GET"])
def thisUserLike():
    userId = request.args.get('search_id')
    userInfo = db.card.find_one({'userId':userId})
    db.card.update_one({'userId': userId}, {'$set': {'like': userInfo['like']+1}})
    userInfo = db.card.find_one({'userId':userId})
    return jsonify({'userInfo':dumps(userInfo), 'msg': '사용자 정보 불러오기 완료'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userId = request.form['userId']
        password = request.form['password']
        exist_user = db.members.find_one({"userId":userId,"password":password})
        print(exist_user)
        if exist_user is None:
            return ({'msg': '아이디/비밀번호를 다시 확인해 주세요!', "result": "fail"})

        if exist_user:
            session['userId'] = userId
            session['userName'] = exist_user['userName']
            session_info = '%s' %session
            print(session_info)
            return ({'msg': '로그인 성공!', "result": "success"})

# logout

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    session_info = '%s' %session
    print(session_info)
    return ({'msg': '로그아웃 성공!', "result": "success"})

# signup


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
        writeCard = False;
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
            "userImage": "https://mblogthumb-phinf.pstatic.net/MjAyMDExMDFfMyAg/MDAxNjA0MjI5NDA4NDMy.5zGHwAo_UtaQFX8Hd7zrDi1WiV5KrDsPHcRzu3e6b8Eg.IlkR3QN__c3o7Qe9z5_xYyCyr2vcx7L_W1arNFgwAJwg.JPEG.gambasg/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EA%B8%B0%EB%B3%B8%ED%94%84%EB%A1%9C%ED%95%84_%ED%8C%8C%EC%8A%A4%ED%85%94.jpg?type=w800",
            "writeCard": writeCard
        }
        db.members.insert_one(doc)

        return ({'msg': '회원가입 성공!', "result": "success"})

@app.route('/board')
def board():
    return render_template('board.html')


@app.route("/board_save", methods=["POST"])
def board_post():
    # num_receive = request.form["num_give"]
    writer_receive = request.form["writer_give"]
    comment_receive = request.form["comment_give"]
    date_receive = request.form["date_give"]

    if writer_receive != '':
        doc = {
            # 'num': num_receive,
            'writerId': writer_receive,
            'comment': comment_receive,
            'date': date_receive
        }
        db.board.insert_one(doc)
    return jsonify({'msg': '댓글 작성 완료!'})


@app.route("/boards", methods=["GET"])
def board_get():
    board_list = list(db.board.find({}, {'_id': False}))
    return jsonify({'board_list': board_list})


# my page
@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

@app.route('/show', methods=["GET"])
def show_get():
    info = db.card.find_one({'userId':'hyuk'})
    return jsonify({'userInfo': info})

# port 는 자신이 사용할 port 지정
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
