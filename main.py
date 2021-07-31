

#! env python
# -*- coding: utf-8 -*-

import os
import sys
import wx
from NotionDiaryUIFrame_main_edit import NotionDiaryUIFrame_main_edit

if __name__ == '__main__':
    app = wx.App(False)
    frame = NotionDiaryUIFrame_main_edit(None)
    frame.Show(True)
    app.MainLoop()
