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
    import wx.adv
    cal_object = wx.adv
import sys, os
import datetime
from kancolle_deffs import *

TRANSCODE='cp932'
TITLETEXT = u"艦これ 戦闘ログ閲覧 0.9.2"

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class KancolleHistMain
###########################################################################

class KancolleHistMain ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"艦これ 戦闘ログ閲覧", pos = wx.DefaultPosition, size = wx.Size( 846,598 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
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
        
        self.m_calendar1 = wx.adv.CalendarCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
        bSizer5.Add( self.m_calendar1, 0, wx.ALL, 5 )
        
        fgSizer5 = wx.FlexGridSizer( 6, 2, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_checkBox2 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"1-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox2, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox3 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"4-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox3, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox4 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"1-6", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox4, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox5 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"5-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox5, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox6 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"2-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox6, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox7 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"6-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox7, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_checkBox8 = wx.CheckBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"3-5", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_checkBox8, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_buttonBattleResultCalc = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"戦果計算（選択月）", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_buttonBattleResultCalc, 0, wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer5.Add( fgSizer5, 1, wx.EXPAND, 5 )
        
        
        sbSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText50 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"イベント選択", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText50.Wrap( -1 )
        bSizer8.Add( self.m_staticText50, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        m_comboBoxEventChoices = []
        self.m_comboBoxEvent = wx.ComboBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxEventChoices, 0 )
        bSizer8.Add( self.m_comboBoxEvent, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticText49 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"海域選択", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText49.Wrap( -1 )
        bSizer8.Add( self.m_staticText49, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        m_comboBoxAreaChoices = []
        self.m_comboBoxArea = wx.ComboBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxAreaChoices, 0 )
        bSizer8.Add( self.m_comboBoxArea, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"ドロップ艦むす検索" ), wx.VERTICAL )
        
        self.m_staticText54 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"艦種", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText54.Wrap( -1 )
        sbSizer6.Add( self.m_staticText54, 0, wx.RIGHT, 5 )
        
        m_comboBoxShiptypeChoices = []
        self.m_comboBoxShiptype = wx.ComboBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxShiptypeChoices, 0 )
        sbSizer6.Add( self.m_comboBoxShiptype, 0, wx.BOTTOM|wx.RIGHT, 5 )
        
        self.m_staticText55 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"艦名", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText55.Wrap( -1 )
        sbSizer6.Add( self.m_staticText55, 0, wx.TOP|wx.RIGHT, 5 )
        
        m_comboBoxShipnameChoices = []
        self.m_comboBoxShipname = wx.ComboBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxShipnameChoices, 0 )
        sbSizer6.Add( self.m_comboBoxShipname, 0, wx.RIGHT, 5 )
        
        self.m_buttonGoTypeNameSeach = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"検索...", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer6.Add( self.m_buttonGoTypeNameSeach, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer8.Add( sbSizer6, 1, wx.EXPAND, 5 )
        
        
        sbSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        
        bSizer95.Add( sbSizer4, 0, wx.EXPAND, 5 )
        
        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"履歴" ), wx.VERTICAL )
        
        self.m_listCtrl1 = wx.ListCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,150 ), wx.LC_ALIGN_LEFT|wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
        sbSizer5.Add( self.m_listCtrl1, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText61 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"List select by :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )
        bSizer6.Add( self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_staticSelectStatus = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
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
        
        self.m_staticText7 = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, u"エリア名", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        fgSizer23.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
        
        self.m_staticTextFiledName = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextFiledName.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextFiledName, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
        
        self.m_staticText9 = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, u"マップ名", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        fgSizer23.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticTextMapName = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextMapName.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextMapName, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
        
        self.m_staticText56 = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, u"艦隊行動", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText56.Wrap( -1 )
        fgSizer23.Add( self.m_staticText56, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticTextKantai = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextKantai.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextKantai, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticText410 = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, u"勝敗", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText410.Wrap( -1 )
        fgSizer23.Add( self.m_staticText410, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )
        
        self.m_staticTextShouHai = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextShouHai.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextShouHai, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
        
        self.m_staticText60 = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, u"触接", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText60.Wrap( -1 )
        fgSizer23.Add( self.m_staticText60, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticTextShokusetu = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextShokusetu.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextShokusetu, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
        
        self.m_staticText52 = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, u"ドロップ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText52.Wrap( -1 )
        fgSizer23.Add( self.m_staticText52, 0, wx.RIGHT|wx.ALIGN_RIGHT, 5 )
        
        self.m_staticTextDrop = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextDrop.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextDrop, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText73 = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, u"戦果", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText73.Wrap( -1 )
        fgSizer23.Add( self.m_staticText73, 0, wx.RIGHT|wx.ALIGN_RIGHT, 5 )
        
        self.m_staticTextResult = wx.StaticText( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_staticTextResult.Wrap( -1 )
        fgSizer23.Add( self.m_staticTextResult, 0, wx.LEFT, 5 )
        
        
        sbSizer44.Add( fgSizer23, 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( sbSizer44, 1, wx.EXPAND, 5 )
        
        sbSizer42 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"こちら側" ), wx.VERTICAL )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText69 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"陣形", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText69.Wrap( -1 )
        bSizer7.Add( self.m_staticText69, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticTextFFShape = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.m_staticTextFFShape.Wrap( -1 )
        bSizer7.Add( self.m_staticTextFFShape, 0, wx.RIGHT|wx.LEFT, 5 )
        
        
        sbSizer42.Add( bSizer7, 0, wx.EXPAND, 5 )
        
        fgSizer2 = wx.FlexGridSizer( 8, 3, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText75 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText75.Wrap( -1 )
        fgSizer2.Add( self.m_staticText75, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticText31 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"第一艦隊", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText31.Wrap( -1 )
        fgSizer2.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText32 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"第二艦隊", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText32.Wrap( -1 )
        fgSizer2.Add( self.m_staticText32, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticText11 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"旗艦 ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        fgSizer2.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticTextClass1 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass1.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName1 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName1.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText14 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        fgSizer2.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass2 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass2.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName2 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName2.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText17 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        fgSizer2.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass3 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass3.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName3 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName3.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText20 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        fgSizer2.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass4 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass4.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass4, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName4 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName4.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName4, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText23 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )
        fgSizer2.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass5 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass5.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass5, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName5 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName5.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName5, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText26 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )
        fgSizer2.Add( self.m_staticText26, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass6 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass6.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass6, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName6 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName6.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextName6, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText63 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText63.Wrap( -1 )
        fgSizer2.Add( self.m_staticText63, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass7 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass7.Wrap( -1 )
        fgSizer2.Add( self.m_staticTextClass7, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticName7 = wx.StaticText( sbSizer42.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticName7.Wrap( -1 )
        fgSizer2.Add( self.m_staticName7, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer42.Add( fgSizer2, 1, wx.EXPAND, 5 )
        
        
        fgSizer3.Add( sbSizer42, 1, wx.EXPAND, 5 )
        
        sbSizer43 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, u"あちら側" ), wx.VERTICAL )
        
        bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText691 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"陣形", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText691.Wrap( -1 )
        bSizer71.Add( self.m_staticText691, 0, wx.RIGHT|wx.LEFT, 5 )
        
        self.m_staticTextEFShape = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.m_staticTextEFShape.Wrap( -1 )
        bSizer71.Add( self.m_staticTextEFShape, 0, wx.RIGHT|wx.LEFT, 5 )
        
        
        sbSizer43.Add( bSizer71, 0, wx.EXPAND, 5 )
        
        fgSizer21 = wx.FlexGridSizer( 8, 3, 0, 0 )
        fgSizer21.SetFlexibleDirection( wx.BOTH )
        fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText301 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText301.Wrap( -1 )
        fgSizer21.Add( self.m_staticText301, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText311 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"第一艦隊", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText311.Wrap( -1 )
        fgSizer21.Add( self.m_staticText311, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText321 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"第二艦隊", wx.DefaultPosition, wx.Size( 150,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText321.Wrap( -1 )
        fgSizer21.Add( self.m_staticText321, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticText111 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"旗艦 ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )
        fgSizer21.Add( self.m_staticText111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticTextClass11 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass11.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass11, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName11 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName11.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName11, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText141 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText141.Wrap( -1 )
        fgSizer21.Add( self.m_staticText141, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass21 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass21.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass21, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName21 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName21.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName21, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText171 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText171.Wrap( -1 )
        fgSizer21.Add( self.m_staticText171, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass31 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass31.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass31, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName31 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName31.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName31, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText201 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText201.Wrap( -1 )
        fgSizer21.Add( self.m_staticText201, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass41 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass41.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName41 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName41.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText231 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText231.Wrap( -1 )
        fgSizer21.Add( self.m_staticText231, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass51 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass51.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass51, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName51 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName51.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName51, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText261 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText261.Wrap( -1 )
        fgSizer21.Add( self.m_staticText261, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass61 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass61.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass61, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName61 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName61.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName61, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText66 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText66.Wrap( -1 )
        fgSizer21.Add( self.m_staticText66, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextClass71 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextClass71.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextClass71, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticTextName71 = wx.StaticText( sbSizer43.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextName71.Wrap( -1 )
        fgSizer21.Add( self.m_staticTextName71, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
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
        
        # Connect Events
        self.m_buttonReloadLog.Bind( wx.EVT_BUTTON, self.m_buttonReloadLogOnButtonClick )
        self.m_calendar1.Bind( wx.adv.EVT_CALENDAR, self.m_calendar1OnCalendar )
        self.m_calendar1.Bind( wx.adv.EVT_CALENDAR_DAY, self.m_calendar1OnCalendarDay )
        self.m_calendar1.Bind( wx.adv.EVT_CALENDAR_MONTH, self.m_calendar1OnCalendarMonth )
        self.m_calendar1.Bind( wx.adv.EVT_CALENDAR_SEL_CHANGED, self.m_calendar1OnCalendarSelChanged )
        self.m_calendar1.Bind( wx.adv.EVT_CALENDAR_YEAR, self.m_calendar1OnCalendarYear )
        self.m_buttonBattleResultCalc.Bind( wx.EVT_BUTTON, self.m_buttonBattleResultCalcOnButtonClick )
        self.m_comboBoxEvent.Bind( wx.EVT_COMBOBOX, self.m_comboBoxEventOnCombobox )
        self.m_comboBoxArea.Bind( wx.EVT_COMBOBOX, self.m_comboBoxAreaOnCombobox )
        self.m_comboBoxShiptype.Bind( wx.EVT_COMBOBOX, self.m_comboBoxShiptypeOnCombobox )
        self.m_comboBoxShipname.Bind( wx.EVT_COMBOBOX, self.m_comboBoxShipnameOnCombobox )
        self.m_buttonGoTypeNameSeach.Bind( wx.EVT_BUTTON, self.m_buttonGoTypeNameSeachOnButtonClick )
        self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.m_listCtrl1OnListItemSelected )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def m_buttonReloadLogOnButtonClick( self, event ):
        event.Skip()
    
    def m_calendar1OnCalendar( self, event ):
        event.Skip()
    
    def m_calendar1OnCalendarDay( self, event ):
        event.Skip()
    
    def m_calendar1OnCalendarMonth( self, event ):
        event.Skip()
    
    def m_calendar1OnCalendarSelChanged( self, event ):
        event.Skip()
    
    def m_calendar1OnCalendarYear( self, event ):
        event.Skip()
    
    def m_buttonBattleResultCalcOnButtonClick( self, event ):
        event.Skip()
    
    def m_comboBoxEventOnCombobox( self, event ):
        event.Skip()
    
    def m_comboBoxAreaOnCombobox( self, event ):
        event.Skip()
    
    def m_comboBoxShiptypeOnCombobox( self, event ):
        event.Skip()
    
    def m_comboBoxShipnameOnCombobox( self, event ):
        event.Skip()
    
    def m_buttonGoTypeNameSeachOnButtonClick( self, event ):
        event.Skip()
    
    def m_listCtrl1OnListItemSelected( self, event ):
        event.Skip()
    
    def m_splitter1OnIdle( self, event ):
        self.m_splitter1.SetSashPosition( 0 )
        self.m_splitter1.Unbind( wx.EVT_IDLE )
    

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 482,275 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    


