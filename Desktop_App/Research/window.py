import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        menuBar = wx.MenuBar()
        panel = wx.Panel(self)

        fileButton = wx.Menu()
        editButton = wx.Menu()
        viewButton = wx.Menu()
        findButton = wx.Menu()
        helpButton = wx.Menu()

        importItem = wx.Menu()
        importItem.Append(wx.ID_ANY, 'Import Document')
        importItem.Append(wx.ID_ANY, 'Import Picture')
        importItem.Append(wx.ID_ANY, 'Import Video')

        fileButton.AppendMenu(wx.ID_ANY, 'Import', importItem)

        toolBar = self.CreateToolBar()
        quitToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('exit.png'))
        importToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Import', wx.Bitmap('exit.png'))
        toolBar.Realize()
        self.Bind(wx.EVT_TOOL, self.Quit, quitToolButton)

        #exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Status msg...')
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Exit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('exit.png'))
        fileButton.AppendItem(exitItem)

        editButton = wx.Menu()

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')
        menuBar.Append(viewButton, 'View')
        menuBar.Append(findButton, 'Find')
        menuBar.Append(helpButton, 'Help')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        nameBox = wx.TextEntryDialog(None, 'What is you name?','Welcome','name')
        userName = ''
        if nameBox.ShowModal() == wx.ID_OK:
            userName = nameBox.GetValue()

        yesNoBox = wx.MessageDialog(None, 'Do you enjoy wxPython?', 'Question', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()
        if yesNoAnswer == wx.ID_NO:
            userName = 'Loser!'

        chooseOneBox = wx.SingleChoiceDialog(None, 'What is you favorite color?',
                                            'Color Question',
                                            ['Green', 'Red', 'Blue', 'Yellow'])

        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()


        wx.TextCtrl(panel, pos = (3, 100), size = (120, 50))

        aweText = wx.StaticText(panel, -1, 'Awesome Text', (3,3))
        aweText.SetForegroundColour('yellow')
        aweText.SetBackgroundColour('black')

        rlyAweText = wx.StaticText(panel, -1, 'Customized Awesomeness', (3,30))
        rlyAweText.SetForegroundColour(favColor)
        rlyAweText.SetBackgroundColour('black')

        title = 'welcome ' + userName if userName else 'welcome'
        self.SetTitle(title)
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None, title = 'epic window')
    app.MainLoop()


if __name__ == '__main__':
        main()
