#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-
'''
Created on Dec 18, 2012

@author: denirz@gmail.com 

'''
#import urllib2   # Probably we will not need it 
import httplib
import base64 
UMSHOST='messages.megafon.ru'

def UMSAuth(Username='9262001222',Password=''):
    '''
    Returns Jsession ID  or  0 , if  auth is not successfull 
    
    '''
    UsernameEncoded=base64.b64encode(Username)
    PasswordEncoded=base64.b64encode(Password)
    
    UMSURL='/userjson/weblogin.do?'
    UMSURL=UMSURL+'webloginReq.user='+UsernameEncoded
    UMSURL=UMSURL+'&webloginReq.secinfo='+PasswordEncoded
    UMSURL=UMSURL+'&imageVerifyCode='
    UMSURL=UMSURL+'&__checkbox_remember=false&__checkbox_keepmeloggedin=false'
    header=({"Accept": "*/*",
             "User-Agent":"curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5"
             })
    
    UMSConnection=httplib.HTTPSConnection(UMSHOST)
    UMSConnection.set_debuglevel(0)
    UMSConnection.request("GET", UMSURL,'',header)
    LoginAnswer=UMSConnection.getresponse()
    print LoginAnswer.status
        # TODO: to add here some check for the status 200 + catch Error  if HTTP Fails at all
#    print LoginAnswer.status
    print LoginAnswer.getheaders()    
    JSessionID=LoginAnswer.getheader('set-cookie').split(";")[0].split("=")[1]
    # we have to check , if auth is OK:
    AuthResponse=LoginAnswer.read()
    if AuthResponse=='{"returnFlg":true}':
        print JSessionID
        return JSessionID
    else:
        print "error"
        return 0


def get_umscsrf(JSession):
    '''
    need only  to  receive _umscsrf
    ''' 
    MIX_URL='/onebox/mix.do'
    headers={"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "Accept": "text/plain",
                 "Cookie":"JSESSIONID="+str(JSession),
                 "Referer":"https://messages.megafon.ru/onebox/mix.do",
                  "User-Agent":"curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5"
                  }
    mix_doConn=httplib.HTTPSConnection(UMSHOST)
    mix_doConn.request('POST', MIX_URL,'', headers)
    mix_resp=mix_doConn.getresponse()
    umscsrf=mix_resp.getheader('_umscsrf')
    print "_umscsrf:",umscsrf
    return umscsrf
#https://messages.megafon.ru/onebox/mix.do

if __name__ == '__main__':
    print UMSAuth('9262001222','609177')
    print UMSAuth('9262001222','609178')
    pass