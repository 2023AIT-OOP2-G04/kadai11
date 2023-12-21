import os
import time
from flask import Flask, request

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import cv2
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = "static/img/upload"
PROCESSED_FOLDER = "static/img/processed"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER


class ImageHandler(FileSystemEventHandler):
    def __init__(self):
        pass

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"新しいファイルが作成されました: {event.src_path}")
        process_image(event.src_path)


def process_image(input_path):
    # 画像の読み込み
    original_image = cv2.imread(input_path)

    # グレースケール変換
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # ノイズ除去
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Cannyエッジ検出
    edges = cv2.Canny(blurred_image, 50, 150)

    # 出力画像のファイルパス
    output_path = os.path.join(
        app.config["PROCESSED_FOLDER"], os.path.basename(input_path)
    )

    # 出力画像の保存
    cv2.imwrite(output_path, edges)

    print(f"Cannyエッジ検出が完了しました。 出力先: {output_path}")


@app.route("/", methods=["POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filename)
            return "Upload successful!"


if __name__ == "__main__":
    # ディレクトリの監視用のイベントハンドラを作成
    event_handler = ImageHandler()

    # Observerを作成し、イベントハンドラを登録
    observer = Observer()
    observer.schedule(event_handler, path=app.config["UPLOAD_FOLDER"], recursive=False)

    # Observerを開始
    observer.start()

    # Flaskアプリを起動
    app.run(debug=True, port=5000)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    # Observerの終了処理
    observer.join()
