import keras
import sys, os
import numpy as np
from keras.models import load_model
from PIL import Image
import requests
import glob
import re
import shutil
import oo

#学習済みデータに基づいた画像判定
class studying:
    def __init__(self,testpic,keras_param):
        self.testpic = testpic
        self.keras_param = keras_param
        self.imsize = (64, 64)

    def load_image(self,path):
        img = Image.open(path)
        img = img.convert('RGB')
        img = img.resize(self.imsize)
        img = np.asarray(img)
        img = img / 255.0
        return img

    def ai_judge(self):
        model = load_model(self.keras_param)
        img = self.load_image(self.testpic)
        prd = model.predict(np.array([img]))
        print(prd) # 精度の表示
        prelabel = np.argmax(prd, axis=1)

        if prelabel == 0:
            return 0
        elif prelabel == 1:
            return 1

"""
LINEに通知する
"""
def main():
    send_line_notify(msg)
    send_line_notify(msg1)


def send_line_notify(notification_message):
    line_notify_token = 'LINE_notify_token'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)


m = 0 #15回判定のためのカウンタ変数
l = 0 #ファイルを一枚一枚読み込むための変数
file = './cnn.h5'
src_file = glob.glob('画像フォルダまでのパス/*.jpg')
datacount = len(src_file)
count = 0
un_count = 0
s = 2
x = []
y = []

#15回判定し、その後画像を削除
while s > 0:
    if len(src_file) == 15:
        for i in src_file:
            a = studying(i,file)
            if a.ai_judge() == 0:
                count += 1
                m += 1
            elif a.ai_judge() == 1:
                un_count += 1
                m += 1
        if m == 15:
            oo.allremove()
            break
    else:
        src_file = glob.glob('画像フォルダまでのパス/*.jpg')
        continue


#判定結果に合わせて内容をかえる
percent=count/15
if count > un_count:
    msg = 'おつかれ'

else:
    msg = 'みんな勉強してるよ'
    msg1 = '君だけやってないの大丈夫？'
    shutil.copy('onsei2.mp3までのパス/onsei2.mp3', 'onsei2.mp3までのパス/Tensou.mp3.tmp') #ラズパイ転送するために名前の変更する



#lineの出力
if __name__ == "__main__":
    main()

voice.avoice()
