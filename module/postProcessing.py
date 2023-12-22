import cv2
import numpy as np
import os

class PostProcessing:
    def __init__(self, imagePath:str=""):
        if imagePath == "":
            self.image = None
        else:
            self.image = cv2.imread(imagePath)
        self.funcList = [self.__sampleFunc(), self.facewaku(), ]  # 画像処理の関数を格納するリスト

    # サンプル関数
    def __sampleFunc(self):
        print("sampleFunc、ファンクリストから呼び出されました。")

    def run(self):
        for func in self.funcList:
            image = func()
            self.writeImage(image)
        return 

    # ここに画像処理の関数を書く
    # 顔検出して枠で囲う関数
    def facewaku(self):
        if self.image is None:
            return

        # 顔検出用の分類器を読み込む
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # グレースケールに変換
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # 顔を検出
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # 検出した顔に枠を描画
        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # processed フォルダに保存
        outputFolder = "./static/img/processed/"
        os.makedirs(outputFolder, exist_ok=True)

        outputPath = os.path.join(outputFolder, "facewaku_output.jpg")
        cv2.imwrite(outputPath, self.image)

        return self.image
    
    def readImage(self, imagePath:str=""):
        if imagePath == "":
            return
        self.image = cv2.imread(imagePath)
        return

    # 主にデバッグ用
    def showImage(self, image=None):
        if image is None:
            return
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def writeImage(self, image=None, outputName=""):
        if image is None:
            return
        outputPath = "./static/img/processed/" + outputName + ".jpg"
        cv2.imwrite(outputPath, image)

if __name__ == "__main__":
    # ここでデバッグする
    # 以下のようにデバッグする
    imagePath = "./static/img/test/test.jpg"
    postProcessing = PostProcessing(imagePath)
    postProcessing.showImage(postProcessing.image)
    postProcessing.writeImage(postProcessing.image, "test")