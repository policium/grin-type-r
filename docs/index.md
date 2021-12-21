# GRIN Type-R 組み立て手順

## はじめに

この度はGRIN Type-Rのご購入ありがとうございます。このキットははんだ付けとファームウェアの書き込み作業が必要です。以下の手順に従って組み立ててください。

## 注意事項

本製品はCherry MXスイッチおよび互換品に対応しています。キーキャップは19mmピッチ18mm角を想定しておりますが、互換性の保証はいたしかねます。  

## 見出し

１．事前準備  
２．キット内容の確認  
３．初期動作確認  
４．ダイオードのはんだ付け  
５．スイッチ用PCBソケットのはんだ付け  
６．スタビライザーの取り付け  
７．スイッチプレートと基板のねじ止め  
８．スイッチの取り付け  
９．トッププレートと基板の取り付け  
１０．ボトムプレートに足を取り付け  
１１．ボトムプレートの取り付け  
１２．キーキャップの取り付け  
１３．動作確認  
１４．３Ｄプリントケース  
Ａ１．付録  

## １．事前準備

### 配列を決める
GRIN Type-RはANSI・ISO・JIS配列と単体スペースバー・分割スペースバーの組み合わせを選べます。それぞれ必要なスイッチの数と必要なキーキャップが変わるため事前に決定する必要があります。

![layout](https://user-images.githubusercontent.com/3132296/146913502-217302a7-877f-430a-b0cc-7842f74d1557.png)

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
- スタビライザー(PCBマウント) … ※選択した配列に合わせる  
[遊舎工房](https://shop.yushakobo.jp/products/a0500st?variant=37665699430561)  
[TALP KEYBOARD](https://talpkeyboard.net/?category_id=5f884b9b3313d216eb50558a)  
- 3Uスタビライザー用ワイヤー … ※選択した配列に合わせる  
分割ではないスペースバーを利用する場合に必要です。ワイヤーのサイズが一般的ではないため自作するか遊舎工房で別途購入してください。  
[遊舎工房](https://shop.yushakobo.jp/products/a0500st?variant=40429698678945)
- USB Type-C ケーブル(データ通信可能なもの) … 1本  
- Micro USB ケーブル(データ通信可能なもの) … 1本  
Picoの動作確認用

### 工具を準備する
- はんだごて（電子基板用）
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

## ２．キット内容の確認
以下が揃っていることをご確認ください。
不足がある場合は、Boothショップサイトのトップページ上部にある、メールアイコンよりメッセージを下さい。
- 袋➀  
    - 基板(PCB) … 1枚  
    - トッププレート(FR-4) … 1枚  
    - スイッチプレート(アルミまたはFR-4) … 1枚  
    - ボトムプレート(FR-4) … 1枚  
- 袋➁  
    - ダイオード(1N4148) … 75個
- 袋➂  
    - M2ネジ(銀) … 6個
    - スペーサー短(丸型両メネジ) … 3個  
- 袋➃  
    - M2ネジ(黒) … 16個  
    - スペーサー長(丸型両メネジ) … 8個  
    - スペーサー太(丸型中空) … 8個  
- 袋➄  
    - プラワッシャー … 8個  
    - ゴムワッシャー … 24個  
- 袋➅  
    - アルミ足 … 2個
    - M4ネジ … 2個
    - ゴム足 … 2個

## ３．初期動作確認

袋➀から基板を取り出します。
出荷状態の基板はPRK FirmwareのANSI版が書き込み済みになっています。先ず正常動作することを確認します。  

### PCに接続し認識されることを確認する

USBケーブルで基板とPCを接続します。「PRKFirmware」というドライブが認識されることを確認します。  

### ピンセット等で端子を短絡させ入力されることを確認する

![IMG_20211024_184022__01](https://user-images.githubusercontent.com/3132296/138600349-d7a1206c-a3c7-4663-90a5-6ad1bfbf6f9c.jpg)  
ピンセット等の導体で写真の2点を短絡して「1」が入力されることを確認してください。入力されない場合は、Boothショップサイトのトップページ上部にある、メールアイコンよりメッセージを下さい。

※出荷状態ではキー配列がANSIになっています。  

## ４．ダイオードのはんだ付け

袋➁のダイオードを基板に取り付けていきます。  

注意！  
キー配列およびスイッチの取り付け方法によってダイオードの取り付けが不要な位置があります。  
不要な位置にダイオードを取り付けるとスタビライザーと干渉する可能性があるため取り付けないで下さい。  
必要なダイオードはレイアウト画像の赤字を参照してください。

注意！  
一部他と向きの違うダイオードがあります。シルクをよく見て間違えないように実装してください。  

ダイオードの足を曲げます。  
![IMG_20211024_185426__01](https://user-images.githubusercontent.com/3132296/138599397-515d71bd-303b-48e0-98fb-fd6c56f75fc6.jpg)

シルクの向きとダイオードの向きを合わせてセットします。  
![IMG_20211024_185451__01](https://user-images.githubusercontent.com/3132296/138599443-0b524bb9-5166-402d-975e-d0db50a08e34.jpg)

ダイオードをマスキングテープで固定します。  
![IMG_20211024_185700__01](https://user-images.githubusercontent.com/3132296/138599491-e0bae086-d260-48b1-b428-10e3a5f24a5f.jpg)

裏返してはんだ付けします。  
![IMG_20211024_185829__01](https://user-images.githubusercontent.com/3132296/138599533-31aaaf06-3e98-4a53-ac3d-a49286c5c794.jpg)

足をニッパーで切断し、フラックスクリーナーで周囲を奇麗にします。  
![IMG_20211024_190343__01](https://user-images.githubusercontent.com/3132296/138599571-aa82a8cc-f0f4-4994-95de-8e2329e0151e.jpg)

## ５．スイッチ用PCBソケットのはんだ付け

※注意 スイッチを直付けする場合、この項の手順は飛ばして下さい。

ソケットを配置してはんだ付けします。浮かないようにピンセットで押さえながらはんだ付けして下さい。  
![IMG_20211024_191023__01](https://user-images.githubusercontent.com/3132296/138601716-b302675a-c47f-4df0-85e3-4094c506b9ff.jpg)

※向きに注意　下の写真の向きは間違いです。  
![IMG_20211024_190934__01](https://user-images.githubusercontent.com/3132296/138602574-db98be8a-e68b-4710-9918-185e2c19d15a.jpg)

## ６．スタビライザーの取り付け

2U以上のサイズのバックスペース、シフトキー、エンターキーおよびISOエンターのために2Uスタビライザーを取り付けます。  
![IMG_20211024_201044__01](https://user-images.githubusercontent.com/3132296/138602682-9a904d91-1ccc-49bf-b053-58f890d8d942.jpg)

3Uスペースバーには3Uワイヤーのスタビライザーを取り付けます。  

## ７．スイッチプレートと基板のねじ止め

袋➂のネジとスペーサーで基板とスイッチプレートを3か所ねじ止めします。  
![IMG_20211025_012308](https://user-images.githubusercontent.com/3132296/138603250-d2de6202-2906-4cfb-a936-b46ea861370a.jpg)

![IMG_20211024_202016__01](https://user-images.githubusercontent.com/3132296/138603264-aa535f03-cefc-45b1-8bed-a865e45260f8.jpg)

## ８．スイッチの取り付け

ソケットの場合は、スイッチの端子を曲げないように気を付けてスイッチを刺して下さい。  
直付けの場合は、裏からはんだ付けして下さい。その際、スイッチが浮かないように気を付けて下さい。  
![IMG_20211024_204917__01](https://user-images.githubusercontent.com/3132296/138603407-edfcd077-62f7-4b1f-a821-9fadd0bea6f5.jpg)

## ９．トッププレートと基板の取り付け

袋➃のネジとスペーサー長をトッププレートに8か所取り付けます。  
![IMG_20211024_211905__01](https://user-images.githubusercontent.com/3132296/138603512-0a3e8f68-802c-4a07-bf53-0dec95cf8f33.jpg)

袋➄のプラワッシャーを1枚ずつスペーサーに刺します。次に袋➄のゴムワッシャを1枚ずつスペーサーに刺します。  
注意！  
硬いのがプラワッシャー、柔らかいのがゴムワッシャーです。  
![IMG_20211024_211924__01](https://user-images.githubusercontent.com/3132296/138603569-339cebf9-9d9b-4629-9fc4-827d561a5353.jpg)

基板とねじ止めしたスイッチプレートをスペーサーに刺します。  
![IMG_20211024_212044__01](https://user-images.githubusercontent.com/3132296/138603678-1e5cce81-fcb9-41f5-9264-fee6a1c8ebae.jpg)

袋➄のゴムワッシャを"2"枚ずつスペーサーに刺します。次に袋➃のスペーサー太を刺します。  
![IMG_20211024_212158__01](https://user-images.githubusercontent.com/3132296/138603821-a8e88bc6-4702-40da-89e2-c6be5727c03e.jpg)  
スペーサーの面がつらいちにならない場合、スペーサーの枚数や浮きを確認して下さい。  

## １０．ボトムプレートに足を取り付け

袋➅のアルミ足とゴム足をボトムプレートに取り付けます。  
アルミ足はM4ネジでボトムプレートに取り付けます。
赤丸はゴム足の貼り付け位置です。  
![feet layout](https://user-images.githubusercontent.com/3132296/146915719-ce421d2b-c62c-4877-b785-19031218be0e.jpg)

## １１．ボトムプレートの取り付け

袋➃のネジで本体とボトムプレートを8か所ねじ止めします。

## １２．キーキャップの取り付け

スイッチにキーキャップを取り付けます。

## １３．動作確認

USBケーブルでPCと接続し動作確認します。必要であればソースコードを修正しキー配列を修正します。  
[サンプル](https://github.com/policium/grin-type-r/tree/main/firmware)を参考に修正してください。

## １４．３Ｄプリントケース

BOOTHにログインした状態で購入履歴より該当の注文詳細にアクセスし、3Dデータをダウンロードしてください。  
[JLCPCB](https://jlcpcb.com/)か[WENEXT](https://www.wenext.com/)か[DMM.make](https://make.dmm.com/print/)で印刷できます。HP MJF PA12 Nylon を推奨します。 
もちろんご自宅の３Ｄプリンタで印刷することもできます。  

注意！  
こちらの3Dデータはサポート対象外とさせていただきます。改変を含め自由にご利用いただいて構いませんが、派生データも含め再頒布はご遠慮ください。  

トッププレート側から被せスナップフィット（ツメ）をひっかけます。
外れにくいように2mmの結束バンドでケースと柱をつなぎます。  

![case snap](https://user-images.githubusercontent.com/3132296/146917573-4bb67aa8-68a3-4ec0-9f66-ae6a32ada06e.jpg)

塗装して楽しむこともできます！  

![case](https://user-images.githubusercontent.com/3132296/146917817-20f95171-bd59-45ae-a27f-70b97efd56f8.jpg)

## Ａ１．付録

トラブルシュートおよびファームウェアの改造にお役立て下さい。  

### KMK FirmwareのUSBストレージの無効化 　

boot.pyを以下の内容に書き換えてください。USBを挿抜して再接続するとUSBストレージが認識されなくなります。  
注意! 不用意に修正するとREPLから復旧するか、ファームウェアを再インストールする必要があります。  

boot.py
```
import storage
import supervisor

storage.disable_usb_drive()
supervisor.set_next_stack_limit(4096 + 4096)
```

### USBストレージの再有効化 　

[MU Editorダウンロード](https://codewith.mu/en/download)  
インストールしてください。  

GRIN Type-RをPCに接続します。  
Mu Editorを起動します。  
ツールバーからシリアルボタンをクリックします。  
![mu1](https://user-images.githubusercontent.com/3132296/139570715-863a8d0e-bd0e-4078-bd58-74653904e181.png)

REPLペインをクリックし「Ctrl+C」を押下します。  
![mu2](https://user-images.githubusercontent.com/3132296/139570725-34043950-0abd-4ff3-8fd7-a7b0392efc4c.png)

「Enter」を押下します。  
![mu3](https://user-images.githubusercontent.com/3132296/139570730-8251d9de-786d-4ed5-adbd-70f82e0f3e97.png)

以下のコードを直接コピー＆ペーストします。（手入力ではなく）  
```
import os
import storage
storage.remount('/', readonly=False)
os.remove('boot.py')
```

![mu4](https://user-images.githubusercontent.com/3132296/139570737-318f5c8b-f691-4309-be04-386b7738ed17.png)

GRIN Type-RのUSBを挿抜して再接続するとUSBドライブとして認識するようになります。  
ドライブからboot.pyが消えているため以下のコードでboot.pyを作成します。  

boot.py
```
import supervisor

supervisor.set_next_stack_limit(4096 + 4096)
```

### 回路図  
![schematic](https://user-images.githubusercontent.com/3132296/139060252-92dcc313-b126-41d9-8f86-858f542e6534.jpg)

### Circuit Pythonで問題が発生した時のヒント  
https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting

