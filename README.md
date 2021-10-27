# NotionDiary
Notionに随時記録をつけることを目的としたソフトウェアです。

Windows版の実行ファイル(NotionDiary.exe)もあります。

# 簡単な使い方
初めに、"Config"を開き、認証情報を入力します。
"Text"ボックスに文章を入力し、"Send"をクリックするとNotionに送信・保存されます。

# 各部の機能
## Title
入力内容が保存されるNotionのページ名を指定します。現在はデフォルトで起動時の日付が入力されるようになっています。
指定したデータベースにその名前のページがない場合は新規作成します。

## Text
保存したいテキストを入力します。複数行の入力も可能です。

## Send
入力内容をNotionに送信します。

## Config
設定を行います。

### Token
NotionのInternal Integration Tokenを入力します。

### Database ID
保存先ページが格納されるデータベースのIDを入力します。

### Property Namw
Database IDで指定したデータベースにおいて、ページ名が表示されるプロパティの名前を入力します。

### Insert timestamp before text
オンにすると入力内容の前に送信した時間が挿入されます。時間はローカルな時間です。

なお、使用にはNotion側でintegrationの作成とデータベースへの設定が必要です。
以下のページのStep1,Step2に従って設定してください。
https://developers.notion.com/docs

# ファイル構成
工事中

# 使用ライブラリ
- WxPython (ライセンス:https://www.wxpython.org/pages/license/)
- Requests (ライセンス: http://www.apache.org/licenses/LICENSE-2.0)

実行ファイルはPyInstallerで作成しています。
