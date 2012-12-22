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
    

def Chat(xmlToParse):
    return xmlParse(xmlToParse,'uniMsg')    
def xmlParse(xmlToParse,TagToParse):    
#    print   'ChatList(xmlToParse)'
#    print xmlToParse
    xml_DOM=parseString(xmlToParse)
#    print xml_DOM.nodeType
#    RootXML=xml_DOM.firstChild
    ChatSet=()
#    print TagToParse
#    tag=C1.tagName
    
#    print "tag:"+tag
#    print C1.childNodes
#    for i in  C1.childNodes:
#            print i.tagName
#    msgC=xml_DOM.getElementsByTagName('msgContact')
    msgC=xml_DOM.getElementsByTagName(TagToParse)

    for msg in msgC:
        chatDC=TagParamsFrom_msgContact(msg)
        ChatSet=ChatSet +(chatDC,)
    return ChatSet
#    print ChatSet
        
#       Chat 
#    
#    xml_DOM

def TagParamsFrom_msgContact(msgContactElement):
    MsgAttr=msgContactElement.firstChild
    MsgDict={}
    while MsgAttr<>None:
#        if MsgAttr.hasAttributes():  print 'hasAttr:',MsgAttr.hasAttributes()
#        if not MsgAttr.hasChildNodes(): print 'hasChildNodes:',MsgAttr.hasChildNodes()
#        print 'Type:',MsgAttr.firstChild.hasAttribute('data')
#        print MsgAttr.tagName
        
        try:
            Data=MsgAttr.firstChild.data
        except AttributeError: 
            Data=''
        MsgDict[MsgAttr.tagName]=Data
        
#        if Data=='':
#            MsgDict[MsgAttr.tagName]=''
#            print "\t_"
#        else:
#            print "\t",Data
        MsgAttr=MsgAttr.nextSibling
    return MsgDict
    pass

from UMSClientLogin import UMSHOST, InsertRandInString, GetAuthParams
from GetMessagesList import xmlGetChatList,xmlGetChat
import  ParseOptions 
if __name__ == '__main__':
    print "Main ParseXMLChatList:"
    (options,args)=ParseOptions.ParseOptions()
    (JsessionID,umscsrf)=GetAuthParams(options.name,options.password)
    print (JsessionID,umscsrf)
    xml=xmlGetChatList(JsessionID,umscsrf)
    print xml
    print "ChatLists:",ChatLists(xml)
    
    xml=xmlGetChat(JsessionID,umscsrf,'+79262001222','+79262001222',10)
    print "Chat:",Chat(xml)
    j=1
    for i in Chat(xml):
        print j,"\t",i['ttl'],i['txtType']
        j+=1
    pass