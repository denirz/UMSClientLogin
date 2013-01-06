#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-

'''
Created on Jan 6, 2013

@author: denirz
'''
import sqlite3
from ParseOptions import ParseOptions
from SQLiteSMS import  dbConnection
def getChats(NumberOfChats=20):
    '''
    Connection to the DB is Taken from *SQLiteSMS.dbConnection()*
    getChats  returns  _NumberOfChats_ Chats items 
    - Chats are located  in "ChatLists" table of  the filename
    - SELECT  MSISDN,msgCtnt,maxTime FROM ChatList ORDER BY maxTime DESC  LIMIT   NumberOfChats; 
    ##returns
    - a Tuple of Tuples _*(ChatFrom,ChatTime,ChatText)*_
    '''
    connect=dbConnection()
    selectString='SELECT  MSISDN,msgCtnt,maxTime FROM ChatList ORDER BY maxTime DESC  LIMIT '+ str(NumberOfChats)+";"
#    print selectString
    cur=connect.cursor() 
    cur.execute(selectString)
    Chats=()
    for ChatItem in cur.fetchall():
        ChatFrom=ChatItem[0]
        ChatText=ChatItem[1]
        ChatTime=ChatItem[2]
        Chats=Chats+((ChatFrom,ChatTime,ChatText),)
    return Chats
    

if __name__ == '__main__':
    (args,params)=ParseOptions()
    print args,params
    print getChats(2)[-1]
    pass