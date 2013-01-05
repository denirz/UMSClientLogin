#__*__charsert:UTF-8__*__
# -*- coding: utf-8 -*-
'''
Created on Jan 3, 2013

@author: denirz
'''
from Tkinter import  * 
import tkFont
from twisted.conch.test.test_helper import HEIGHT

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
#        self['height']='2000'
        self.pack(expand=1)
        self.createTopFrame()
        self.createSearchFrame()
        MainFrame=self.createMainFrame()
        self.putChatItem(MainFrame)
        self.putChatItem(MainFrame,'+79262001223','2012-31-10','ну просто достаточно длинный текст чтобы его   было можно перенести, если понадобится - ибо а вдруг понадобится? ')
        self.putChatItem(MainFrame,'+79262001223','2012-31-11','и еще один такой- же ну просто достаточно длинный текст чтобы его   было можно перенести, если понадобится - ибо а вдруг понадобится? ')
        self.putChatItem(MainFrame, '+79262131605', '2013-04-01', 'ты  поганый и вонючий урод,   я тебя неавижу! ')
        self.putChatItem(MainFrame, '+79262131605', '2013-04-01', 'ты  поганый и вонючий урод,   я тебя неавижу! ')
        self.createWidget()
        pass
    def createTopFrame(self):
        self.topFrame=Frame(self,width='200',height='10') # to enhance later the size of the frame
#        self.topFrame['expand']='true'
        self.topFrame.pack(side='top',expand=1,fill='x')
        self.tempTopLabel=Label(self.topFrame,text='[------------TopFrame]')
        self.tempTopLabel.pack(side='right')
        self.refreshButton=Button(self.topFrame,text="refresh")
        self.refreshButton.pack(side='left')
        pass
    def createSearchFrame(self):
        self.searchFrame=Frame(self)
#        self.searchFrame['width']=self.topFrame['width']
        self.searchFrame['height']='20'
        self.searchFrame['background']='Green'
        self.searchFrame.pack(side='top',fill='x',expand=1)
        #label for the searchFrame: 
        self.tempSearchLabel=Label(self.searchFrame,text='[searchFrame]')
        self.tempSearchLabel.pack(side='left')
    def createMainFrame(self):
        # create a big SuperFrame with scrollbar &  frame
        self.mainSuperFrame=Frame(self)
        self.mainSuperFrame.pack(side='top',fill='both')
#        Create  a Scroll bar  on th right 
        self.mainScrollBar=Scrollbar(self.mainSuperFrame)
        self.mainScrollBar.pack(side='right',fill='y')
#         Create a Main  Frame
        self.mainFrame=Frame(self.mainSuperFrame,width='200',height='2000')
#        self.mainFrame['height']='2000'
        self.mainFrame['background']='Yellow'
        self.mainFrame.pack(side='left',fill='both')
        return self.mainFrame
#        # tempMainLabel:
#        self.tempMainLabel=Label(self.mainFrame,text='[tempMainFrame]')
#        self.tempMainLabel.pack(side='top',fill='x')
#        self.tempMainLabel=Label(self.mainFrame,text='[tempMainFrame]')
#        self.tempMainLabel.pack(side='bottom')
#        self.tempMainLabel=Label(self.mainFrame,text='[tempMainFrame]')
#        self.tempMainLabel.pack(side='bottom')

    def putChatItem(self,frame,source='+79262001222',date='2012-12-31',text='text просто проверка'):
        
        boldFont=tkFont.Font(family='Arial',size='10',weight='bold')
        itemF=Frame(frame)
        itemF.pack(side='top', fill='x',expand='1')
        itemFHeader=Frame(itemF)
        itemFHeader.pack(side='top',fill='x',expand='1')
        itemFText=Frame(itemF)
        itemFText.pack(side='top',fill='x',expand='1')
        
        self.Number=Label(itemFHeader,text=source)
        self.Number['font']=boldFont
        self.Number['justify']='right'
        self.Number.pack(side='right',fill='none')
        self.Date=Label(itemFHeader,text=date)
        self.Date['font']=boldFont
#        self.Date['underline']='1'
        self.Date['highlightthickness']='2'
        self.Date.pack(side='right',fill='none')
        
        self.smsText=Label(itemFText,text=text)
        self.smsText['wraplength']='250'
        self.smsText['justify']='left'
        self.smsText.pack(side='bottom',pady='0')
        pass
    def createWidget(self):
        pass 
    

if __name__ == '__main__':
    root=Tk()
    app=Application(master=root)
    app.mainloop()
    app.destroy()
    pass