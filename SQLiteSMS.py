#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-

'''
Created on Dec 23, 2012

@author: denirz
Finction   to Put  ChatSets  and MessageSet into database 
'''
import sqlite3
DBNAME='./example.db'
DEBUGLEVEL=0
def  dbConnection():
    '''
    will check if database & Table  for _ChatList_ Exists. 
    if YES -  returns   Connections descriptor  to this Database.
    if NO -  creates it  and returns the connection 
    _ChatList_  - is a table for Chats 
    _Messages_  - is a table for messages  
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

def putItemIntoDb(objectSer,conn,TableName):
    '''
    putItemIntoDb(objectSer,conn,TableName): 
    Inserts Item _objectSer_ INTO DB  table _TableName_ of _conn_ database
     
    Does it Without any  conditions! 
    '''
    Cursor=conn.cursor()
    strSQL='INSERT INTO '+TableName+ '('
    ColumnKeys=''
    ValuesKeys=''
    for Key in objectSer.keys():
        ColumnKeys=ColumnKeys+Key+','
        ValuesKeys=ValuesKeys+'"'+objectSer[Key].replace('"','') +'"'+','
    strSQL=strSQL+ColumnKeys[:-1] + ') VALUES ('+ ValuesKeys[:-1]+')'
    if DEBUGLEVEL:print strSQL
    Cursor.execute(strSQL)
    conn.commit()
    
def deleteItemFromDb(ObjectSer,conn,TableName,KeyFieldSet):
    ''''
    Deletes from Db _conn_ all the items  similar to   the _ObjectSer_
    Similarity means _KeyFieldSet_ parameters to be equal  to  corresponding fields of tghe table _TableName_
    DELETE FROM TableName WHERE (KeyField=ObjectSer[KeyField] AND KeyField2=ObjectSer[KeyField2] AND ...)
    '''
    strSQL='DELETE FROM '+TableName+' WHERE ( '
    for KeyField in KeyFieldSet:
        strSQL=strSQL+KeyField+'="'+ObjectSer[KeyField]+'" AND '
    strSQL=strSQL[:-4]+")"
    if DEBUGLEVEL: print "DELETE SQL",strSQL
    Cursor=conn.cursor()
    Cursor.execute(strSQL)
    conn.commit()

def checkItemInDb(item,db,TableName,KeyFieldSet):
    '''
    Checks if the  _item_  exists in _TableName_ of _db_ database
    Similarity   means _KeyFieldSet_ fields of the  _item_ are equal to the  database record
    SELECT * FROM TableName WHERE (KeyFields=item[KeyFields] AND KeyField1=item[KryField1]...) 
    '''
    strSQL='SELECT * FROM '+TableName+' WHERE ('
    for KeyField in KeyFieldSet:
        strSQL=strSQL+ KeyField+'="'+item[KeyField]+'" AND '
    strSQL=strSQL[:-4]+")"
    if DEBUGLEVEL:print strSQL 
    cur=db.cursor()
    cur.execute(strSQL)
    exdata=cur.fetchone()
    if exdata:
        return "yes"
    else:
        return "no"
    

def dbAddChatList(Chats,NumberOfItemsToAnaalyze):
    '''
    Adds Set of Chat ( _Chats_) to the ChatList  to the  DataBase:
     Analyze only _NumberOfItemsToAnaalyze_
    if the old Version od Chat is already in the Database , so first we have to remove it from there
     
    '''
    db=dbConnection()
    if len(Chats)==0:
        return ('Error',)
    InsertedItems=()
    for item  in Chats[:NumberOfItemsToAnaalyze]:
        if checkItemInDb(item,db,'ChatList',('MSISDN','maxTime'))=='no':
            deleteItemFromDb(item,db,'ChatList',('MSISDN',))
            putItemIntoDb(item,db,'ChatList')
            InsertedItems=InsertedItems+(item,)
    return InsertedItems
    db.close()

def dbAddMessages(MessageSet):
    '''
    Add Messages _MessageSet_ to the Messages table of the DataBase
    '''
    conn=dbConnection()
    AddedMessages=()
    for Message in MessageSet:
        if checkItemInDb(Message,conn,'Messages',('msgID',))=='no':
            if DEBUGLEVEL:print "adding Message into DB"
            putItemIntoDb(Message,conn,'Messages')
            AddedMessages=AddedMessages+(Message,)
    return AddedMessages

def UpdateLocalSQLite(JsessionID,umscrf,ChatListDepth=10,ChatMessagesDepth=10,MyMSISDN='+79262001222'):
    '''
    UpdateLocalSQLite(JsessionID,umscrf,ChatListDepth=10,ChatMessagesDepth=10,MyMSISDN='+79262001222'):
     to be called every Time to update the  Local  Database from  Server;
    '''
    xml=xmlGetChatList(JsessionID,umscsrf)
    ChatLs=ChatLists(xml)
#    print "ChatLists To Insert:",ChatLs,"\n"
    insChats=dbAddChatList(ChatLs,ChatListDepth)
#    print "InsertedChats:",insChats
    
    for ChatItem in insChats:
        print MyMSISDN
        xml=xmlGetChat(JsessionID,umscsrf,MyMSISDN,ChatItem['MSISDN'],ChatMessagesDepth)
#        print xml
        MessageSet=Chat(xml)
        addedMessages=dbAddMessages(MessageSet)
        for msg in addedMessages:
            print 'AddedMessage: FROM:',msg['snd'],'TO:',msg['rcv'], 'TIME:',msg['t'],":"
            print '\t',msg['ttl']
#        print 'AddedMessages:',ChatItem['MSISDN'],len(addedMessages),addedMessages
    

############################### Main 
import  ParseOptions 
import NDateNumber
from ParseXmlChatList import ChatLists, Chat 
from GetMessagesList import xmlGetChatList,xmlGetChat
from UMSClientLogin import  GetAuthParams
if __name__ == '__main__':
    print "Main ParseXMLChatList:"
    (options,args)=ParseOptions.ParseOptions()
        
    (JsessionID,umscsrf)=GetAuthParams(options.name,options.password)
    print (JsessionID,umscsrf) 
    normname=NDateNumber.NormMSISDN(options.name, '+')
    print 'normname=',normname 
    UpdateLocalSQLite(JsessionID,umscsrf,20,40,normname)