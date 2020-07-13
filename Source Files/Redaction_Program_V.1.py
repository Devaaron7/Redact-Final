import wx 
import os
import re
import demo

rfile = open("banned_words.txt", "r")

blist = rfile.read()

flist = blist.split("\n")

class CalcFrame(demo.MyFrame1): 
   def __init__(self,parent): 
      demo.MyFrame1.__init__(self,parent)  
		
   def FindSquare(self,event): 
      in_text = str(self.m_textCtrl1.GetValue())
      ftext = ""
      ftext += in_text
      for y in range(0, len(flist)):
         temp = re.sub(r"\b{}\b".format(flist[y].title()),"<redacted>" ,in_text)
         in_text = temp
         temp = re.sub(r"\b{}\b".format(flist[y].lower()),"<redacted>" ,in_text)
         in_text = temp 
         temp = re.sub(r"\b{}\b".format(flist[y].upper()),"<redacted>" ,in_text)
         in_text = temp 
      self.m_textCtrl2.SetValue (in_text) 
        
app = wx.App(False) 
frame = CalcFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop() 