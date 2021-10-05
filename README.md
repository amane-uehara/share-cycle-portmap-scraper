# シェアサイクルのポートマップの取得スクリプト

ポートマップの一覧を、Google MapからJSON形式で取得するためのPythonスクリプト。

対応地域は下表を参照。

|地名    |サービス              | ポートマップの Google Map URL                                                |
|:-------|:---------------------|:-----------------------------------------------------------------------------|
| 仙台   | DATE BIKE            | <https://www.google.com/maps/d/viewer?mid=1ShMz32NqMaa6LipSCvAz4Xn3F_s>      |
| 奥日光 | サイクルシェア       | <https://www.google.com/maps/d/viewer?mid=1fUip9lp8PSk64THAQ79i8jWzfpM>      |
| 東京   | 広域ポートマップ     | <https://www.google.com/maps/d/viewer?mid=1L2l1EnQJhCNlm_Xxkp9RTjIj68Q>      |
| 川崎   | バイクシェア         | <https://www.google.com/maps/d/viewer?mid=1uAKaGq8dcNdvSIoQ7-33ZzIxQduFoAYi> |
| 横浜   | コミュニティサイクル | <https://www.google.com/maps/d/viewer?mid=1jhQA9-EMSTN0TH6javoFWbR18tM>      |
| 名古屋 | カリテコバイク       | <https://www.google.com/maps/d/viewer?mid=1HcdtxBimRiIbo1g2evC4e0SoTD6psbSD> |
| 大阪   | HUBchari             | <https://www.google.com/maps/d/viewer?mid=1x3udX-cLHZvwupRLqle1g447iek>      |
| 大阪   | バイクシェア         | <https://www.google.com/maps/d/viewer?mid=1m-q1JvpxPyniClnJSoDrwW7OtQVEtxil> |
| 奈良   | バイクシェア         | <https://www.google.com/maps/d/viewer?mid=1r5s5HllrLVSiOPZQiCqa8p23huBmqQUE> |
| 広島市 | ぴーすくる           | <https://www.google.com/maps/d/viewer?mid=1oeVRN3d9Du9TNXzVVHLgZKy3PCI>      |
| 沖縄   | ちゅらチャリ         | <https://www.google.com/maps/d/viewer?mid=1E1dgLVa8uDZvt5PnqT6ZcaorBik>      |

## How to use

以下のコマンドにより、東京のポートマップが標準出力に表示される。

```sh
$ sh fetch_raw_json.sh "https://www.google.com/maps/d/viewer?mid=1L2l1EnQJhCNlm_Xxkp9RTjIj68Q" > tmp.json
$ python3 parse.py tmp.json
```

`fetch_raw_json.sh`の第一引数にはポートマップのURLを入力する。

結果

```sh
[
  {
    "state": "",
    "symbol": "A1-01",
    "name_jp": "ああああああ",
    "name_en": "Aaaaaaa Bbbb Cccccc",
    "explain": "いいいいいいい0-0-0",
    "latitude": 35.1234567,
    "longitude": 139.1234567
  },
  {
    "state": "",
    "symbol": "A1-02",
    "name_jp": "ううう",
    "name_en": "Ddddddd",
    "explain": "ええええええ0-0-0",
    "latitude": 35.7654321,
    "longitude": 139.7654321
  },
  ... (略) ...
```

## 補遺

名古屋のポートマップのスクレイピングについては、`parse.py`ではなく`parse_nagoya.py`を使用する。

```sh
$ sh fetch_raw_json.sh "https://www.google.com/maps/d/viewer?mid=1HcdtxBimRiIbo1g2evC4e0SoTD6psbSD" > tmp.json
$ python3 parse_nagoya.py tmp.json
```

## LICENSE

MIT
