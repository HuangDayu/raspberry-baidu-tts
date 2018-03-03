#!/usr/bin/env python#coding:utf-8# -*- coding: utf-8 -*
import os
from api import AipSpeech
#App ID: 10351927
#API Key: VWgKFTtRGdeviVbZ0AP80SfZ
#Secret Key: 1945bd34ec52542c48a4864b76bda2ca
#语音识别百度文档地址：http://yuyin.baidu.com/docs/asr/190
# arecord -Dhw:1,0 -c 2 -r 16000 -f S16_LE test.wav
APP_ID = '10351927'
API_KEY = 'VWgKFTtRGdeviVbZ0AP80SfZ'
SECRET_KEY = '1945bd34ec52542c48a4864b76bda2ca'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 从URL获取文件识别
# aipSpeech.asr('', 'pcm', 16000, {
#     'url': 'http://121.40.195.233/res/16k_test.pcm',
#     'callback': 'http://xxx.com/receive',
# })

if __name__ == "__main__":
    # 识别本地文件
    str = aipSpeech.asr(get_file_content('./shibie.wav'), 'wav',16000,{
        'lan': 'zh',
    })	print(str)
    print(str['result'].encode('utf-8'))
