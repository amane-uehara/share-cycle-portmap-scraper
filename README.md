# シェアサイクルのポートマップをJSONで取得するスクリプト

ポートマップの一覧を、Google MapからJSON形式で取得するためのスクリプト

### How to use

以下のコマンドにより、東京のポートマップが標準出力に表示される。

```sh
$ sh fetch_raw_json.sh "https://www.google.com/maps/d/viewer?mid=1L2l1EnQJhCNlm_Xxkp9RTjIj68Q" > tmp.json
$ python3 tokyo-osaka.py tmp.json
```

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

### 他地域のポートマップの取得方法

大阪のポートマップの取得方法

```sh
$ sh fetch_raw_json.sh "https://www.google.com/maps/d/viewer?mid=1x3udX-cLHZvwupRLqle1g447iek" > tmp.json
$ python3 tokyo-osaka.py tmp.json
```

名古屋のポートマップの取得方法

```sh
$ sh fetch_raw_json.sh "https://www.google.com/maps/d/viewer?mid=1HcdtxBimRiIbo1g2evC4e0SoTD6psbSD" > tmp.json
$ python3 nagoya.py tmp.json
```
