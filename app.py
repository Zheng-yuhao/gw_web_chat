






























































































































# ログイン画面表示
@app.route("/login")
def login_get():
    return render_template("login.html")


# ログインするプログラム。
@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name")
    password = request.form.get("password")
    conn = sqlite3.connect('chattest.db')
    c = conn.cursor()
    c.execute(
        "select id from user where name = ? and password = ?", (name, password))
    user_id = c.fetchone()
    conn.close()
    print(type(user_id))
    if user_id is None:
        return render_template("login.html")
    else:
        session['user_id'] = user_id[0]
        return redirect("/userlist")


# アカウント作成(新規ユーザー登録)プログラム
@app.route("/regist", methods=["POST"])
def regist():
    name = request.form.get("name")
    password = request.form.get("password")
    conn = sqlite3.connect('chattest.db')
    c = conn.cursor()
    c.execute("insert into user values(null,?,?)", (name, password))
    conn.commit()
    conn.close()
    return redirect("/login")


# ログアウト
@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")