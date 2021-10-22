# GRIN Type-R 組み立て手順

## １．はじめに

この度はGRIN Type-Rのご購入ありがとうございます。このキットははんだ付けとファームウェアの書き込みが必要です。以下の手順に従って組み立ててください。

## ２．注意事項

本製品はCherry MXスイッチおよび互換品に対応しています。キーキャップは19mmピッチ18mm角を想定しておりますが、キーキャップの互換性は保証いたしかねます。
TBD：互換確認済キーキャップ一覧

## ３．事前準備

### 配列を決める
GRIN Type-RはANSI・ISO・JIS配列と３Uスペースバー・分割スペースバーの組み合わせを選べます。それぞれ必要なスイッチの数と必要なキーキャップが変わるため事前に決定する必要があります。

TODO：配列と必要キー数の表を作成

### キット以外に必要な部品を準備する
- キーキャップ(Cherry MX互換) … 選択した配列に合わせる  
[遊舎工房](https://shop.yushakobo.jp/collections/keycaps)  
[TALP KEYBOARD](https://talpkeyboard.net/?category_id=59be183f428f2d49120007b1)  
- キースイッチ(Cherry MX 互換) … ※選択した配列に合わせる  
[遊舎工房](https://shop.yushakobo.jp/collections/all-switches)  
[TALP KEYBOARD](https://talpkeyboard.net/?category_id=59cf8860ed05e668db003f5d)  
- Cherry MX スイッチ用PCBソケット … ※選択した配列に合わせる  
キースイッチを直付けする場合は不要  
[遊舎工房](https://shop.yushakobo.jp/products/a01ps)  
[TALP KEYBOARD](https://talpkeyboard.net/items/5e02c5405b120c792616bcf9)  
- スタビライザー … ※選択した配列に合わせる  
[遊舎工房](https://shop.yushakobo.jp/products/a0500st?variant=37665699430561)
[TALP KEYBOARD](https://talpkeyboard.net/?category_id=5f884b9b3313d216eb50558a)  
- 3Uスタビライザー用ワイヤー … ※選択した配列に合わせる  
分割ではないスペースバーを利用する場合に必要です。ワイヤーのサイズが一般的ではないため自作するか遊舎工房で別途購入してください。  
[遊舎工房](https://shop.yushakobo.jp/products/a0500st?variant=40429698678945)
- USB Type-C ケーブル(データ通信可能なもの) … 1本  
- Micro USB ケーブル(データ通信可能なもの) … 1本  
Picoの動作確認用

### 工具を準備する
- はんだごて
- はんだ
- フラックス
- フラックスクリーナー（IPA等のアルコールや溶剤でも代用可能）
- ピンセット
- ニッパー
- プラスドライバー(No.0)
- ティッシュ

### 他にあるといい物
- シリコン作業マット
- ウエス、キムワイプ、綿棒
- マスキングテープ
- はんだ吸い取り線、はんだ吸い取り器
- テスター(トラブル時の原因調査用)

## ４．キット内容の確認
- 基板(PCB) … 1枚  
- トッププレート(FR-4) … 1枚  
- スイッチプレート(アルミ) … 1枚  
- ボトムプレート(FR-4) … 1枚  
- ダイオード(1N4148) … 75個
- M2ネジ … 16個  
- スペーサー(丸型両メネジ) … 8個  
- スペーサー(丸型中空) … 8個  
- ゴムワッシャー … 32個  
- アルミ足 … 2個
- バンポン … 2個

### 拡張キット
- 3D プリントシェル  
Coming soon...

## ５．CircuitPythonのインストール
[公式サイト](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)に従ってCircuitPythonをRaspberry Pi Picoにインストールします。  
以下にWindows10での簡単な流れを記載します。

### UF2ファイルのダウンロード
https://circuitpython.org/board/raspberry_pi_pico/ からUF2ファイルをダウンロードします。CircuitPython 7.0.0のJAPANESEで確認済みです。  

### UF2ブートローダーを起動
Raspberry Pi PicoのBOOTSELボタンを押しながらUSBをPCと接続します。初回時はBOOTSELボタンを押さなくてもUF2ブートローダーが立ち上がるようです  
UF2ブートローダーの起動に成功するとPRI-RP2というドライブがマウントされます。

### UF2ファイルの書き込み
先ほどダウンロードしたUF2ファイルをPRI-RP2ドライブのルートにコピーします。コピー後はRaspberry Pi Picoが自動で再起動します。  
CircuitPythonのインストールに成功していると、CIRCUITPYというドライブがマウントされます。

## ６．標準ファームウェア（KMK Firmware）の書き込みと動作確認

## ７．Raspberry Pi Pico のはんだ付け

## ８．ダイオードのはんだ付け

## ９．Cherry MX スイッチ用PCBソケットのはんだ付け

## １０．スタビライザーの取り付け

## １１．スイッチの取り付け

## １２．動作確認

## １３．トッププレートとボトムプレートの取り付け

## １４．キーキャップの取り付け

## １５．3D プリントシェルの取り付け
Coming soon...
