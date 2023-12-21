from flask import Flask, request, render_template, jsonify
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# moduleのimport
from module.postProcessing import PostProcessing
# Path: module/directoryMonitoring.py

# ディレクトリ監視関数の追加
# ここに書く


# Flaskの処理
app = Flask(__name__)

# http://127.0.0.1:5000/upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # webページからのファイルをuploadフォルダに保存
    pass

# http://127.0.0.1:5000/show
@app.route('/show', methods=['GET'])
def show():
    # uploadフォルダとprocessedフォルダの画像を表示
    return render_template("show.html")

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)