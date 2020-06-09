# Numer0n-Bot(discord.py)
 
 Numer0n-Botは、discordのpython用のライブラリを使用して、discordのBotとして開発されているプロジェクトです。

# Features
 
Numer0n-Botは、以前民放で放映されていた対戦型のゲームNumer0nをdiscordのサーバー上で遊べるようにしたものです。
ソロモードは完成しており、現在は2人での対戦モードの実装中です。
 
# Requirement
 
詳細は、requirement.txt参照
* python 3.7.6
* discord.py 1.3.3

# Bot Command

```bash
n/help - 使用可能なコマンドの確認
n/rule - Numer0nの簡単なルールを表示（DM）
n/solo - Numer0nのソロモード。10回までにBotが生成した3桁の数字を当てられたらクリア。（アビリティは使用不可）
```
 
# Note
 
お使いのPCでデバッグして実行するためには、新たにBOTのTOKENを記述するための「secret.json」というファイルを追加する必要があります。
secret.jsonの中身は、以下の通りとします。
```bash
{
  "TOKEN": "YOUR_TOKEN_HERE"
}
```
※BOTのTOKENは、Discord公式のDeveloper PortalでBotユーザーを作成することにより発行できます。
 
# Author

* Redbullet2000
* Discord ID : Broccolingual/Red_Bullet #9592
* Mail : broccolingual@gmail.com
 
# License

"Numer0n-bot" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).