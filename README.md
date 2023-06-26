# Table Of Content
- 1. INSTALLATION
    - 1.1 python3
    - 1.2 sqlite
    - 1.3 Flask
    - 1.4 pipenv
- 2. REPOSITORY
---
## 1. Installation
### 1.1 python3
```shell
python3 -V
# Python 3.11.4
# 仮想環境は3.8.7を採用する => 修正:3.11.4採用する、version切り替えめんどくさい；；
```

### 1.2 flask
`flask1.1.2`

### 1.3 sqlite
```shell
# 決めてない,Macならデフォルトで入っているはず, windowsは多分入ってない・・・一旦飛ばすか！
sqlite3 -version
# 3.39.5　バージョンに関してはどっちでもいいと思うけど、、問題あったらまたバージョン変更を行う
```

### 1.4 pipenv
- pipenvとは？
  - https://zenn.dev/nekoallergy/articles/py-env-pipenv01
  - 簡単に言うと・・・ローカル上のtarget directoryを仮想環境に変更する(pythonの環境)

- pipenvのインストール手順および仮想環境の作成(開発は仮想環境で行う)

    ```shell
    # 1.pipenvのインストール
    pip3 install pipenv

    pip3 list
    Package          Version
    ---------------- ---------
    certifi          2023.5.7
    distlib          0.3.6
    filelock         3.12.2
    pip              23.1.2
    pipenv           2023.6.18
    platformdirs     3.8.0
    protobuf         4.21.12
    setuptools       67.6.1
    virtualenv       20.23.1
    virtualenv-clone 0.5.7
    wheel            0.40.0

    # 2.directoryを作成
    mkdir gw_web_chat
    cd gw_web_chat

    # 3.git pull
    git remote add origin https://github.com/Zheng-yuhao/gw_web_chat.git
    git pull origin main

    # 3.1(optional)vscodeでファイルを書くかVimで書くか
    # 先にrepositoryをpullしたので、リポジトリー中にはrequirements.txtというファイルがあるはず、なければ自分で追加
    touch requirements.txt

    # 3.2(optional)requirementsの中身
    Flask==1.1.2

    # 4.仮想環境を生成(必ずgw_web_chat directoryにCD)
    pipenv --python 3.8.7

    # 5.仮想環境にパッケージをインストール
    pipenv install -r requirements.txt

    # 6.仮想環境に入る
    pipenv shell

    # 7.pip3 listでflaskが正常にインストールされたかどうかを確認
    pip3 list
    Package      Version
    ------------ -------
    click        8.1.3
    Flask        1.1.2
    itsdangerous 2.1.2
    Jinja2       3.1.2
    MarkupSafe   2.1.3
    pip          23.1.2
    setuptools   67.8.0
    Werkzeug     2.3.6
    wheel        0.40.0
    
    # 仮想環境から出る
    exit

    # 仮想環境へパッケージ追加
    pipenv install seaborn

    # 仮想環境を消す
    pipenv --rm
    ```
---

- [ ] 2023/06/26開発環境準備

---

## 2. Repository
RPの出し方について　→ [How to submit a pull request](https://qiita.com/siida36/items/880d92559af9bd245c34)

