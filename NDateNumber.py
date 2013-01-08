#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-
'''
Created on Jan 6, 2013

@author: denirz
 Module Assumes to  provide 2 Functions:
     1) NORMALIZE MSISDN  TO REQUIRED FORMAT +,+7,89,9
     2) MODIFY TIMESTRING IN GMT RECEIVED FROM  THE SYSTEM TO THE  READABLE FORMAT ACCORDING TO LOCAL TIME 
'''
#import string
import re
import time
from datetime import datetime,timedelta,tzinfo
#from dateutil.tz import tzlocal
#import dateutil.tz
#from dateutil import zoneinfo
import pytz
#from test.test_multiprocessing import DELTA

def NormMSISDN(msisdn,format):
    '''
    NormMSISDN(msisdn,format): returns normalized  *msisdn* to the   required format
    valuable *format* is: '+','7','926'
    '''
#    print msisdn
    # First -  we have to remove  () and spaces
#    res=re.compile(r'\s').sub('')
    wmsisdn=re.sub('\s|\(|\)','',msisdn)

    comp=re.compile(r'^\+[1-9]+')
    StartsFromPlus=comp.match(wmsisdn)
    comp8=re.compile(r'^8[1-9]+')
#    print wmsisdn
    StartsFrom8=comp8.match(wmsisdn)
#    print StartsFrom8
#    print" removed spaces:",wmsisdn
    # if  required format is international -  simpleast way: 
    if format=="+":
        if StartsFromPlus:
            return wmsisdn
        else:
            wmsisdn="+"+wmsisdn
        
        if StartsFrom8:
#            print "Starts from 8:",wmsisdn
            wmsisdn=re.sub('^\+8','+7',wmsisdn)
            return wmsisdn
        return wmsisdn
    
    if format=='7':
        if StartsFromPlus:
            wmsisdn=re.sub('^\+','',wmsisdn)
            return wmsisdn
        if StartsFrom8:
            wmsisdn=re.sub('^8', '7', wmsisdn,1)
            return wmsisdn 
        return wmsisdn
    
    if format=='926':
        if StartsFromPlus:
            wmsisdn=re.sub('^\+7','',wmsisdn)
            return wmsisdn
        if StartsFrom8:
            wmsisdn=re.sub('^8','',wmsisdn)
            return wmsisdn 
        return wmsisdn    
    
    # if required format not found 
    return wmsisdn
#    print wmsisdn
#    print result

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = timedelta(hours=offset)
        self.__dst = timedelta(hours=offset-1)
        self.__name = ''
    def utcoffset(self, dt):
        return self.__offset
    def tzname(self, dt):
        return self.__name
    def dst(self, dt):
        return self.__dst



def NormDate(dateString):
#    utc=pytz.UTC
    utc=pytz.timezone('UTC')
    print utc
    dateString=dateString
    UTCtime=datetime.strptime(dateString,'%Y%m%d%H%M%S')    
    print time.timezone
    timediff=timedelta(0,time.timezone)
    localtime=UTCtime-timediff
    print localtime
    
    
    now_aware = utc.localize(UTCtime)
    print "now aware:",now_aware
    print "tzinfo:",now_aware.tzinfo
    
    delta=timedelta(0,0,0,0,0,4)
    delta=timedelta(hours=+4)
    print delta
    t=now_aware+delta
    print t 
    print "------------------------"
    mtc=pytz.timezone('US/Eastern')
    now_aware = mtc.localize(UTCtime)
    print "now aware1:",now_aware
    
    
    print "Seconds:",UTCtime.second
    
#    
    utc_dt = datetime(UTCtime.year, UTCtime.month, UTCtime.day, UTCtime.hour,15,1,tzinfo=utc)
#    utc_dt = datetime(UTCtime.year, UTCtime.month, UTCtime.day, UTCtime.hour, UTCtime.min,UTCtime.second,tzinfo=utc)
    print "utc_dt:",utc_dt
    print UTCtime.tzinfo
    nowDT=datetime.now(tzlocal())
    print nowDT
#    print nowDT.tzlocal()
    t=datetime.now()
    print t 
    print"---:", UTCtime
    print"---:", datetime.now(FixedOffset(0))
    
#    print tzinfo.utcoffset(datetime.now().tzinfo)
    return dateString
    pass


if __name__ == '__main__':
    print NormMSISDN("8 (926) 2001222","926")
    print NormDate("20131231164523")
    pass
