import os
import shutil

#ディレクトリに入っている写真を全て削除
def allremove():
    os.makedirs('写真が入っているディレクトリ', exist_ok=True)

    target_dir = '写真が入っているディレクトリ名'

    shutil.rmtree(target_dir)

    os.mkdir(target_dir)

    print(os.listdir('写真が入っているディレクトリ/'))
