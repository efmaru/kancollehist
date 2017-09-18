# kankollehist
--  
航海日誌(logbook-kai)さんの作るログ(海戦・ドロップ報告書.csv)を参照して海戦履歴をなんちゃって検索するプログラム  
おもに、海域または日付での編成検索、ドロップの検索が行えます。
![メインウィンドウ](http://www.asteria-net.jp/~kancollehist/kancollehist_main.png)
そのうちなんちゃって戦果計算も実装予定。

*まだ正式リリースではないので、ひっそりと公開してます。  *

## プラットフォーム
python(2.6または2.7)とwxpython（2.8または2.9）が動けば大抵のOSで動作するはず。  
今のところ、開発環境がGoogle ドライブ上にログとかプログラムを置いて行っているので、  
Windows(7/8/8.1）とMac（El Capitanまで）の動作確認が取れています。  

## 使い方
### まずはpython環境の準備
・python2.6または2.7をインストールします。  
・wxpython2.9あたりをインストールします。  
・pythonを実行後、import wxとうって、問題なければ使えます。  
```
$ python
Python 2.7.10 (default, Oct 23 2015, 19:19:21) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import wx
>>> wx.__version__
'2.9.5.0'
>>> ^D(python終了）
```
### プログラムファイルの準備。
海戦・ドロップ報告書.csvファイルがあるフォルダに、kancollehist.pyとkancolle_deffs.pyをコピー。  
以下のコマンドで実行開始。  
```
$ python kancollehist.py
```
# 改善中の項目
以下に、バグとまでは言えないのですが、改善中の項目をあげます。  
・CSV項目番号のずれ対処  
　こちらの環境独自の判断基準でlogbookからlogbook-kaiへバージョンアップした時に、  
　項目がずれたのを認識しているので、総項目数とかもっとグローバルな判断基準に変更中。  
・最初に検索できる海域番号  
　起動時、海域番号が1-1から1-6しか無いのです。  
　これを最初から全海域にする予定。  
・海域リストの自動取得。  
　現在、取得できる海域リストはkancolle_deffs.pyに書かれているものしかありません。  
　これをログファイルから取得できる形にする予定。  
　イベント海域は・・・まあ、そうねｗ（いい形を模索中）  


