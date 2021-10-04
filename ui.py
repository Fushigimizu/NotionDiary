# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class UIFrame_main
###########################################################################

class UIFrame_main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.titleLabel = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titleLabel.Wrap( -1 )

		bSizer13.Add( self.titleLabel, 0, wx.ALL, 5 )

		self.titleBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer13.Add( self.titleBox, 0, wx.ALL, 5 )

		self.bodyLabel = wx.StaticText( self, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bodyLabel.Wrap( -1 )

		bSizer13.Add( self.bodyLabel, 0, wx.ALL, 5 )

		self.bodyBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,250 ), 0 )
		bSizer13.Add( self.bodyBox, 0, wx.ALL, 5 )

		fgSizer7 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.sendButton = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.sendButton, 0, wx.ALL, 5 )

		self.configButton = wx.Button( self, wx.ID_ANY, u"Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.configButton, 0, wx.ALL, 5 )

		self.sendingText = wx.StaticText( self, wx.ID_ANY, u"To Send, Click \"Send\" Button", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.sendingText.Wrap( -1 )

		fgSizer7.Add( self.sendingText, 0, wx.ALL, 5 )


		bSizer13.Add( fgSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.sendButton.Bind( wx.EVT_BUTTON, self.SendOnButtonClick )
		self.configButton.Bind( wx.EVT_BUTTON, self.ConfigOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SendOnButtonClick( self, event ):
		event.Skip()

	def ConfigOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class UIFrame_Config
###########################################################################

class UIFrame_Config ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		fgSizer5 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer1 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer1.SetMinSize( wx.Size( -1,140 ) )
		self.tokenLabel = wx.StaticText( self, wx.ID_ANY, u"Token", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.tokenLabel.Wrap( -1 )

		fgSizer1.Add( self.tokenLabel, 0, wx.ALL, 5 )

		self.tokenBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.tokenBox.SetMinSize( wx.Size( 160,-1 ) )

		fgSizer1.Add( self.tokenBox, 0, wx.ALL, 5 )

		self.idLabel = wx.StaticText( self, wx.ID_ANY, u"Database ID", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.idLabel.Wrap( -1 )

		fgSizer1.Add( self.idLabel, 0, wx.ALL, 5 )

		self.idBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.idBox.SetMinSize( wx.Size( 160,-1 ) )

		fgSizer1.Add( self.idBox, 0, wx.ALL, 5 )

		self.propertyLabel = wx.StaticText( self, wx.ID_ANY, u"Property Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.propertyLabel.Wrap( -1 )

		fgSizer1.Add( self.propertyLabel, 0, wx.ALL, 5 )

		self.propertyBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.propertyBox.SetMinSize( wx.Size( 160,-1 ) )

		fgSizer1.Add( self.propertyBox, 0, wx.ALL, 5 )

		self.timestampCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Insert timestamp before text", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.timestampCheckBox, 0, wx.ALL, 5 )


		fgSizer5.Add( fgSizer1, 1, wx.EXPAND, 5 )

		m_sdbSizer5 = wx.StdDialogButtonSizer()
		self.m_sdbSizer5Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Save )
		self.m_sdbSizer5Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer5.AddButton( self.m_sdbSizer5Cancel )
		m_sdbSizer5.Realize();

		fgSizer5.Add( m_sdbSizer5, 1, wx.EXPAND, 5 )


		bSizer7.Add( fgSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer5Cancel.Bind( wx.EVT_BUTTON, self.OnCancelButtonClick )
		self.m_sdbSizer5Save.Bind( wx.EVT_BUTTON, self.OnSaveButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnCancelButtonClick( self, event ):
		event.Skip()

	def OnSaveButtonClick( self, event ):
		event.Skip()


