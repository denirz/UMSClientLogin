'''
Created on Dec 20, 2012

@author: denirz
'''
from UMSClientLogin import UMSHOST
def GetMessageList(Jsession,_umscsrf):
    print "GetMessageListOutput1:"
# get chat list:
#    https://messages.megafon.ru/onebox/getChatList.do?startNum=1&endNum=100&reFreshFlag=1&operation=1&chatMsgType=10100000000100000000000000000000&t=0.2095859289213695
'''
chatMsgType=10100000000100000000000000000000
endNum=100
operation=1
reFreshFlag=1
startNum=1
t=0.7770682506014785
'''
''' Header
GET /onebox/getChatList.do?startNum=1&endNum=100&reFreshFlag=1&operation=1&chatMsgType=10100000000100000000000000000000&t=0.7770682506014785 HTTP/1.1
Host: messages.megafon.ru
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0
Accept: application/xml, text/xml, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
_umscsrf: 135597772024196670
Referer: https://messages.megafon.ru/onebox/mix.do
Cookie: __utma=88342791.234245059.1347864230.1355896865.1355899542.6; __utmz=88342791.1347864230.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); bookmarks=eNpLtDKwqq4FAAZPAf4%3D; __utma=241511582.1838151384.1350099050.1350914052.1351022928.5; __utmz=241511582.1350099050.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); JSESSIONID=B6A8000600434AA23D945B2C2D4386DF; __utmc=88342791; _umscsrf=1355924196670
'''    
#getchat itself     
'''    
https://messages.megafon.ru/onebox/oneboxList.do?umReq.ctlg=1%2C2&umReq.numFlg=1&umReq.mType=2053&umReq.srt=0&umReq.lType=0&umReq.dFlg=0&umReq.srtDr=0&umReq.rdFlg=0&umReq.bNum=1&umReq.eNum=50&umReq.snd=%2B79262001208&umReq.rcv=%2B79262001222&umReq.bTime=&umReq.eTime=&umReq.impt=-1&umReq.t=&umReq.threadFlag=1&rownid=0.576959018029553    
---
rownid=0.576959018029553
umReq.bNum=1
umReq.bTime=
umReq.ctlg=1,2
umReq.dFlg=0
umReq.eNum=50
umReq.eTime=
umReq.impt=-1
umReq.lType=0
umReq.mType=2053
umReq.numFlg=1
umReq.rcv=+79262001222
umReq.rdFlg=0
umReq.snd=+79262001208
umReq.srt=0
umReq.srtDr=0
umReq.t=
umReq.threadFlag=1 
---
GET /onebox/oneboxList.do?umReq.ctlg=1%2C2&umReq.numFlg=1&umReq.mType=2053&umReq.srt=0&umReq.lType=0&umReq.dFlg=0&umReq.srtDr=0&umReq.rdFlg=0&umReq.bNum=1&umReq.eNum=50&umReq.snd=%2B79262001208&umReq.rcv=%2B79262001222&umReq.bTime=&umReq.eTime=&umReq.impt=-1&umReq.t=&umReq.threadFlag=1&rownid=0.576959018029553 HTTP/1.1
Host: messages.megafon.ru
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
_umscsrf: 135595391081854513
Referer: https://messages.megafon.ru/onebox/mix.do
Cookie: __utma=88342791.234245059.1347864230.1355899542.1355974282.7; __utmz=88342791.1347864230.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); bookmarks=eNpLtDKwqq4FAAZPAf4%3D; __utma=241511582.1838151384.1350099050.1350914052.1351022928.5; __utmz=241511582.1350099050.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); JSESSIONID=DDE7AA5DE4F42F99C0785DF1C806DEE1; __utmc=88342791; _umscsrf=1355981854513; __utmb=88342791.2.10.1355974282

'''





    pass
if __name__ == '__main__':
    print "GetMessagesList Module output:"
    GetMessageList('ldd','123523542342')
    pass