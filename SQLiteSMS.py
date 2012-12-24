#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-

'''
Created on Dec 23, 2012

@author: denirz
'''
import sqlite3
DBNAME='./example.db'
def  dbConnection():
    '''
    will check if databse & Table  for _ChatList_ Exista. 
    if YES -  returns   Connections descriptor  to this Database.
    if NO -  creates it 
    '''
    conn = sqlite3.connect(DBNAME)
    Cursor=conn.cursor()
    SqlCreateString='CREATE TABLE IF NOT EXISTS ChatList (\
            MSISDN TEXT,\
            msgCtnt TEXT,\
            unReadMsgNum INTEGER,\
            msgNum INTEGER,\
            msgType INTEGER,\
            maxTime TEXT\
            )'
    Cursor.execute(SqlCreateString)
    conn.commit()
    SqlCreateString='CREATE TABLE IF NOT EXISTS Messages (\
                osz,\
                txtType,\
                cc,\
                oID,\
                mdType,\
                dFlg,\
                mCls,\
                duration,\
                txt,\
                cNum,\
                rcv,\
                state,\
                rpFlg,\
                usr,\
                rdFlg,\
                attachInfo,\
                channel,\
                snd,\
                sz,\
                fwdFlg,\
                pID,\
                ctlg,\
                cmnt,\
                drct,\
                lType,\
                impt,\
                ttl,\
                msgID,\
                flt,\
                bcc,\
                mType,\
                t\
                )'
    Cursor.execute(SqlCreateString)
    conn.commit()
                
    return conn
#import re
def putItemIntoDb(objectSer,conn,TableName):
    '''
    INSERT ITEM INTO DB
    do it Without any  conditions! 
    '''
    Cursor=conn.cursor()
    strSQL='INSERT INTO '+TableName+ '('
    ColumnKeys=''
    ValuesKeys=''
    for Key in objectSer.keys():
        ColumnKeys=ColumnKeys+Key+','
        ValuesKeys=ValuesKeys+'"'+objectSer[Key].replace('"','') +'"'+','
    strSQL=strSQL+ColumnKeys[:-1] + ') VALUES ('+ ValuesKeys[:-1]+')'
    print strSQL
    Cursor.execute(strSQL)
    conn.commit()
    
def deleteItemFromDb(ObjectSer,conn,TableName,KeyFieldSet):
    ''''
    Should delete  in Db all items that a  similar to   the _ObjectSer_
    and then add objectSer itself into the DB 
    DELETE FROM TableName WHERE (KeyField=ObjectSer[KeyField] AND KeyField2=ObjectSer[KeyField2] AND ...)
    '''
    pass
    #First Delete:
    strSQL='DELETE FROM '+TableName+' WHERE ( '
    for KeyField in KeyFieldSet:
        strSQL=strSQL+KeyField+'="'+ObjectSer[KeyField]+'" AND '
    strSQL=strSQL[:-4]+")"
    print "DLETE SQL",strSQL
    Cursor=conn.cursor()
    print Cursor.execute(strSQL)

def checkItemInDb(item,db,TableName,KeyFieldSet):
    strSQL='SELECT * FROM '+TableName+' WHERE ('
    for KeyField in KeyFieldSet:
#        print item[KeyField]
#        print item.values()
        strSQL=strSQL+ KeyField+'="'+item[KeyField]+'" AND '
    strSQL=strSQL[:-4]+")"
    print strSQL 
    cur=db.cursor()
    cur.execute(strSQL)
    exdata=cur.fetchone()
    print exdata
    if exdata:
        return "yes"
    else:
        return 'no'
        
    pass 
    

def dbAddChatList(Chats):
    '''
    Experimental addition of chat List to  SQLite 
    '''
    db=dbConnection()
    if len(Chats)==0:
        return "no Chats to insert"
    for item  in Chats[:2000]:
        if checkItemInDb(item,db,'ChatList',('MSISDN','maxTime'))=='no':
            deleteItemFromDb(item,db,'ChatList',('MSISDN',))
            putItemIntoDb(item,db,'ChatList')
#        else:
#            deleteItemFromDb(item,db,'ChatList',('MSISDN',))
#            putItemIntoDb(item,db,'ChatList')
            
#        putItemIntoDb(item,db,'ChatList')
#        deleteItemFromDb(item,db,'ChatList',('MSISDN','maxTime'))
#        print checkItemInDb(item,db,'ChatList',('MSISDN','maxTime'))

def dbAddMessages(MessageSet):
    conn=dbConnection()
    for Message in MessageSet:
#       PUT ALL MESSAGES into DB:
#        putItemIntoDb(Message,conn,'Messages')
#        Check if message is inside Db:
        print checkItemInDb(Message,conn,'Messages',('msgID',))
#        checkItemInDb(Messae)
    pass
    



import  ParseOptions 
from ParseXmlChatList import ChatLists, Chat 
from GetMessagesList import xmlGetChatList,xmlGetChat
from UMSClientLogin import  GetAuthParams
if __name__ == '__main__':
    print "Main ParseXMLChatList:"
    (options,args)=ParseOptions.ParseOptions()
    (JsessionID,umscsrf)=GetAuthParams(options.name,options.password)
    print (JsessionID,umscsrf)
    xml=xmlGetChatList(JsessionID,umscsrf)
##    print xml
#    of=open("./chats_unread.xml",'w')
#    of.write(xml)
#    of.close()
    ChatLs=ChatLists(xml)
    print "ChatLists:",ChatLs
    dbAddChatList(ChatLs)
    
    xml=xmlGetChat(JsessionID,umscsrf,'+79262001222','SMENA',14)
    MessageSet=Chat(xml)
#    dbAddMessages(MessageSet)
