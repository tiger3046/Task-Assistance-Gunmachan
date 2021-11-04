#!/bin/sh
sleep 20
fn=$(date +%Y%m%d%H%M%S)
raspistill -o "shasinフォルダまでのディレクトリ"/shasin/${fn}.jpg -w 100 -h 100
scp "shasinフォルダまでのディレクトリ"/shasin/${fn}.jpg "ユーザ名"@"グローバルIPアドレス":"gpapicturesフォルダまでのディレクトリ"/gpapictures
rm "shasinフォルダまでのディレクトリ"/shasin/${fn}.jpg
