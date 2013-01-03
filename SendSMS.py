#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-

'''
Created on Dec 19, 2012

@author: denirz
'''

from UMSClientLogin import GetAuthParams, InsertRandInString, UMSHOST
import httplib
import urllib

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
                "Referer":UMSHOST+"/onebox/mix.do",
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
    Text=Options.text
    Phone=Options.dest
    print Text,Phone
    Flash=Options.flash
    print "Login parameters:",Username,Password
    (JSessionID,_umscsrf)=GetAuthParams(Username,Password)
    print "JSessionID",JSessionID,_umscsrf

    if _umscsrf<>0:
        xml=SendSMS(JSessionID,_umscsrf,Phone,Text,Flash)
        print xml
    pass
    