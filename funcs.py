import GUI
import wx
from pymongo import MongoClient
class funcs(GUI.MyFrame1):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.db_con()
        self.acn = "accountname"
        self.pwd = "password"
        self.state = False

        # 綁定按鈕
        self.login.Bind(wx.EVT_BUTTON, self.login_button)
        self.establish.Bind(wx.EVT_BUTTON, self.establish_account)
    # 建立資料庫連線
    def db_con(self):
        self.client = MongoClient(host="localhost", port=27017)
        self.db = self.client.banned
    # 尋找帳號密碼
    def check_acc(self, acn):
        dacn = None
        dpwd = None
        for thing in self.db.user.find({self.acn:acn}):
            thing = dict(thing)
            dacn = thing[self.acn]
            dpwd = thing[self.pwd]
        return dacn, dpwd
    # 登入介面
    def login_button(self, event):
        iacn = self.input_account.Value
        ipwd = self.input_pass.Value
        cacn = None
        cpwd = None
        cacn, cpwd = self.check_acc(iacn)
        if cacn != None and cpwd == ipwd:
            # todo:彈出視窗顯示登入成功
            self.state = True
            print('ok')
        else:
            # todo:彈出視窗顯示登入失敗
            print('bad')
            pass
    # 建立帳號
    def establish_account(self, event):
        wacn = self.input_account.Value
        wpwd = self.input_pass.Value
        whacn, whpwd = self.check_acc(wacn)
        if whacn:
            # todo 彈出視窗顯示帳戶已存在
            print('account exist')
        else:
            # todo 彈出視窗顯示帳戶以增加完成
            self.db.user.insert_one({self.acn:wacn, self.pwd:wpwd})
            print('Account adding')
            