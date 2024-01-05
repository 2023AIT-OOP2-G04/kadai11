# img->uploadに画像ファイルが追加される。
# 画像のパスを取得する
# 画像処理を走らせる

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from postProcessing import PostProcessing

class ImageProcessingHandler(FileSystemEventHandler):
    def __init__(self, post_processor):
        super().__init__()
        self.post_processor = post_processor

    def on_created(self, event):
        if event.is_directory:
            return

        # 新しいファイルが作成された場合に画像処理を行う
        image_path = event.src_path
        self.post_processor.readImage(image_path)
        self.post_processor.run()

def watch_directory(directory_path, post_processor):
    event_handler = ImageProcessingHandler(post_processor)
    observer = Observer()
    observer.schedule(event_handler, directory_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    # ディレクトリ監視関数の追加
    directory_to_watch = "./kadai11/static/img/uplode"  # 監視対象ディレクトリのパスを指定
    post_processor = PostProcessing()
    watch_directory(directory_to_watch, post_processor)
