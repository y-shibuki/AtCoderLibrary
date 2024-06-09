# AtCoder で快適にコーディングを行うためのライブラリ

## 初期設定

atcoder のユーザー名とパスワードを登録

```bash
oj login -u ユーザー名 -p パスワード "https://atcoder.jp/"
oj login --check "https://atcoder.jp/"
```

### 設定ファイルの場所

```bash
/Users/{home}/Library/Preferences/atcoder-cli-nodejs
```

### コマンド

- 新しい問題・テストファイルのインストール

```bash
acc new "id"
```

### ショートカットキー

- atcoder に提出する

```bash
Command + Control + S
```

- コードをテストする

```bash
Command + Control + T
```

## AtCoder のコツ

### 無限大（INF）について

PyPyでは`2^64`を超えると、動作が遅くなる（らしい）。なので無限大(INF)は`2^60`程度、つまり`1<<60`程度をおくとTLEになりにくい。
[参考リンク](https://hirohirohirohiros.hatenablog.com/entry/2022/02/13/170000)

### キューについて

スタックキューはqueue.Queueよりもcollections.dequeの方が圧倒的に速い。
[参考リンク](https://pop-ketle.hatenablog.com/entry/2020/02/13/140652)