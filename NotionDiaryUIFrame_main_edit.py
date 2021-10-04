"""Subclass of UIFrame1, which is generated by wxFormBuilder."""

import wx
import ui
from NotionDiaryUIFrame_main import NotionDiaryUIFrame_main
from NotionDiaryUIFrame_Config_edit import NotionDiaryUIFrame_Config_edit
import datetime
import core

today = datetime.date.today()
# Implementing UIFrame1


class NotionDiaryUIFrame_main_edit(NotionDiaryUIFrame_main):
	def __init__(self, parent):
		NotionDiaryUIFrame_main.__init__(self, parent)
		self.titleBox.SetValue(today.isoformat())

	# Handlers for UIFrame1 events.
	def SendOnButtonClick(self, event):
		# TODO: Implement SendOnButtonClick
		sending = self.sendingText.SetLabel("Sending……")
		txt = self.bodyBox.GetValue()
		title = self.titleBox.GetValue()
		core.send(title, txt)
		sending = self.sendingText.SetLabel("Sending…… Complete")

	def ConfigOnButtonClick(self, event):
		# TODO: Implement ConfigOnButtonClick
		app = wx.App(False)
		frame = NotionDiaryUIFrame_Config_edit(None)
		frame.Show(True)
		app.MainLoop()
