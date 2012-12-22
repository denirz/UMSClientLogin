#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-
'''
Created on Dec 22, 2012

@author: denirz
THis module  contains modules that are required to parse xml with chat lists and retum tuples  With  data from them
'''
from xml.dom.minidom import  parseString
import xml.dom.minidom 


def ChatLists(xmlToParse):
    '''
    ChatLists(xmlToParse):  Returns  Tuple of Dictionaries with Chats on th top 
    '''
    return xmlParse(xmlToParse,'msgContact')
    

def Chat(xmlToParse):
    '''
    Chat(xmlToParse): Returns Tuple of Dictionaries with Messages & their data.
    '''
    return xmlParse(xmlToParse,'uniMsg')    
def xmlParse(xmlToParse,TagToParse):    
    xml_DOM=parseString(xmlToParse)
    ChatSet=()
    msgC=xml_DOM.getElementsByTagName(TagToParse)

    for msg in msgC:
        chatDC=TagParamsFrom_msgContact(msg)
        ChatSet=ChatSet +(chatDC,)
    return ChatSet

def TagParamsFrom_msgContact(msgContactElement):
    '''
    Function that convert 1 level Item to Dictionary 0 Tag-valut.
    '''
    MsgAttr=msgContactElement.firstChild
    MsgDict={}
    while MsgAttr<>None:
        try:
            Data=MsgAttr.firstChild.data
        except AttributeError: 
            Data=''
        MsgDict[MsgAttr.tagName]=Data
        MsgAttr=MsgAttr.nextSibling
    return MsgDict

from UMSClientLogin import  GetAuthParams
from GetMessagesList import xmlGetChatList,xmlGetChat
import  ParseOptions 
if __name__ == '__main__':
    print "Main ParseXMLChatList:"
    (options,args)=ParseOptions.ParseOptions()
    (JsessionID,umscsrf)=GetAuthParams(options.name,options.password)
    print (JsessionID,umscsrf)
    xml=xmlGetChatList(JsessionID,umscsrf)
#    print xml
    of=open("./chats_unread.xml",'w')
    of.write(xml)
    of.close()
    ChatLs=ChatLists(xml)
    print "ChatLists:",ChatLs
    for i in ChatLs:
        print i 
    xml=xmlGetChat(JsessionID,umscsrf,'+79262001222','+79262131605',10)
    Messages=Chat(xml)
    print "Chat:",Messages
    print Messages[0].keys()
    j=1
    for i in Messages:
        print j,"\t",i['snd'],i['rcv'],i['msgID'],i['t'],":"
        print "\t\t",i['ttl']
        j+=1
    pass