# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.login_phase = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel17 = wx.Panel( self.login_phase, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.account = wx.StaticText( self.m_panel17, wx.ID_ANY, u"account", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.account.Wrap( -1 )
		gSizer3.Add( self.account, 0, wx.ALL, 5 )
		
		self.input_account = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.input_account, 0, wx.ALL, 5 )
		
		self.password = wx.StaticText( self.m_panel17, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )
		gSizer3.Add( self.password, 0, wx.ALL, 5 )
		
		self.input_pass = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.input_pass.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		gSizer3.Add( self.input_pass, 0, wx.ALL, 5 )
		
		self.establish = wx.Button( self.m_panel17, wx.ID_ANY, u"establish", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.establish, 0, wx.ALL, 5 )
		
		self.login = wx.Button( self.m_panel17, wx.ID_ANY, u"login", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.login, 0, wx.ALL, 5 )
		
		
		self.m_panel17.SetSizer( gSizer3 )
		self.m_panel17.Layout()
		gSizer3.Fit( self.m_panel17 )
		self.login_phase.AddPage( self.m_panel17, u"a page", False )
		
		bSizer1.Add( self.login_phase, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

