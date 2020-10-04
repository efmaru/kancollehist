# -*- coding: utf-8 -*- 

from kancollehist_gui import *
import codecs
import sys

'''
艦これ、航海日誌ログビューワー
'''

if sys.version.split(".")[0] == "3":
    def unicode(src, transcode):
        '''
        '''

        return src

class KancolleHist(KancolleHistMain):
    '''
    '''

    def __init__( self, parent, debuglevel=0, infile=None ):
        '''
        コンストラクタ
        '''

        KancolleHistMain.__init__(self, parent)

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

        print("exit program")
        self.m_listCtrl1.DeleteAllItems()
        pass

    def KancolleHistMainOnClose( self, event ):

        ending = wx.MessageDialog(self, "End?", "End dialog", wx.YES_NO)

        ret = ending.ShowModal()
        if self._debuglevel >= 1:
            print(ret)
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
            print("%s年%s月のおおよその戦果"%(year, month))
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
        print(shiptype)
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
            print(area)
        term = self.m_comboBoxEvent.GetValue()
        self.ListCtrlChangeByArea(term, area)
        event.Skip()
    
    def m_comboBoxEventOnCombobox( self, event=None ):
        '''
        海域またはイベント選択動作
        '''

        term = self.m_comboBoxEvent.GetValue()
        if self._debuglevel >= 1:
            print(term)
        choise = []
        for item in arealist:
            ss = item.split(':')
            #print ss[0]
            if ss[0] == term:
                #print ss[1]
                choise.append(ss[1])

        if self._debuglevel >= 1:
            print(choise)
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
                        print("%s,"%unicode(aitem, TRANSCODE),)
                    print("")
                self.clearClassNameControls()
                location = unicode(item[7], TRANSCODE)
                if item[7] == "":
                    location = chr(64 + int(item[6]))
                if len(item[5].split(":")) == 2:
                    self.m_staticTextFiledName.SetLabel(unicode(item[5].split(":")[1], TRANSCODE))
                else:
                    self.m_staticTextFiledName.SetLabel(unicode(item[5], TRANSCODE))
                self.m_staticTextMapName.SetLabel(unicode(item[6], TRANSCODE) + ":" + location)
                self.m_staticTextShouHai.SetLabel(unicode(item[8], TRANSCODE))
                if item[16] != "":      # drop艦
                    self.m_staticTextDrop.SetLabel(unicode(item[16] + ':' + item[17], TRANSCODE))
                self.m_staticTextKantai.SetLabel(unicode(item[9], TRANSCODE))
                self.m_staticTextShokusetu.SetLabel(unicode(item[13] + ':' + item[14], TRANSCODE))
                # こちら側
                # 第一艦隊
                self.m_staticTextFFShape.SetLabel(unicode(item[10], TRANSCODE))
                self.m_staticTextClass1.SetLabel(unicode(item[18], TRANSCODE))
                #self.m_staticTextName1.SetLabel(unicode(item[19], TRANSCODE))
                self.m_staticTextClass2.SetLabel(unicode(item[20], TRANSCODE))
                #self.m_staticTextName2.SetLabel(unicode(item[21], TRANSCODE))
                self.m_staticTextClass3.SetLabel(unicode(item[22], TRANSCODE))
                #self.m_staticTextName3.SetLabel(unicode(item[23], TRANSCODE))
                self.m_staticTextClass4.SetLabel(unicode(item[24], TRANSCODE))
                #self.m_staticTextName4.SetLabel(unicode(item[25], TRANSCODE))
                self.m_staticTextClass5.SetLabel(unicode(item[26], TRANSCODE))
                #self.m_staticTextName5.SetLabel(unicode(item[27], TRANSCODE))
                self.m_staticTextClass6.SetLabel(unicode(item[28], TRANSCODE))
                #self.m_staticTextName6.SetLabel(unicode(item[29], TRANSCODE))
                # 第二艦隊
                if item[42] != "":
                    self.m_staticTextName1.SetLabel(unicode(item[30], TRANSCODE))
                    self.m_staticTextName2.SetLabel(unicode(item[32], TRANSCODE))
                    self.m_staticTextName3.SetLabel(unicode(item[34], TRANSCODE))
                    self.m_staticTextName4.SetLabel(unicode(item[36], TRANSCODE))
                    self.m_staticTextName5.SetLabel(unicode(item[38], TRANSCODE))
                    self.m_staticTextName6.SetLabel(unicode(item[40], TRANSCODE))
                # あちら側
                # 第一艦隊
                if item[42] == "":
                    self.m_staticTextClass11.SetLabel(unicode(item[30], TRANSCODE))
                    self.m_staticTextClass21.SetLabel(unicode(item[32], TRANSCODE))
                    self.m_staticTextClass31.SetLabel(unicode(item[34], TRANSCODE))
                    self.m_staticTextClass41.SetLabel(unicode(item[36], TRANSCODE))
                    self.m_staticTextClass51.SetLabel(unicode(item[38], TRANSCODE))
                    self.m_staticTextClass61.SetLabel(unicode(item[40], TRANSCODE))
                else:
                    self.m_staticTextEFShape.SetLabel(unicode(item[11], TRANSCODE))
                    self.m_staticTextClass11.SetLabel(unicode(item[42], TRANSCODE))
                    #self.m_staticTextName11.SetLabel(unicode(item[43], TRANSCODE))
                    self.m_staticTextClass21.SetLabel(unicode(item[44], TRANSCODE))
                    #self.m_staticTextName21.SetLabel(unicode(item[45], TRANSCODE))
                    self.m_staticTextClass31.SetLabel(unicode(item[46], TRANSCODE))
                    #self.m_staticTextName31.SetLabel(unicode(item[47], TRANSCODE))
                    self.m_staticTextClass41.SetLabel(unicode(item[48], TRANSCODE))
                    #self.m_staticTextName41.SetLabel(unicode(item[49], TRANSCODE))
                    self.m_staticTextClass51.SetLabel(unicode(item[50], TRANSCODE))
                    #self.m_staticTextName51.SetLabel(unicode(item[51], TRANSCODE))
                    self.m_staticTextClass61.SetLabel(unicode(item[52], TRANSCODE))
                    #self.m_staticTextName61.SetLabel(unicode(item[53], TRANSCODE))
                # 第二艦隊
                self.m_staticTextName11.SetLabel(unicode(item[54], TRANSCODE))
                self.m_staticTextName21.SetLabel(unicode(item[56], TRANSCODE))
                self.m_staticTextName31.SetLabel(unicode(item[58], TRANSCODE))
                self.m_staticTextName41.SetLabel(unicode(item[60], TRANSCODE))
                self.m_staticTextName51.SetLabel(unicode(item[62], TRANSCODE))
                self.m_staticTextName61.SetLabel(unicode(item[64], TRANSCODE))

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
            print(shiptype, shipname)
        for item in self.hists:
            item[0] = ''
            if unicode(item[16], TRANSCODE) == shiptype:
                if shipname != "":
                    if unicode(item[17], TRANSCODE) != shipname:
                        continue
                #print item[1], item[2], item[3]
                self.m_listCtrl1.InsertStringItem(index, unicode(str(index), TRANSCODE))
                self.m_listCtrl1.SetStringItem(index, 1, item[1] + '/' + item[2] + '/' + item[3] + ' ' + item[4])
                if len(item[5].split(":")) == 2:
                    self.m_listCtrl1.SetStringItem(index, 2, unicode(item[5].split(":")[1], TRANSCODE))
                else:
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
            print(event, area)
        events = event + ":" + area
        for item in self.hists:
            item[0] = ''
            area_num = area_name = ""
            items = item[5].split(":")
            if len(items) == 2:
                area_num = items[0]
                area_name = items[1]
            else:
                area_name = item[5]
            #if unicode(item[5], TRANSCODE) == arealist[events]:
            findarea = False
            if area_num == "":
                if unicode(area_name, TRANSCODE) == arealist[events]:
                    findarea = True
            else:
                if area_num == area:
                    findarea = True
            if findarea is True:
                #print item[1], item[2], item[3]
                #print("arealist[events] = %s[%s](%s)"%(arealist[events], area, item[5]))
                #self.m_listCtrl1.InsertStringItem(index, unicode(str(index), TRANSCODE))
                self.m_listCtrl1.InsertItem(index, unicode(str(index), TRANSCODE))
                #self.m_listCtrl1.SetStringItem(index, 1, item[1] + '/' + item[2] + '/' + item[3] + ' ' + item[4])
                self.m_listCtrl1.SetItem(index, 1, item[1] + '/' + item[2] + '/' + item[3] + ' ' + item[4])
                if len(item[5].split(":")) == 2:
                    #self.m_listCtrl1.SetStringItem(index, 2, unicode(item[5].split(":")[1], TRANSCODE))
                    self.m_listCtrl1.SetItem(index, 2, unicode(item[5].split(":")[1], TRANSCODE))
                else:
                    #self.m_listCtrl1.SetStringItem(index, 2, unicode(item[5], TRANSCODE))
                    self.m_listCtrl1.SetItem(index, 2, unicode(item[5], TRANSCODE))
                #self.m_listCtrl1.SetStringItem(index, 3, unicode(item[6], TRANSCODE))
                #self.m_listCtrl1.SetStringItem(index, 4, unicode(item[7], TRANSCODE))
                self.m_listCtrl1.SetItem(index, 3, unicode(item[6], TRANSCODE))
                self.m_listCtrl1.SetItem(index, 4, unicode(item[7], TRANSCODE))
                if item[16] != "":
                    #self.m_listCtrl1.SetStringItem(index, 5, unicode(item[16] + ':' + item[17], TRANSCODE))
                    self.m_listCtrl1.SetItem(index, 5, unicode(item[16] + ':' + item[17], TRANSCODE))
                item[0] = str(index)
                index += 1

    def ListCtrlChangeByDatetime(self, year, month, day):
        '''
        日付でリストボックス内を変更
        '''

        self.m_listCtrl1.DeleteAllItems()
        index = self.m_listCtrl1.GetItemCount()
        if self._debuglevel >= 1:
            print(year, month, day)
        length = 0
        for item in self.hists:
            if length != len(item):
                length = len(item)
                if self._debuglevel >= 1:
                    print("%s/%s/%s %s - %s"%(item[1], item[2], item[3], item[4], len(item)))
            item[0] = ''
            if item[1] == str(year):
                if item[2] == "%02d"%month:
                    if item[3] == "%02d"%day:
                        #print item[1], item[2], item[3]
                        #self.m_listCtrl1.InsertStringItem(index, unicode(str(index), TRANSCODE))
                        self.m_listCtrl1.InsertItem(index, unicode(str(index), TRANSCODE))
                        #self.m_listCtrl1.SetStringItem(index, 1, item[1] + ':' + item[2] + ':' + item[3] + ' ' + item[4])
                        self.m_listCtrl1.SetItem(index, 1, item[1] + ':' + item[2] + ':' + item[3] + ' ' + item[4])
                        if len(item[5].split(":")) == 2:
                            #self.m_listCtrl1.SetStringItem(index, 2, unicode(item[5].split(":")[1], TRANSCODE))
                            self.m_listCtrl1.SetItem(index, 2, unicode(item[5].split(":")[1], TRANSCODE))
                        else:
                            #self.m_listCtrl1.SetStringItem(index, 2, unicode(item[5], TRANSCODE))
                            self.m_listCtrl1.SetItem(index, 2, unicode(item[5], TRANSCODE))
                        #self.m_listCtrl1.SetStringItem(index, 3, unicode(item[6], TRANSCODE))
                        #self.m_listCtrl1.SetStringItem(index, 4, unicode(item[7], TRANSCODE))
                        self.m_listCtrl1.SetItem(index, 3, unicode(item[6], TRANSCODE))
                        self.m_listCtrl1.SetItem(index, 4, unicode(item[7], TRANSCODE))
                        if item[16] != "":
                            #self.m_listCtrl1.SetStringItem(index, 5, unicode(item[16] + ':' + item[17], TRANSCODE))
                            self.m_listCtrl1.SetItem(index, 5, unicode(item[16] + ':' + item[17], TRANSCODE))
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
                print("set log filename...exit")
                sys.exit(1)
            else:
                filename = self.logfilename
        else:
            if self.logfilename == "":
                self.logfilename = filename

        infile = codecs.open(filename, 'r', 'sjis')
        #lines = infile.read()
        #lines1 = lines.split('\n')
        self.hists = []

        for aline in infile:
            #print "%s : %s"%(count, aline)
            aline = aline.replace('"', '')
            aline = aline.split(',')

            # 日時の分解
            sdate = aline[0].split(' ')
            date = []
            for i in range(70):
                date.append("")

            if len(sdate[0].split('-')) != 1:
                #date.append(sdate[0].split('-')[0])
                #date.append(sdate[0].split('-')[1])
                #date.append(sdate[0].split('-')[2])
                date[1] = sdate[0].split('-')[0]
                date[2] = sdate[0].split('-')[1]
                date[3] = sdate[0].split('-')[2]
            else:
                print(sdate[0])
                continue
            if len(sdate) == 2:
                #date.append(sdate[1])
                date[4] = sdate[1]

            # 各項目の格納
            linesize = len(aline)
            for i in range(1, linesize):
                #date.append(aline[i])
                if i == 1:
                    area_num_and_name = aline[i].split(" ")
                    if len(area_num_and_name) == 2:
                        date[i + 4] = "%s:%s"%(area_num_and_name[0], area_num_and_name[1])
                        continue
                item_place = i + 4
                if linesize == 35:
                    if i > 7:
                        item_place += 3
                try:
                    date[item_place] = (aline[i])
                except:
                    print(date)
                    print(len(date))
                    print(item_place)
                    sys.exit()

            #print date
            self.hists.append(date)
            #sys.stderr.write("%s\n"%str(date))
            #sys.stderr.flush()
            #self.m_listCtrl1.InsertStringItem(index, aline.split(',')[0])
            #self.m_listCtrl1.SetStringItem(index, 1, aline.split(',')[1])
            #self.m_listCtrl1.SetStringItem(index, 2, aline.split(',')[2])
            #self.m_listCtrl1.SetStringItem(index, 3, aline.split(',')[3])

        #print self.hists[1]
        # 最後の日付をリスト表示
        today = datetime.datetime.now()
        #print type(today)
        print(date)
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

# ※海域＝海域番号（e.g. 1-1） 海域名

# 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# X  X0 X1 X2 X3 X4 X5 X6 X7 X8 X9 Y  Y0 Y1 Y2 Y3 Y4 Y5 Y6 Y7 Y8 Y9 Z0

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
    except(getopt.GetoptError, err):
        print(str(err))
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
            print("python kancollehist.py [-l <log file>] [-d <debug level>]")
            sys.exit(1)

    app = wx.App(0)
    #KtSystemContFrame(None,-1,'newdoc.xml - HRC System Control Frame')
    #ce = KancolleHistMain(None, debug, infile)
    ce = KancolleHist(None, debug, infile)
    ce.Show()
    #ce.readHistLog(infile)

    app.MainLoop()

    sys.exit(0)

if __name__ == '__main__':
    main()


