'''
Created on Jan 6, 2013

@author: denirz
'''
import unittest
from UMSClientLogin.NDateNumber import NormMSISDN

class Test(unittest.TestCase):


    def testNormMSISDN(self):
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
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()