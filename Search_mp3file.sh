#!/bin/sh


while true
do
	scp "ユーザ名"@"グローバルIPアドレス":"Tensou.mp3までのディレクトリ名"/Tensou.mp3.tmp /home/pi
	ssh "ユーザ名"@"グローバルIPアドレス" rm Tensou.mp3.tmpまでのディレクトリ名/Tensou.mp3.tmp
        mv /home/pi/Tensou.mp3.tmp /home/pi/Tensou.mp3	
	sleep 1
done

