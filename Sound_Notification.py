#ラズパイの起動時に実行できるように設定する
import subprocess
import os
import time

while True:
    file=os.path.exists('/home/pi/Tensou.mp3')
    #ラズパイ側に音声ファイルが来るまで無限ループ
    if (file==True):
        subprocess.call("mpg321 /home/pi/Tensou.mp3",shell='true')
        os.remove('/home/pi/Tensou.mp3')
    time.sleep(1)
