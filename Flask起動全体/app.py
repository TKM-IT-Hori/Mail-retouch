import yahoo
import doushi
import ProofreadingAPI
from flask import Flask, render_template, request, logging, Response, redirect, flash, Markup
app = Flask(__name__)

# 文章校正pyファイル
# 敬語pyファイル

# トップページ出力


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # return render_template('output.html')

# 文章校正ページ
@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        text = request.form['textarea1']
        yahoo_text = yahoo.yahoo(text)
        if not yahoo_text == None:
            yahoo_text = str(yahoo_text)
            yahoo_text = yahoo_text.strip("{[']}")
            yahoo_text = yahoo_text.replace("': '", ":")
            yahoo_text = yahoo_text.replace("', '", "")
            yahoo_text = Markup(yahoo_text)
            # print(yahoo_text)
        elif yahoo_text == None:
            yahoo_text = "変換ミスや誤用などは検出されませんでした。結果はあくまで目安ですのでご自身でも再度ご確認ください。"
        return render_template('index.html', text=yahoo_text, beforeText=text)

# 敬語ページ
@app.route('/keigo', methods=['GET', 'POST'])
def keigo():
    # ボタン押し前
    if request.method == 'GET':
        dropText = "動詞を選択して▽ボタンを押してください。"
        return render_template('index2.html', dropText=dropText, sonkei=[], kennzyou=[], teinei=[], s_count=0, k_count=0, t_count=0)
    # ボタン押した後
    else:
        # 送られたワード
        keigo = request.form["keigotext"]
        print(keigo)
        text = request.form["keigosearch"]
        # 解析
        kaiseki = doushi.doushi(text)
        print(kaiseki)
        # 結果あり
        if type(kaiseki) == tuple:
            dropText = "敬語の検索結果です。選択+クリックでコピー。"
            # リスト処理
            sonkei = str(kaiseki[0])  # sonkei
            sonkei = sonkei.strip("[']")
            sonkei = sonkei.split()
            s_count = len(sonkei)
            print(sonkei)
            # リスト処理
            kennzyou = str(kaiseki[1])  # kennzyou
            kennzyou = kennzyou.strip("[']")
            kennzyou = kennzyou.split()
            k_count = len(kennzyou)
            print(kennzyou)
            # リスト処理
            teinei = str(kaiseki[2])  # teinei
            teinei = teinei.strip("[']")
            teinei = teinei.split()
            t_count = len(teinei)
            print(teinei)
        # 結果無し
        elif type(kaiseki) == str:
            print(kaiseki)
            dropText = Markup(kaiseki)
            sonkei = []
            kennzyou = []
            teinei = []
            s_count = 0
            k_count = 0
            t_count = 0


        # 変数送信
        return render_template('index2.html', dropText=dropText, selectWord=text, sonkei=sonkei, kennzyou=kennzyou, teinei=teinei, s_count=s_count, k_count=k_count, t_count=t_count, keigo=keigo)


if __name__ == "__main__":
    app.run(debug=True)
