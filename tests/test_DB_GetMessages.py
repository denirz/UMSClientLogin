'''
Created on Jan 6, 2013

@author: denirz
'''
import unittest
from UMSClientLogin.DB_GetMessages import getChats
class Test(unittest.TestCase):

    def test_get20Chats(self):
        ChatL=getChats(20)
        print ChatL
        self.assertEqual(len(ChatL), 20, ' retieved less than 20  items')
        pass
    def test_getChatsN(self):
        self.getChats(200)
        
    def getChats(self,num=20):
        ChatL=getChats(num)
#        print len(ChatL)
        self.assertEqual(len(ChatL), num, ' retieved less than'+str(num)+'items')
        pass
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()