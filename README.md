# Table Of Content
1. INSTALLATION
    - 1.1 python3
    - 1.2 sqlite
    - 1.3 Flask
    - 1.4 pipenv
2. REPOSITORY
    - 2.1 真似するrepository
    - 2.2 開発repositoryのdirectory tree
3. Summary of preliminary tasks
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
    git init

    # 3.git pull
    git remote add origin https://github.com/Zheng-yuhao/gw_web_chat.git
    git pull origin main

    # 3.1(optional)vscodeでファイルを書くかVimで書くか
    # 先にrepositoryをpullしたので、リポジトリー中にはrequirements.txtというファイルがあるはず、なければ自分で追加
    touch requirements.txt

    # 3.2(optional)requirementsの中身
    Flask==1.1.2

    # 4.仮想環境を生成(必ずgw_web_chat directoryにCD)
    pipenv --python 3.11.4

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

### 2.1 真似するrepository
https://github.com/TAKANARI1985/flaskchat/tree/main

> **注意事項**  
> **Procfile, requirements.txtをコピペする必要はない** 

### 2.2 開発repositoryのdirectory tree
```shell
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
├── static
│   └── css
└── templates
├── .gitignore

4 directories, 4 files
```

- `Pipfile`, `Pipfile.lock`は`.gitignore`に入ってる => gitにプッシュせん
- `20230626`現時点、`static/css`と`template` direcotryに何も入ってないのでローカルから`push`してもあげられない！
  - 各自feature branchを作成して`mkdir`コマンドで上のdirectory構造を作成してください！
  - feature branchの名前は割り当てられた機能で決める

## 3. Summary of preliminary tasks
- [Remote repository](https://github.com/Zheng-yuhao/gw_web_chat)から`pull`する
- `pipenv`で仮想環境を作る
- 仮想化環境で`Flask`が正常にインストールされている
- ローカル環境でdirectory treeを真似する/作成する
- 開発ツール
  - vscode
    - markdown extension install![Alt text](markdown_extension_image.png)  
    インストール後このREADME.mdファイルを開き、![Alt text](button_image.png)  の右の点点点から左の2個目を押してpreview modeでこのREADMEファイルを見ることができます。

---
last edit:2023/06/26 by: @Zheng-yuhao  
*補足：トークンはMacOsのキーチェンのデータベースに含まれている。`command` + `space`でキーチェンを検索してからgithubを検索してください・・・出てくるはずです！絶対ファイルとかに記録しないでください、記録しようとしてもせめて単独のdirectoryの下に置いてください！*

---

2023/06/27:  
- [ ] :各々の担当部分を決める
- [ ] :ブランチの命名規則の決定
- [ ] :必要があればコードの解説

---

# 4. 流星向け研修
- `Python3`
  - `Python3`がインストールされている状態なら`pip`も入っているはず。
- `pip`で`pipenv`ライブラリーのインストール
- `git`のツールに関して [git for windows](https://prog-8.com/docs/git-env-win)
- `git`の操作以外`power shell`を使ってください


# 5. 担当部分の決定

- 流星


- 玲雄


- 涼


- 俺

# 6. ブランチ名の命名規則の決定

```txt
feature/function_name

e.g: feature/login, feature/web-chat-interface
```

# 7. コード解説＝マネする手順
0. まずはね！githubを確認してください、`main/clone` branchに切り替えて、新しいVersionを`pull`してください！、やり方は覚えていませんか？？？
1. `app.py`のみに対して開発を行う。
2. まず、directory内で`app.py`を作成。
   1. 注：先に`feature/<function_name>`を作ってください、新しいfeatureブランチで開発を行ってください。
3. vscodeを立ち上げ、`app.py`を開き、各自担当の部分をコピペしてください。=>*6番を確認*
4. vscodeの設定上、システムのデフォルトpythonを使っているため、コピペした後、波線みたいなエラーが出てくる。
   1. 理由として、vscodeは”このprojectはPipenv環境の下にいる”であることがわかってないから。
   2. 解決として、Vscodeの右下pythonのバージョンを選択できる。`pipenv`環境が正常にインストールされた場合は`python 3.11.4('<project_name>:pipenv')`という風に選択肢が出てくるので、それを選択したらオッケー！[参考資料](https://freeheroblog.com/vscode-pipenv/)
5. 担当部分のコードのコピペが終了したら、pull request(PR)を出してみてください（俺をreviewerにするため、pull request出す画面でreviewer選択を行なってください。）
   **注意@PRを出す時、`git push origin <ここはmainではない>`,<>の中は今自分が作ったfeature branchの名前で書いてください・・・意味は、origin(remote repository)で新しいfeatureブランチを作って、そっちにpushする。**
6. 俺が承認してから、mergeするのボタンを各自押してみてください！何行目から書くのも決める必要がある。必ず守ってほしい！じゃないとコンフリクトが出てくる！prを出してからmergeする時のconflictが起こった場合の解決方法は俺もわからんので！

7. 全員の開発が完了したら、`main/clone`ブランチに対してもう一度自分のローカルのrepositoryの更新を行なってください！これでローカル上のflask　appが走れるようになる！

8. web appを走らせる方法
まず、`pipenv shell`で仮想環境に入る。次は`set FLASK_APP=app.py`コマンドを入力し、`flask run`したらオッケー。

もし以下のエラーが出たら
```shell
from jinja2 import escape
ImportError: cannot import name 'escape' from 'jinja2' (/Users/zheng.yuhao/.local/share/virtualenvs/gw_web_chat-8qGCZwLj/lib/python3.11/site-packages/jinja2/__init__.py)
```

`pipenv install Flask==2.1.0`コマンドを実行してみてください！バージョンの問題らしいぜ！

インストール終了後、`flask run`コマンド実行してください。

これで、ローカルの5000portにアクセスできるぜ！！（portはなにってまだ覚えてる？）iphoneからもアクセスできるはずですけど、、、どうやら会社の MACはfirewallが設定されてて、外部からのアクセスはできんわ・・・残念。
