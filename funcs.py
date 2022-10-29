import GUI
import wx
from pymongo import MongoClient
class funcs(GUI.MyFrame1):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.db_con()
        self.acn = "accountname"
        self.pwd = "password"
        self.login.Bind(wx.EVT_BUTTON, self.login_button)
        self.state = False
    # 建立資料庫連線
    def db_con(self):
        self.client = MongoClient(host="localhost", port=27017)
        self.db = self.client.banned
    def login_button(self, event):
        iacn = self.input_account.Value
        ipwd = self.input_pass.Value
        cpwd = None
        for thing in self.db.user.find({self.acn:iacn}):
            thing = dict(thing)
            iacn = thing[self.acn]
            cpwd = thing[self.pwd]
        if cpwd == ipwd:
            print('login suiccessful')
        else:
            print('this account not establish yet')
