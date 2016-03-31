#coding=utf-8
import wx

class Frame(wx.Frame):#显示图像的类，是wx.Frame子类
    pass
    def __init__(self,image,id=-1,
        pos=wx.DefaultPosition,
        title='Hello,wxPython!'):
        #显示图像

class APP(wx.App):
    def OnInit(self):
        self.frame = Frame(parent=None,tile='My TOOL')
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__=='__main__':
    app=APP()
    app.MainLoop()
