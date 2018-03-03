#!/usr/bin/env python#coding:utf-8# -*- coding: utf-8 -*
import os
from api import AipSpeech
#App ID: 10351927
#API Key: VWgKFTtRGdeviVbZ0AP80SfZ
#Secret Key: 1945bd34ec52542c48a4864b76bda2ca

#语音合成百度文档地址：http://yuyin.baidu.com/docs/tts/196
# 参数	类型	描述	是否必须
# tex	String	合成的文本，使用UTF-8编码，请注意文本长度必须小于1024字节	是
# lang	String	语言选择,填写zh	是
# ctp	String	客户端类型选择，web端填写1	是
# cuid	String	用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内	否
# spd	String	语速，取值0-9，默认为5中语速	否
# pit	String	音调，取值0-9，默认为5中语调	否
# vol	String	语速，取值0-15，默认为5中语速	否
# per	String	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
APP_ID = '10351927'
API_KEY = 'VWgKFTtRGdeviVbZ0AP80SfZ'
SECRET_KEY = '1945bd34ec52542c48a4864b76bda2ca'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def get_ip():
    #注意外围使用双引号而非单引号,并且假设默认是第一个网卡,特殊环境请适当修改代码
    ip = os.popen("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1").read()
    #print(ip)
    return ip;

if __name__ == "__main__":
    getip='大鱼叔叔，我的IP地址是：'+get_ip()
    result = aipSpeech.synthesis(getip, 'zh', 1, {
        'vol': 5,
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('hecheng.mp3', 'wb') as f:
            f.write(result)
