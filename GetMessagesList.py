#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-
'''
Created on Dec 20, 2012

@author: denirz
'''
import httplib,urllib
from UMSClientLogin import UMSHOST,InsertRandInString,GetAuthParams
def xmlGetChatList(Jsession,_umscsrf):
#    https://messages.megafon.ru/onebox/getChatList.do?startNum=1&endNum=100&reFreshFlag=1&operation=1&chatMsgType=10100000000100000000000000000000&t=0.2095859289213695
#    print "GetChatListOutput1:"
#    print __name__
    UrltoGet='/onebox/getChatList.do?'
    params={
            'chatMsgType':'10100000000100000000000000000000',
            'endNum':100,
            'operation':1,
            'reFreshFlag':1,
            'startNum':1
            }
    UrlencParams=urllib.urlencode(params)
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "text/plain",
                "Cookie":"JSESSIONID="+Jsession+";",
                "Referer":"https://messages.megafon.ru/onebox/mix.do",
                "User-Agent":"curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5",
                "_umscsrf":InsertRandInString(_umscsrf)
                  }
    url=UrltoGet+UrlencParams
#    print "url:",url
    ChatListConnection=httplib.HTTPSConnection(UMSHOST)
    ChatListConnection.set_debuglevel(0)
    ChatListConnection.request('GET', url, '',headers)
    ChatListResp=ChatListConnection.getresponse()
    xml=ChatListResp.read()
#    fd=open('./chats.xml','w')
#    fd.write(xml)
#    fd.close()
#    print xml
    return xml

def xmlGetChat(Jsession,_umscsrf):
#https://messages.megafon.ru/onebox/oneboxList.do?umReq.ctlg=1%2C2&umReq.numFlg=1&umReq.mType=2053&umReq.srt=0&umReq.lType=0&umReq.dFlg=0&umReq.srtDr=0&umReq.rdFlg=0&umReq.bNum=1&umReq.eNum=50&umReq.snd=%2B79262001208&umReq.rcv=%2B79262001222&umReq.bTime=&umReq.eTime=&umReq.impt=-1&umReq.t=&umReq.threadFlag=1&rownid=0.576959018029553    
    UrltoGet='/onebox/oneboxList.do?'
    params={
            #    'rownid':0.576959018029553
            'umReq.bNum':1,
            'umReq.bTime':'',
            'umReq.ctlg':'1,2',
            'umReq.dFlg':0,
            'umReq.eNum':50,
            'umReq.eTime':'',
            'umReq.impt':-1,
            'umReq.lType':0,
            'umReq.mType':2053,
            'umReq.numFlg':1,
            'umReq.rcv':'+79262001222',
            'umReq.rdFlg':0,
            'umReq.snd':'+79262001223',
            'umReq.srt':0,
            'umReq.srtDr':0,
            'umReq.t':'',
            'umReq.threadFlag':1
            }
    UrlencParams=urllib.urlencode(params)
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "text/plain",
                "Cookie":"JSESSIONID="+Jsession+";",
                "Referer":"https://messages.megafon.ru/onebox/mix.do",
                "User-Agent":"curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5",
                "_umscsrf":InsertRandInString(_umscsrf)
                  }
    url=UrltoGet+UrlencParams
    print "url:",url
    ChatListConnection=httplib.HTTPSConnection(UMSHOST)
    ChatListConnection.set_debuglevel(6)
    ChatListConnection.request('GET', url, '',headers)
    ChatListResp=ChatListConnection.getresponse()
    xml=ChatListResp.read()
    fd=open('./roldchats.xml','w')
    fd.write(xml)
    fd.close()
    return xml   
   
   

import ParseOptions
if __name__ == '__main__':
    print "GetMessagesList Module output:"
    (args,params)=ParseOptions.ParseOptions()
    (Jsession,_umscsrf)=GetAuthParams(args.name,args.password)
    print "Main: Jsession:",Jsession
    print xmlGetChatList(Jsession,_umscsrf)
    print xmlGetChat(Jsession,_umscsrf)
    pass
