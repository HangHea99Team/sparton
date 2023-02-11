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

# port 는 자신이 사용할 port 지정
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
