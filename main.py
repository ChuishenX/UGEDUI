from you_get import common
from ui.ui_form import Ui_MainWindow
import sys, os
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6 import QtCore
from requests import get
from multiprocessing import Process as P
import multiprocessing as m
from pydub import AudioSegment

headers = {'User-Agent': "Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
message = "欢迎使用 UGEDUI，这是一个基于 You-Get 的视频下载器。"

try:
    os.mkdir("downloads")
except:
    pass

os.chdir(os.path.join(os.path.abspath('.'),"downloads"))

# # 如果没有安装ffmpeg，这里会给你一个包让你安装。
# try:
#     os.system("ffmpeg")
# except:
#     pass

def customdownload(url, dir, merge, q): # 适配多进程
    try:
        print("Downloading...")
        common.any_download(url,output_dir=dir,merge=merge)
        print("Downloaded.")
        q.put(0)
    except Exception as e:
        print(e)
        q.put(-1)

class TheMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.downloader.clicked.connect(self.downloadInside)
        self.ui.converter.clicked.connect(self.convert)

    def downloadInside(self):
        urls = []
        url = self.ui.theInput.toPlainText()
        if len(url.split("\n"))>=2:
            urls = url.split("\n")
        def download(url):
            try:
                print("0")
                q = m.Queue()
                print("1")
                p = P(target=customdownload,args=(url,".","True",q))
                print(2)
                p.start(); p.join(); a = q.get()
                print(3)
                return
            except Exception as e:
                print(e)
        if urls:
            for url in urls:
                QMessageBox.information(self,url+" 已在后台下载",url+" 已在后台下载",QMessageBox.Ok)
                download(url)
        else:
            QMessageBox.information(self,url+" 已在后台下载",url+" 已在后台下载",QMessageBox.Ok)
            download(url)
    
    def convert(self):
        def to_audio(filepath, output_type="mp3"):
            song = AudioSegment.from_file(filepath)
            filename = filepath.split(".")[-2]
            song.export(f"{filename}.{output_type}", format=f"{output_type}")
        files = os.listdir()
        for file in files:
            if file.endswith(".mp4"):
                to_audio(file,"mp3")
                os.remove(file)
    
if __name__ == "__main__":
    m.freeze_support()
    app = QApplication(sys.argv)
    window = TheMainWindow()
    window.show()
    sys.exit(app.exec())

