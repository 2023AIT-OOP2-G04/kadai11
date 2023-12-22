from flask import Flask, request, render_template, jsonify
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import glob

# moduleのimport
from module.postProcessing import PostProcessing

# Path: module/directoryMonitoring.py

# ディレクトリ監視関数の追加
# ここに書く


# Flaskの処理
app = Flask(__name__)


# http://127.0.0.1:5000/upload
@app.route("/upload", methods=["POST"])
def upload_file():
    # webページからのファイルをuploadフォルダに保存

    uploadPath = "./static/img/upload"

    uploadFile = request.files.get("uploadFile", None)

    # ファイル名を取得
    # filename = secure_filename(uploadFile.filename)

    print("aaaa")

    # print(uploadFile.filename)
    # print(filename)

    try:
        # ファイルを保存する
        uploadFile.save(os.path.join(uploadPath, uploadFile.filename))
    except:
        return jsonify({"result": "error"})

    return jsonify({"result": "success"})

    pass


# http://127.0.0.1:5000/show
@app.route("/show", methods=["GET"])
def show():
    # uploadフォルダとprocessedフォルダの画像を表示
    uploadPath = "static/upload"
    uploadFiles = [
        f for f in os.listdir(uploadPath) if os.path.isfile(os.path.join(uploadPath, f))
    ] 
    print(uploadFiles)

    processedPath = "static/processed"
    processedFiles = [
        f for f in os.listdir(processedPath) if os.path.isfile(os.path.join(processedPath, f))
    ] 
    print(processedFiles)


    return render_template("show.html",
                           uploadFiles,
                           processedFiles)


# http://127.0.0.1:5000/
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
