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
n/rule, n/rules- Numer0nの簡単なルールを表示（DM）
n/solo - Numer0nのソロモード。10回までにBotが生成した3桁の数字を当てられたらクリア。（アビリティは使用不可）
n/create, n/make - 対戦モードのゲームを作成
n/join, n/enter - 対戦モードの参加者を登録（入力した本人が登録）
n/leave, n/remove - 対戦モードの参加者を削除（入力した本人を削除）
n/player, n/players - 対戦モードの参加者を表示※ゲームを作成している必要あり。
n/start - 対戦モードのゲームを開始（ゲームを作成した上で参加者を2人登録している必要あり）
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

# Directory Structure

```bash
├main.py #メイン
├cogs
│  ├utils
│  │  ├__init__.py
│  │  ├game.py #ゲームクラスとゲームに関する関数の定義
│  │  ├player.py #プレイヤークラス
│  │  ├abillity.py #ゲームで使用するアビリティに関する関数の定義
│  │  ├views_rule.py #ルールで表示するEmbedのテンプレート
│  │  ├views_solomode.py #ソロモードで表示するEmbedのテンプレート
│  │  └views_battlemode.py #バトルモードで表示するEmbedのテンプレート
│  ├__init__.py
│  ├solomode.py #ソロモードのコマンド
│  ├battlemode.py #バトルモードのコマンド
│  └rules.py #ルールのコマンド
├secret.json #上記(Note)の通り自分で作成する必要あり。
├Procfile
├requirement.txt
├runtime.txt
└README.md
```
 
# Author

* Redbullet2000
* Discord ID : Broccolingual/Red_Bullet #9592
* Mail : broccolingual@gmail.com
 
# License

"Numer0n-bot" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).