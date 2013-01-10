#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-

'''
Created on Jan 6, 2013

@author: denirz
'''
import unittest
from NDateNumber import NormMSISDN,NormDate

class Test(unittest.TestCase):


    def testNormMSISDN(self):
        inp='9262001222'
        outp='+79262001222'
        r=NormMSISDN(inp,'+')
        self.assertEqual(r,outp,'expected:'+outp+' received:'+ r)
        inp='+79262001222'
        outp=inp
        r=NormMSISDN(inp,'+')
        self.assertEqual(r, outp,'expected:'+outp+' received:'+ r)
        inp='+7926 2001222'
        outp='+79262001222'
        r=NormMSISDN(inp,'+')
        self.assertEqual(r, outp,'expected:'+outp+' receied:'+ r)
        inp='+7 9262001222'
        outp='+79262001222'
        r=NormMSISDN(inp,'+')
        self.assertEqual(r, outp,'expected:'+outp+' receied:'+ r)
        inp='7(926) 2001222'
        outp='+79262001222'
        r=NormMSISDN(inp,'+')
        self.assertEqual(r, outp,'expected:'+outp+' received:'+ r)
        
        inp='7(926) 2001222'
        flag='7'
        outp='79262001222'
        r=NormMSISDN(inp,flag)
        self.assertEqual(r, outp,'input:'+inp+":"+flag+'expected:'+outp+' received:'+ r)
        
        inp='8(986) 2001222'
        flag='+'
        outp='+79862001222'
        r=NormMSISDN(inp,flag)
        self.assertEqual(r, outp,'input:'+inp+":"+flag+'expected:'+outp+' received:'+ r)
        
        inp='8(986) 2001222'
        flag='7'
        outp='79862001222'
        r=NormMSISDN(inp,flag)
        self.assertEqual(r, outp,'input:'+inp+":"+flag+'expected:'+outp+' received:'+ r)

        inp='+7(986) 2001222'
        flag='7'
        outp='79862001222'
        r=NormMSISDN(inp,flag)
        self.assertEqual(r, outp,'input:'+inp+":"+flag+'expected:'+outp+' received:'+ r)

        inp='8(986) 2001222'
        flag='926'
        outp='9862001222'
        r=NormMSISDN(inp,flag)
        self.assertEqual(r, outp,'input:'+inp+":"+flag+'expected:'+outp+' received:'+ r)
        
        inp='+7(986) 2001222'
        flag='926'
        outp='9862001222'
        r=NormMSISDN(inp,flag)
        self.assertEqual(r, outp,'input:'+inp+":"+flag+'expected:'+outp+' received:'+ r)
    def testNormTime(self):
        inputs='20131212235945'
        output=NormDate(inputs)
#        print output.hour 
        self.assertEqual(output.hour,3,"время не перенеслось через 12 ")
        inputs='20131231235945'
        output=NormDate(inputs)
        self.assertEqual(output.day, 1, 'день не перенеесся')
        self.assertEqual(output.year, 2014, 'год не перененеcен')
        
        
    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()