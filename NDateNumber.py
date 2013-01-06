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
if __name__ == '__main__':
    print NormMSISDN("8 (926) 2001222","926")

    pass
