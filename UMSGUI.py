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
        self.pack()
        self.createTopFrame()
        self.createSearchFrame()
        MainFrame=self.createMainFrame()
        self.putChatItem(MainFrame)
        
        self.createWidget()
        pass
    def createTopFrame(self):
        self.topFrame=Frame(self,width='200',height='10') # to enhance later the size of the frame
        self.topFrame.pack(side='top',fill='x')
        self.tempTopLabel=Label(self.topFrame,text='[------------TopFrame]')
        self.tempTopLabel.pack(side='right')
        pass
    def createSearchFrame(self):
        self.searchFrame=Frame(self)
#        self.searchFrame['width']=self.topFrame['width']
        self.searchFrame['height']='20'
        self.searchFrame['background']='Green'
        self.searchFrame.pack(side='top',fill='x')
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
        pass
    def createWidget(self):
        pass 
    

if __name__ == '__main__':
    root=Tk()
    app=Application(master=root)
    app.mainloop()
    app.destroy()
    pass