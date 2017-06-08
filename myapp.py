#coding:utf-8
import wx
import json
import urllib
import base64
import socket
import struct
import string
class myApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None,-1,'MY APP',pos = (50, 50),size = (1000, 1000),style = wx.DEFAULT_FRAME_STYLE,name = 'myApp')
        panel = wx.Panel(frame, -1)
        self.text1 = wx.TextCtrl(panel,-1,pos = (50, 50),size = (800, 400),style = wx.TE_RICH|wx.TE_MULTILINE)
        self.text2 = wx.TextCtrl(panel,-1,pos = (50, 600),size = (800, 400),style = wx.TE_RICH|wx.TE_MULTILINE)
        self.button1 = wx.Button(panel,-1,"JSON FORMAT",pos = (50, 520))
        self.button2 = wx.Button(panel,-1,"URL DECODE",pos = (160, 520))
        self.button3 = wx.Button(panel,-1,"BASE64 DECODE",pos = (270,520))
        self.button4 = wx.Button(panel,-1,"IP CONVERT",pos = (390,520))
        self.Bind(wx.EVT_BUTTON,self.OnButton1,self.button1)
        self.Bind(wx.EVT_BUTTON,self.OnButton2,self.button2)
        self.Bind(wx.EVT_BUTTON,self.OnButton3,self.button3)
        self.Bind(wx.EVT_BUTTON,self.OnButton4,self.button4)
        frame.Show()
        return True
    def OnButton1(self, event):
        try:
            text = json.loads(self.text1.GetValue(),"unicode")
            self.text2.SetValue(json.dumps(text,indent=4))
        except:
            self.text2.SetValue(u"\t\t\t\tcheck input")
    def OnButton2(self, event):
        try:
            self.text2.SetValue(urllib.unquote(self.text1.GetValue().encode("ascii")).decode("utf-8"))
        except:
            self.text2.SetValue(u"\t\t\t\tcheck input")
    def OnButton3(self, event):
        try:
            self.text2.SetValue(base64.b64decode(self.text1.GetValue().encode("ascii")).decode("utf-8"))
        except:
            self.text2.SetValue(u"\t\t\t\tcheck input")
    def OnButton4(self, event):
        try:
            int_ip = string.atoi(self.text1.GetValue().encode("ascii"))
            self.text2.SetValue(socket.inet_ntoa(struct.pack('>I',int_ip)))
        except:
            self.text2.SetValue(str(socket.ntohl(struct.unpack('I',socket.inet_aton(self.text1.GetValue().encode("ascii")))[0])))
            print self.text2.GetValue()
app = myApp()
app.MainLoop()