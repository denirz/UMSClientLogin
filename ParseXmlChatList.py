#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-
'''
Created on Dec 22, 2012

@author: denirz
THis module  contains modules that are required to parse xml with chat lists and retum tuples  With  data from them
'''
from xml.dom.minidom import parse, parseString
#import xml.dom.minidom
import xml.dom.minidom 
def ChatLists(xmlToParse):
    return xmlParse(xmlToParse,'msgContact')
    
def xmlParse(xmlToParse,TagToParse):    
#    print   'ChatList(xmlToParse)'
#    print xmlToParse
    xml_DOM=parseString(xmlToParse)
#    print xml_DOM.nodeType
    RootXML=xml_DOM.firstChild
    ChatsSet=()
#    tag=C1.tagName
    
#    print "tag:"+tag
#    print C1.childNodes
#    for i in  C1.childNodes:
#            print i.tagName
#    msgC=xml_DOM.getElementsByTagName('msgContact')
    msgC=xml_DOM.getElementsByTagName(TagToParse)

    for msg in msgC:
        chatDC=ChatParamsFrom_msgContact(msg)
        ChatSet=ChatsSet +(chatDC,)
    return ChatSet
#    print ChatSet
        
#       Chat 
#    
#    xml_DOM

def ChatParamsFrom_msgContact(msgContactElement):
    MsgAttr=msgContactElement.firstChild
    MsgDict={}
    while MsgAttr<>None:
#        if MsgAttr.hasAttributes():  print 'hasAttr:',MsgAttr.hasAttributes()
#        if not MsgAttr.hasChildNodes(): print 'hasChildNodes:',MsgAttr.hasChildNodes()
#        print MsgAttr.tagName
#        print "\t",MsgAttr.firstChild.data
        MsgDict[MsgAttr.tagName]=MsgAttr.firstChild.data
        MsgAttr=MsgAttr.nextSibling
    return MsgDict
    pass

from UMSClientLogin import UMSHOST, InsertRandInString, GetAuthParams
from GetMessagesList import xmlGetChatList
import  ParseOptions 
if __name__ == '__main__':
    print "Main ParseXMLChatList:"
    (options,args)=ParseOptions.ParseOptions()
    (JsessionID,umscsrf)=GetAuthParams(options.name,options.password)
    print (JsessionID,umscsrf)
    xml=xmlGetChatList(JsessionID,umscsrf)
    print ChatLists(xml)
    pass