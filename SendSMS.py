#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-

'''
Created on Dec 19, 2012

@author: denirz
'''

from UMSClientLogin import GetAuthParams, InsertRandInString, UMSHOST
import httplib
import urllib
'''
def xmlGetChatList(Jsession):
    params={ 
         'chatMsgType':'10100000000100000000000000000000',
         'endNum':'100',
         'operation':'1',
         'reFreshFlag':'1',
         'startNum':'1',
         }
#    print params
    print UMSHOST
    ListMsgURL='/onebox/getChatList.do?'
    for var in params.keys():
            ListMsgURL=ListMsgURL+'&'+var+'='+params[var]
    print ListMsgURL
#    ListMsgURL='/onebox/getChatList.do?startNum=1&endNum=100&reFreshFlag=1&operation=1&chatMsgType=10100000000100000000000000000000'
#    startNum=1&endNum=100&reFreshFlag=1&operation=1&chatMsgType=10100000000100000000000000000000
    headers = {"Content-type": "application/x-www-form-urlencoded",
                 "Accept": "text/plain",
                 "Cookie":"JSESSIONID="+Jsession}
#    print headers
    ListConnection=httplib.HTTPSConnection(UMSHOST)
    ListConnection.set_debuglevel(6)
    ListConnection.request('GET', ListMsgURL,'', headers)
    listresp=ListConnection.getresponse()
    xml=listresp.read()
    print "headers LISTConnection:", listresp.getheaders()
#    fd=open('./list.xml','w')
#    fd.write(xml)
#    fd.close()
    return xml
#https://messages.megafon.ru/onebox/getChatList.do?startNum=1&endNum=100&reFreshFlag=1&operation=1&chatMsgType=10100000000100000000000000000000&t=0.819595287356757
'''

def SendSMS(JSession,_umscsrf,NumberTo,Text,Flash=0):
    '''
    SendSMS(JSession,_umscsrf,NumberTo,Text,Flash=0) Sends SMS to number NumberTo... 
    Jsession and _umscsfr are taken from login and first query
    _umscsrf is enlarged inside  Function  
    
    returns XML response that  you could analyze to check what actually is wrong if any.
    '''
    # https://messages.megafon.ru/onebox/sendSMS.do
    SMSSendURL='/onebox/sendSMS.do'
    params={
        'cid':'',
        'datetime':'',
        'deleteAttachBoolean':0,
        'emailAttachContentIDList':'',
        'emailSignature':'',
        'flashflag':Flash,
        'hour':'00',
        'longSMSMark':0,
        'minute':00,
        'msgContent':Text, 
        'msgID':'',
        'msgType_Operation':0,
        'msg_Operation':0,
        'regularlySendTime':'',
        'sendNowTime':'',
        'to':NumberTo+';',
        'updateOperating':''
        }
#    print params
    UrlencParams=urllib.urlencode(params)
#    print UrlencParams
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "text/plain",
                "Cookie":"JSESSIONID="+JSession+";",
                "Referer":"https://messages.megafon.ru/onebox/mix.do",
                "User-Agent":"curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5",
                "_umscsrf":InsertRandInString(_umscsrf)
                  }
#    print  headers
    SendSMSConnection=httplib.HTTPSConnection(UMSHOST)
    SendSMSConnection.set_debuglevel(0)
    SendSMSConnection.request('POST', SMSSendURL,UrlencParams, headers)
    SendResp=SendSMSConnection.getresponse()
    return  SendResp.read()
    

import ParseOptions

if __name__ == '__main__':
    (Options,Args)=ParseOptions.ParseOptions()
    
    Username=Options.name
    Password=Options.password
#    Text=Options.text.encode("utf-8")
    Text=Options.text
    Phone=Options.dest
    print Text,Phone
    Flash=Options.flash
    print "Login parameters:",Username,Password
    (JSessionID,_umscsrf)=GetAuthParams(Username,Password)
    print "JSessionID",JSessionID
    '''
    JSessionID=UMSAuth(Username,Password)
    print JSessionID
    if JSessionID==0:
        print  "Error"
    else:
        _umscsrf=get_umscsrf(JSessionID)
#        print xmlGetChatList(JSessionID)
    '''
    if _umscsrf<>0:
        xml=SendSMS(JSessionID,_umscsrf,Phone,Text,Flash)
        print xml
    pass
    