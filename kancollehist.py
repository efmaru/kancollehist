# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov 27 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
try:
    import wx.calendar
    cal_object = wx.calendar
except:
    import wx.lib.calendar
    cal_object = wx.lib.calendar
import sys, os
import datetime
from kancolle_deffs import *

TRANSCODE='cp932'
TITLETEXT = u"艦これ 戦闘ログ閲覧 0.9.1"

###########################################################################
## Class KancolleHistMain
###########################################################################

class KancolleHistMain ( wx.Frame ):
    
    def __init__( self, parent, debuglevel=0, infile=None ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = TITLETEXT, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer94 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,-1 ), wx.TAB_TRAVERSAL )
        bSizer95 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticStatus = wx.StaticText( self.m_panel1, wx.ID_ANY, u"全：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticStatus.Wrap( -1 )
        bSizer4.Add( self.m_staticStatus, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText58 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_staticText58.Wrap( -1 )
        bSizer4.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_buttonReloadLog = wx.Button( self.m_panel1, wx.ID_ANY, u"ログ再読込", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_buttonReloadLog, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        m_comboBoxLogFileChoices = [ u"海戦・ドロップ報告書", u"海戦・ドロップ報告書2015" ]
        self.m_comboBoxLogFile = wx.ComboBox( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), m_comboBoxLogFileChoices, 0 )
        self.m_comboBoxLogFile.SetSelection( 0 )
        bSizer4.Add( self.m_comboBoxLogFile, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer95.Add( bSizer4, 0, wx.EXPAND, 5 )
        
        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"日付指定" ), wx.HORIZONTAL )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_calendar1 = wx.calendar.CalendarCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.calendar.CAL_SHOW_HOLIDAYS )
        bSizer5.Add( self.m_calendar1, 0, wx.ALL, 5 )
        
        fgSizer5 = wx.FlexGridSizer( 6, 2, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_checkBox2 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"1-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox2, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox3 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"4-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox3, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox4 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"1-6", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox4, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox5 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"5-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox5, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox6 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"2-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox6, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox7 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"6-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox7, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox8 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"3-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox8, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_buttonBattleResultCalc = wx.Button( self.m_panel1, wx.ID_ANY, u"戦果計算（選択月）", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_buttonBattleResultCalc, 0, wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer5.Add( fgSizer5, 1, wx.EXPAND, 5 )
        
        
        sbSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText49 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"海域選択", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText49.Wrap( -1 )
        bSizer8.Add( self.m_staticText49, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        m_comboBoxAreaChoices = []
        self.m_comboBoxArea = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxAreaChoices, 0 )
        bSizer8.Add( self.m_comboBoxArea, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticText50 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"イベント選択", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText50.Wrap( -1 )
        bSizer8.Add( self.m_staticText50, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        m_comboBoxEventChoices = []
        self.m_comboBoxEvent = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxEventChoices, 0 )
        bSizer8.Add( self.m_comboBoxEvent, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"ドロップ艦むす検索" ), wx.VERTICAL )
        
        self.m_staticText54 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"艦種", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText54.Wrap( -1 )
        sbSizer6.Add( self.m_staticText54, 0, wx.RIGHT, 5 )
        
        m_comboBoxShiptypeChoices = []
        self.m_comboBoxShiptype = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxShiptypeChoices, 0 )
        sbSizer6.Add( self.m_comboBoxShiptype, 0, wx.BOTTOM|wx.RIGHT, 5 )
        
        self.m_staticText55 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"艦名", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText55.Wrap( -1 )
        sbSizer6.Add( self.m_staticText55, 0, wx.TOP|wx.RIGHT, 5 )
        
        m_comboBoxShipnameChoices = []
        self.m_comboBoxShipname = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxShipnameChoices, 0 )
        sbSizer6.Add( self.m_comboBoxShipname, 0, wx.RIGHT, 5 )
        
        self.m_buttonGoTypeNameSeach = wx.Button( self.m_panel1, wx.ID_ANY, u"検索...", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer6.Add( self.m_buttonGoTypeNameSeach, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer8.Add( sbSizer6, 1, wx.EXPAND, 5 )
        
        
        sbSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        
        bSizer95.Add( sbSizer4, 0, wx.EXPAND, 5 )
        
        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"履歴" ), wx.VERTICAL )
        
        self.m_listCtrl1 = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,150 ), wx.LC_ALIGN_LEFT|wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
        sbSizer5.Add( self.m_listCtrl1, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText61 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"List select by :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )
        bSizer6.Add( self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_staticSelectStatus = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticSelectStatus.Wrap( -1 )
        bSizer6.Add( self.m_staticSelectStatus, 0, wx.ALL, 5 )
        
        
        sbSizer5.Add( bSizer6, 0, 0, 5 )
        
        
        bSizer95.Add( sbSizer5, 1, wx.EXPAND, 5 )
        
        
        self.m_panel1.SetSizer( bSizer95 )
        self.m_panel1.Layout()
        bSizer94.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
        
        self.m_panel7 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer3 = wx.FlexGridSizer( 3, 1, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        sbSizer44 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"戦績他情報" ), wx.VERTICAL )
        
        fgSizer23 = wx.FlexGridSizer( 7, 2, 0, 0 )
        fgSizer23.SetFlexibleDirection( wx.BOTH )
        fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText7 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"エリア名", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        fgSizer23.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 5 )
        
        self.m_staticTextFiledName = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextFiledName.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextFiledName, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
        
        self.m_staticText9 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"マップ名", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        fgSizer23.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.m_staticTextMapName = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextMapName.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextMapName, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
        
        self.m_staticText56 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"艦隊行動", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText56.Wrap( -1 )
        fgSizer23.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextKantai = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextKantai.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextKantai, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText410 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"勝敗", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText410.Wrap( -1 )
        fgSizer23.Add( self.m_staticText410, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
        
        self.m_staticTextShouHai = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextShouHai.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextShouHai, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
        
        self.m_staticText60 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"触接", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText60.Wrap( -1 )
        fgSizer23.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_staticTextShokusetu = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextShokusetu.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextShokusetu, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
        
        self.m_staticText52 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"ドロップ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText52.Wrap( -1 )
        fgSizer23.Add( self.m_staticText52, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
        
        self.m_staticTextDrop = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextDrop.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextDrop, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer44.Add( fgSizer23, 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( sbSizer44, 1, wx.EXPAND, 5 )
        
        sbSizer42 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"こちら側" ), wx.VERTICAL )
        
        fgSizer2 = wx.FlexGridSizer( 7, 3, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText30 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )
        fgSizer2.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText31 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"艦名", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText31.Wrap( -1 )
        fgSizer2.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText32 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"HP", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText32.Wrap( -1 )
        fgSizer2.Add( self.m_staticText32, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticText11 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"旗艦 ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        fgSizer2.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticTextClass1 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass1.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName1 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName1.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText14 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        fgSizer2.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass2 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass2.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName2 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName2.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText17 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        fgSizer2.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass3 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass3.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName3 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName3.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText20 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        fgSizer2.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass4 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass4.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName4 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName4.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText23 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )
        fgSizer2.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass5 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass5.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName5 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName5.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText26 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )
        fgSizer2.Add( self.m_staticText26, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass6 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass6.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName6 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName6.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer42.Add( fgSizer2, 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( sbSizer42, 1, wx.EXPAND, 5 )
        
        sbSizer43 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"あちら側" ), wx.VERTICAL )
        
        fgSizer21 = wx.FlexGridSizer( 7, 3, 0, 0 )
        fgSizer21.SetFlexibleDirection( wx.BOTH )
        fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText301 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText301.Wrap( -1 )
        fgSizer21.Add( self.m_staticText301, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText311 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"艦名", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText311.Wrap( -1 )
        fgSizer21.Add( self.m_staticText311, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText321 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"HP", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText321.Wrap( -1 )
        fgSizer21.Add( self.m_staticText321, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticText111 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"旗艦 ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )
        fgSizer21.Add( self.m_staticText111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticTextClass11 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass11.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName11 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName11.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText141 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText141.Wrap( -1 )
        fgSizer21.Add( self.m_staticText141, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass21 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass21.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName21 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName21.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText171 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText171.Wrap( -1 )
        fgSizer21.Add( self.m_staticText171, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass31 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass31.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName31 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName31.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText201 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText201.Wrap( -1 )
        fgSizer21.Add( self.m_staticText201, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass41 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass41.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass41, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName41 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName41.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName41, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText231 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText231.Wrap( -1 )
        fgSizer21.Add( self.m_staticText231, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass51 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass51.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass51, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName51 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName51.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName51, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText261 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText261.Wrap( -1 )
        fgSizer21.Add( self.m_staticText261, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass61 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass61.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass61, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName61 = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName61.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName61, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer43.Add( fgSizer21, 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( sbSizer43, 1, wx.EXPAND, 5 )
        
        
        self.m_panel7.SetSizer( fgSizer3 )
        self.m_panel7.Layout()
        fgSizer3.Fit( self.m_panel7 )
        self.m_splitter1.Initialize( self.m_panel7 )
        bSizer94.Add( self.m_splitter1, 0, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer94 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        self.Show()

        # Connect Events
        self.m_buttonReloadLog.Bind( wx.EVT_BUTTON, self.m_buttonReloadLogOnButtonClick )
        self.m_calendar1.Bind( wx.calendar.EVT_CALENDAR, self.m_calendar1OnCalendar )
        self.m_calendar1.Bind( wx.calendar.EVT_CALENDAR_DAY, self.m_calendar1OnCalendarDay )
        self.m_calendar1.Bind( wx.calendar.EVT_CALENDAR_MONTH, self.m_calendar1OnCalendarMonth )
        self.m_calendar1.Bind( wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.m_calendar1OnCalendarSelChanged )
        self.m_calendar1.Bind( wx.calendar.EVT_CALENDAR_YEAR, self.m_calendar1OnCalendarYear )
        self.m_comboBoxArea.Bind( wx.EVT_COMBOBOX, self.m_comboBoxAreaOnCombobox )
        self.m_comboBoxEvent.Bind( wx.EVT_COMBOBOX, self.m_comboBoxEventOnCombobox )
        self.m_comboBoxShiptype.Bind( wx.EVT_COMBOBOX, self.m_comboBoxShiptypeOnCombobox )
        self.m_comboBoxShipname.Bind( wx.EVT_COMBOBOX, self.m_comboBoxShipnameOnCombobox )
        self.m_buttonGoTypeNameSeach.Bind( wx.EVT_BUTTON, self.m_buttonGoTypeNameSeachOnButtonClick )
        self.m_buttonBattleResultCalc.Bind( wx.EVT_BUTTON, self.m_buttonBattleResultCalcOnButtonClick )
        self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.m_listCtrl1OnListItemSelected )
        self.Bind( wx.EVT_CLOSE, self.KancolleHistMainOnClose )

        self._debuglevel = debuglevel
        self.logfilename = ""

        # タイトル設定
        title = [[u"No", wx.LIST_FORMAT_CENTER, 40],
                 [u"年月", wx.LIST_FORMAT_CENTER, 150],
                 [u"海域", wx.LIST_FORMAT_LEFT, 100],
                 [u"マス", wx.LIST_FORMAT_LEFT, 35],
                 [u"ボス", wx.LIST_FORMAT_LEFT, 35],
                 [u"ドロップ", wx.LIST_FORMAT_LEFT, 100]]

        cindex = 0
        for column in title:
            self.m_listCtrl1.InsertColumn(cindex, column[0], column[1], column[2])
            cindex += 1

        if infile is not None:
            self.readHistLog(infile)

        # 海域選択肢追加
        normal_areas = (u'1-1',
                 u'1-2',
                 u'1-3',
                 u'1-4',
                 u'1-5',
                 u'1-6')
        self.m_comboBoxArea.SetItems(normal_areas)

        # イベント選択追加
        #events = (u'通常',
        #          u'14秋',
        #          u'15冬',
        #          u'15春',
        #          u'15夏',
        #          u'15秋',
        #          u'16冬',
        #          u'16春',
        #          u'16夏',
        #          u'16秋',
        #          u'17冬')
        areas = sorted(arealist.keys())
        events = []
        area = ""
        for item in areas:
            if area == item.split(":")[0]:
                continue
            area = item.split(":")[0]
            events.append(area)
            
        self.m_comboBoxEvent.SetItems(events)
        self.m_comboBoxEvent.SetSelection(0)
        self.m_comboBoxEventOnCombobox()

    def __del__( self ):
        '''
        '''

        print "exit program"
        self.m_listCtrl1.DeleteAllItems()
        pass

    def KancolleHistMainOnClose( self, event ):

        ending = wx.MessageDialog(self, "End?", "End dialog", wx.YES_NO)

        ret = ending.ShowModal()
        if self._debuglevel >= 1:
            print ret
        if ret == wx.ID_NO:
            return
        event.Skip()

    def m_buttonBattleResultCalcOnButtonClick( self, event ):
        '''
        戦果計算開始ボタン
        '''

        date = self.m_calendar1.GetDate()               # 対象月を取得
        #self.ListCtrlChangeByDatetime(date.GetYear(), date.GetMonth() + 1, date.GetDay())

        year = "%s"%date.GetYear()
        month = "%d"%(date.GetMonth() + 1)
        if self._debuglevel >= 1:
            print "%s年%s月のおおよその戦果"%(year, month)
        for item in self.hists:
            if item[1] == date.GetYear():
                if item[2] == date.GetMonth():
                    pass

        event.Skip()

    def m_buttonReloadLogOnButtonClick( self, event ):
        '''
        リロード
        '''

        histfile = self.m_comboBoxLogFile.GetValue() + '.csv'
        self.readHistLog(histfile)
        event.Skip()

    def m_comboBoxShiptypeOnCombobox( self, event=None ):
        '''
        検索ボックス、ドロップ艦、艦種選択
        '''

        shiptype = self.m_comboBoxShiptype.GetValue()
        print shiptype
        shipnames = []
        for item in self.shiptype_names:
            #print item
            items = item.split(':')
            #print items[0]
            if items[0] == shiptype:
                shipnames.append(items[1])

        #print shipnames
        if len(shipnames) != 0:
            self.m_comboBoxShipname.SetItems(shipnames)
            self.m_comboBoxShipname.SetSelection(0)

        if event is not None:
            event.Skip()
    
    def m_comboBoxShipnameOnCombobox( self, event ):
        '''
        検索ボックス、ドロップ艦、艦名選択
        '''
        event.Skip()

    def m_buttonGoTypeNameSeachOnButtonClick( self, event ):
        '''
        ドロップ艦種、艦むすで中身で検索
        '''

        shiptype = self.m_comboBoxShiptype.GetValue()
        shipname = self.m_comboBoxShipname.GetValue()

        if shiptype == None:
            return
        if shipname == None:
            shipname = ""

        self.ListCtrlChangeByDropShip(shiptype, shipname)
        self.m_staticSelectStatus.SetLabel("Select by ship type and ship name")
        event.Skip()
    
    def m_comboBoxAreaOnCombobox( self, event ):
        '''
        個別エリア選択動作
        '''

        area = self.m_comboBoxArea.GetValue()
        if self._debuglevel >= 1:
            print area
        term = self.m_comboBoxEvent.GetValue()
        self.ListCtrlChangeByArea(term, area)
        event.Skip()
    
    def m_comboBoxEventOnCombobox( self, event=None ):
        '''
        海域またはイベント選択動作
        '''

        term = self.m_comboBoxEvent.GetValue()
        if self._debuglevel >= 1:
            print term
        choise = []
        for item in arealist:
            ss = item.split(':')
            #print ss[0]
            if ss[0] == term:
                #print ss[1]
                choise.append(ss[1])

        if self._debuglevel >= 1:
            print choise
        if len(choise) == 0:
            return
        self.m_comboBoxArea.Clear()
        self.m_comboBoxArea.SetItems(sorted(choise))
        self.m_comboBoxArea.SetSelection(0)

        self.ListCtrlChangeByArea(term, choise[0])
        self.m_staticSelectStatus.SetLabel("Select by area")

        if event is not None:
            event.Skip()

    def clearClassNameControls(self):
        '''
        艦種艦名表示テキストコントロール(s)の内容をクリアする
        '''

        self.m_staticTextDrop.SetLabel("")
        # こちら側
        self.m_staticTextClass1.SetLabel("")
        self.m_staticTextName1.SetLabel("")
        self.m_staticTextClass2.SetLabel("")
        self.m_staticTextName2.SetLabel("")
        self.m_staticTextClass3.SetLabel("")
        self.m_staticTextName3.SetLabel("")
        self.m_staticTextClass4.SetLabel("")
        self.m_staticTextName4.SetLabel("")
        self.m_staticTextClass5.SetLabel("")
        self.m_staticTextName5.SetLabel("")
        self.m_staticTextClass6.SetLabel("")
        self.m_staticTextName6.SetLabel("")
        # あちら側
        self.m_staticTextClass11.SetLabel("")
        self.m_staticTextName11.SetLabel("")
        self.m_staticTextClass21.SetLabel("")
        self.m_staticTextName21.SetLabel("")
        self.m_staticTextClass31.SetLabel("")
        self.m_staticTextName31.SetLabel("")
        self.m_staticTextClass41.SetLabel("")
        self.m_staticTextName41.SetLabel("")
        self.m_staticTextClass51.SetLabel("")
        self.m_staticTextName51.SetLabel("")
        self.m_staticTextClass61.SetLabel("")
        self.m_staticTextName61.SetLabel("")

    def m_listCtrl1OnListItemSelected( self, event ):
        '''
        リストボックスで選択したら
        '''

        index = self.m_listCtrl1.GetFirstSelected()
        #print "selected %d in list"%index
        for item in self.hists:
            if item[0] == str(index):
                if self._debuglevel > 1:
                    for aitem in item:
                        print "%s,"%unicode(aitem, TRANSCODE),
                    print ""
                self.clearClassNameControls()
                location = unicode(item[7], TRANSCODE)
                if item[7] == "":
                    location = chr(64 + int(item[6]))
                self.m_staticTextFiledName.SetLabel(unicode(item[5], TRANSCODE))
                self.m_staticTextMapName.SetLabel(unicode(item[6], TRANSCODE) + ":" + location)
                self.m_staticTextShouHai.SetLabel(unicode(item[8], TRANSCODE))
                if item[16] != "":      # drop艦
                    self.m_staticTextDrop.SetLabel(unicode(item[16] + ':' + item[17], TRANSCODE))
                self.m_staticTextKantai.SetLabel(unicode(item[9], TRANSCODE))
                self.m_staticTextShokusetu.SetLabel(unicode(item[13] + ':' + item[14], TRANSCODE))
                # こちら側
                self.m_staticTextClass1.SetLabel(unicode(item[18], TRANSCODE))
                self.m_staticTextName1.SetLabel(unicode(item[19], TRANSCODE))
                self.m_staticTextClass2.SetLabel(unicode(item[20], TRANSCODE))
                self.m_staticTextName2.SetLabel(unicode(item[21], TRANSCODE))
                self.m_staticTextClass3.SetLabel(unicode(item[22], TRANSCODE))
                self.m_staticTextName3.SetLabel(unicode(item[23], TRANSCODE))
                self.m_staticTextClass4.SetLabel(unicode(item[24], TRANSCODE))
                self.m_staticTextName4.SetLabel(unicode(item[25], TRANSCODE))
                self.m_staticTextClass5.SetLabel(unicode(item[26], TRANSCODE))
                self.m_staticTextName5.SetLabel(unicode(item[27], TRANSCODE))
                self.m_staticTextClass6.SetLabel(unicode(item[28], TRANSCODE))
                self.m_staticTextName6.SetLabel(unicode(item[29], TRANSCODE))
                # あちら側
                self.m_staticTextClass11.SetLabel(unicode(item[30], TRANSCODE))
                self.m_staticTextName11.SetLabel(unicode(item[31], TRANSCODE))
                self.m_staticTextClass21.SetLabel(unicode(item[32], TRANSCODE))
                self.m_staticTextName21.SetLabel(unicode(item[33], TRANSCODE))
                self.m_staticTextClass31.SetLabel(unicode(item[34], TRANSCODE))
                self.m_staticTextName31.SetLabel(unicode(item[35], TRANSCODE))
                self.m_staticTextClass41.SetLabel(unicode(item[36], TRANSCODE))
                self.m_staticTextName41.SetLabel(unicode(item[37], TRANSCODE))
                self.m_staticTextClass51.SetLabel(unicode(item[38], TRANSCODE))
                self.m_staticTextName51.SetLabel(unicode(item[39], TRANSCODE))
                self.m_staticTextClass61.SetLabel(unicode(item[40], TRANSCODE))
                self.m_staticTextName61.SetLabel(unicode(item[41], TRANSCODE))

        event.Skip()

    def m_calendar1OnCalendar( self, event ):
        '''
        カレンダーで日付をダブルクリックした
        '''

        #print "double click on calendar"
        event.Skip()
    
    def m_calendar1OnCalendarDay( self, event ):
        '''
        カレンダーで日付選択を変更した
        '''

        #print "date selection change to another day"
        event.Skip()
    
    def m_calendar1OnCalendarMonth( self, event ):
        '''
        カレンダーで月の選択を変更した
        '''

        #print "month change selection"
        event.Skip()
    
    def m_calendar1OnCalendarSelChanged( self, event ):
        '''
        カレンダーで日付選択を変更した
        '''
        #print "date selection changed"
        #2016年11月04日Friday 00:00:00
        date = self.m_calendar1.GetDate()
        #print type(date)
        self.ListCtrlChangeByDatetime(date.GetYear(), date.GetMonth() + 1, date.GetDay())
        self.m_staticSelectStatus.SetLabel("Select by calendar")
        event.Skip()
    
    def m_calendar1OnCalendarYear( self, event ):
        '''
        カレンダーで年の選択を変更した
        '''
        event.Skip()


    def m_splitter1OnIdle( self, event ):
        self.m_splitter1.SetSashPosition( 0 )
        self.m_splitter1.Unbind( wx.EVT_IDLE )

    def ListCtrlChangeByDropShip(self, shiptype, shipname):
        '''
        海域(またはイベント)でリストボックス内を変更
        '''

        self.m_listCtrl1.DeleteAllItems()
        index = self.m_listCtrl1.GetItemCount()
        if self._debuglevel >= 1:
            print shiptype, shipname
        for item in self.hists:
            item[0] = ''
            if unicode(item[16], TRANSCODE) == shiptype:
                if shipname != "":
                    if unicode(item[17], TRANSCODE) != shipname:
                        continue
                #print item[1], item[2], item[3]
                self.m_listCtrl1.InsertStringItem(index, unicode(str(index), TRANSCODE))
                self.m_listCtrl1.SetStringItem(index, 1, item[1] + ':' + item[2] + ':' + item[3] + ' ' + item[4])
                self.m_listCtrl1.SetStringItem(index, 2, unicode(item[5], TRANSCODE))
                self.m_listCtrl1.SetStringItem(index, 3, unicode(item[6], TRANSCODE))
                self.m_listCtrl1.SetStringItem(index, 4, unicode(item[7], TRANSCODE))
                if item[16] != "":              # drop
                    self.m_listCtrl1.SetStringItem(index, 5, unicode(item[16] + ':' + item[17], TRANSCODE))
                item[0] = str(index)
                index += 1

    def ListCtrlChangeByArea(self, event, area):
        '''
        海域(またはイベント)でリストボックス内を変更
        '''

        self.m_listCtrl1.DeleteAllItems()
        index = self.m_listCtrl1.GetItemCount()
        if self._debuglevel >= 1:
            print event, area
        events = event + ":" + area
        for item in self.hists:
            item[0] = ''
            if unicode(item[5], TRANSCODE) == arealist[events]:
                #print item[1], item[2], item[3]
                self.m_listCtrl1.InsertStringItem(index, unicode(str(index), TRANSCODE))
                self.m_listCtrl1.SetStringItem(index, 1, item[1] + ':' + item[2] + ':' + item[3] + ' ' + item[4])
                self.m_listCtrl1.SetStringItem(index, 2, unicode(item[5], TRANSCODE))
                self.m_listCtrl1.SetStringItem(index, 3, unicode(item[6], TRANSCODE))
                self.m_listCtrl1.SetStringItem(index, 4, unicode(item[7], TRANSCODE))
                if item[16] != "":
                    self.m_listCtrl1.SetStringItem(index, 5, unicode(item[16] + ':' + item[17], TRANSCODE))
                item[0] = str(index)
                index += 1

    def ListCtrlChangeByDatetime(self, year, month, day):
        '''
        日付でリストボックス内を変更
        '''

        self.m_listCtrl1.DeleteAllItems()
        index = self.m_listCtrl1.GetItemCount()
        if self._debuglevel >= 1:
            print year, month, day
        length = 0
        for item in self.hists:
            if length != len(item):
                length = len(item)
                if self._debuglevel >= 1:
                    print "%s/%s/%s %s - %s"%(item[1], item[2], item[3], item[4], len(item))
            item[0] = ''
            if item[1] == str(year):
                if item[2] == "%02d"%month:
                    if item[3] == "%02d"%day:
                        #print item[1], item[2], item[3]
                        self.m_listCtrl1.InsertStringItem(index, unicode(str(index), TRANSCODE))
                        self.m_listCtrl1.SetStringItem(index, 1, item[1] + ':' + item[2] + ':' + item[3] + ' ' + item[4])
                        self.m_listCtrl1.SetStringItem(index, 2, unicode(item[5], TRANSCODE))
                        self.m_listCtrl1.SetStringItem(index, 3, unicode(item[6], TRANSCODE))
                        self.m_listCtrl1.SetStringItem(index, 4, unicode(item[7], TRANSCODE))
                        if item[16] != "":
                            self.m_listCtrl1.SetStringItem(index, 5, unicode(item[16] + ':' + item[17], TRANSCODE))
                        item[0] = str(index)
                        index += 1
    def refreshShipTypeAndName(self):
        '''
        艦種設定
        #shiptypes = (u'戦艦',
        #             u'工作艦',
        #             u'揚陸艦',
        #             u'潜水艦',
        #             u'軽空母',
        #             u'駆逐艦',
        #             u'正規空母',
        #             u'潜水母艦',
        #             u'軽巡洋艦',
        #             u'重巡洋艦')
        '''

        shiptype = ""
        shipname = ""
        self.shiptype_names = []
        for item in self.hists:
            if item[16] != "":
                asnew = True
                for shipname in self.shiptype_names:
                    if unicode(item[17], TRANSCODE) == shipname.split(":")[1]:
                        asnew = False
                        continue

                if asnew is True:
                    self.shiptype_names.append("%s:%s"%(unicode(item[16], TRANSCODE), unicode(item[17], TRANSCODE)))
                    #print("%s:%s"%(unicode(item[16], TRANSCODE), unicode(item[17], TRANSCODE)))
        shiptypes = []
        for item in self.shiptype_names:
            asnew = True
            for shiptype in shiptypes:
                if shiptype == item.split(":")[0]:
                    asnew = False
                    continue

            if asnew is True:
                shiptypes.append(item.split(":")[0])

        self.m_comboBoxShiptype.SetItems(shiptypes)
        self.m_comboBoxShiptype.SetSelection(0)
        self.m_comboBoxShiptypeOnCombobox()
    def readHistLog(self, filename=""):
        '''
        '''

        if filename == "":
            if self.logfilename == "":
                print "set log filename...exit"
                sys.exit(1)
            else:
                filename = self.logfilename
        else:
            if self.logfilename == "":
                self.logfilename = filename

        infile = open(filename, 'r')
        #lines = infile.read()
        #lines1 = lines.split('\n')
        self.hists = []

        for aline in infile:
            #print "%s : %s"%(count, aline)
            aline = aline.split(',')

            # 日時の分解
            sdate = aline[0].split(' ')
            date = []
            for i in range(42):
                date.append("")

            if len(sdate[0].split('-')) != 1:
                #date.append(sdate[0].split('-')[0])
                #date.append(sdate[0].split('-')[1])
                #date.append(sdate[0].split('-')[2])
                date[1] = sdate[0].split('-')[0]
                date[2] = sdate[0].split('-')[1]
                date[3] = sdate[0].split('-')[2]
            else:
                continue
            if len(sdate) == 2:
                #date.append(sdate[1])
                date[4] = sdate[1]

            # 各項目の格納
            linesize = len(aline)
            for i in range(1, linesize):
                #date.append(aline[i])
                item_place = i + 4
                if linesize == 35:
                    if i > 7:
                        item_place += 3
                try:
                    date[item_place] = (aline[i])
                except:
                    print date
                    print len(date)
                    print item_place
                    sys.exit()

            #print date
            self.hists.append(date)
            #self.m_listCtrl1.InsertStringItem(index, aline.split(',')[0])
            #self.m_listCtrl1.SetStringItem(index, 1, aline.split(',')[1])
            #self.m_listCtrl1.SetStringItem(index, 2, aline.split(',')[2])
            #self.m_listCtrl1.SetStringItem(index, 3, aline.split(',')[3])

        #print self.hists[1]
        # 最後の日付をリスト表示
        today = datetime.datetime.now()
        #print type(today)
        self.ListCtrlChangeByDatetime(today.year, int(today.month), int(today.day))

        self.refreshShipTypeAndName()
    
def main():
# ---- 解析前のログ
# -- 旧バージョン(35カラム)
#0    1    2    3    4      5        6        7       8        9         10
#日付,海域,マス,ボス,ランク,艦隊行動,味方陣形,敵陣形,敵艦隊,ドロップ艦種,ドロップ艦娘
# 11      12        13      14        15      16        17      18        19      20        21      22    
#,味方艦1,味方艦1HP,味方艦2,味方艦2HP,味方艦3,味方艦3HP,味方艦4,味方艦4HP,味方艦5,味方艦5HP,味方艦6,味方艦6HP
# 23    24      25    26      27    28      29    30      31    32      33    34
# 敵艦1,敵艦1HP,敵艦2,敵艦2HP,敵艦3,敵艦3HP,敵艦4,敵艦4HP,敵艦5,敵艦5HP,敵艦6,敵艦6HP
#
# -- 新バージョン(38カラム)
#0    1    2    3    4      5        6        7      8      9        10     11     12           13             14            15         16 17 18-
#日付,海域,マス,ボス,ランク,艦隊行動,味方陣形,敵陣形,制空権,味方触接,適触接,敵艦隊,ドロップ艦種,ドロップ艦むす,伊401改(Lv89),24/24,

# ---- 解析後のログ(日付＞2017,1,1,12,15)
# -- 旧バージョン
#     5    6    7    8      9        10       11     12     13           14
#日付,海域,マス,ボス,ランク,艦隊行動,味方陣形,敵陣形,敵艦隊,ドロップ艦種,ドロップ艦娘
# 15      16        17      18        19      20        21      22        23      24        25      26    
#,味方艦1,味方艦1HP,味方艦2,味方艦2HP,味方艦3,味方艦3HP,味方艦4,味方艦4HP,味方艦5,味方艦5HP,味方艦6,味方艦6HP
# 27    28      29    30      31    32      33    34      35    37      38    39
# 敵艦1,敵艦1HP,敵艦2,敵艦2HP,敵艦3,敵艦3HP,敵艦4,敵艦4HP,敵艦5,敵艦5HP,敵艦6,敵艦6HP
#
# -- 新バージョン(2016/12/04 16:26:02以降)
#     5    6    7    8      9       10        11     12     13       14     15     16           17             18-
#日付,海域,マス,ボス,ランク,艦隊行動,味方陣形,敵陣形,制空権,味方触接,敵触接,敵艦隊,ドロップ艦種,ドロップ艦むす,伊401改(Lv89),24/24,
    import sys
    import getopt

    #print len(sys.argv)
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "l:d:", ["help"])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(1)

    debug = 0
    infile = u"海戦・ドロップ報告書.csv"

    for opt, arg in optlist:
        if opt == '-d':
            num = int(arg)
            if 0 < num and num < 5:
                debug = num
        elif opt == '-l':
            infile = arg
        else:
            print "python kancollehist.py [-l <log file>] [-d <debug level>]"
            sys.exit(1)

    app = wx.App(0)
    #KtSystemContFrame(None,-1,'newdoc.xml - HRC System Control Frame')
    ce = KancolleHistMain(None, debug, infile)
    #ce.readHistLog(infile)

    app.MainLoop()

if __name__ == '__main__':
    main()


