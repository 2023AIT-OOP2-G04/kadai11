import cv2
import numpy as np

class PostProcessing:
    def __init__(self, imagePath:str=""):
        if imagePath == "":
            self.image = None
        else:
            self.image = cv2.imread(imagePath)
        self.funcList = []  # 画像処理の関数を格納するリスト

    # 画像処理の関数を追加する

    def run(self):
        for func in self.funcList:
            image = func()
            self.writeImage(image)
        return 

    # ここに画像処理の関数を書く
    
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