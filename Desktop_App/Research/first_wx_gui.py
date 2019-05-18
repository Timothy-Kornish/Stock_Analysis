import wx

app = wx.App()

frame = wx.Frame(None, -1, 'gui.__init__')#, style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLOSE_BOX | wx.CAPTION)
frame.Show()

app.MainLoop()
