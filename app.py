import requests
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 준영님 코드
import certifi

# DB 커넥션
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.zhropba.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.sparton
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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
    app.run('0.0.0.0', port=5001, debug=True)
