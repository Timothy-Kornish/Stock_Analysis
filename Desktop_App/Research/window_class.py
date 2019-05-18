import wx

class windowClass(wx.Frame):
    def __init__(self, parent, title):
        super(windowClass, self).__init__(parent, title = title, size = (300, 600)) # size  =  width, hieght
        #self.Center()
        #self.Move((800, 250))
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    windowClass(None, title = 'Epic Window')
    app.MainLoop()
