import funcs
import wx
if __name__ == '__main__':
    app = wx.App()
    frame = funcs.funcs(None)
    frame.Show()
    app.MainLoop()