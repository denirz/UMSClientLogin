#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-
'''
Created on Jan 5, 2013

@author: denirz
'''
import unittest
from UMSClientLogin import InsertRandInString
import UMSClientLogin
from ParseOptions import  ParseOptions
#from UMSClientLogin.GetMessagesList import Jsession

class TestGetAuthParams(unittest.TestCase):

    def test_CorrectLogin(self):
        (session,umscsrf)=UMSClientLogin.GetAuthParams('9262001222', '609177')
#        print len(umscsrf),len(session)
        self.assertEquals(len(umscsrf), 13,'9262001222  неверная длина  UMSCSRF')
        self.assertEquals(len(session), 32, '9262001222  неверная длина JsessionID')
        
        (session,umscsrf)=UMSClientLogin.GetAuthParams('79262001222', '609177')
#        print umscsrf
        self.assertEquals(len(umscsrf), 13,'79262001222 неверная длина UMSCSRF ')
        self.assertEquals(len(session), 32, '7926200122 неверная  длина JSessionID  ')
        
    def test_WrongPassword(self):
        (session,umscsrf)=UMSClientLogin.GetAuthParams('79262001222', '60917e')
#        print umscsrf,session
        self.assertEqual(umscsrf,0)
        self.assertEqual(session, 0, 'session ID не равен 0 ')
    def test_WrongUserName(self):
        (session,umscsrf)=UMSClientLogin.GetAuthParams('+79262001222', '609177')
#        print umscsrf,session
        self.assertEqual(umscsrf,0)
        self.assertEqual(session, 0, 'sessionID  не равен 0')
 
class TestRandInsert(unittest.TestCase):
    def test_InsertRandInString(self):
        stringto='1234567890ABC'       
        Longerstring=InsertRandInString(stringto)
        print Longerstring
        self.assertEqual(len(Longerstring), 18, Longerstring+' длина не равна 18')
    def test_InsertRandStringShort(self):
        stringto='123'       
        Longerstring=InsertRandInString(stringto)
        print Longerstring
        self.assertTrue(len(Longerstring)<18, Longerstring+' Длина больше 18')
        stringto=''       
        Longerstring=InsertRandInString(stringto)
        print Longerstring
        self.assertTrue(len(Longerstring)<18, Longerstring+' Длина больше 18')
        
if __name__ == "__main__":
#    (args,options)=ParseOptions()
#    print args
#    print options
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()