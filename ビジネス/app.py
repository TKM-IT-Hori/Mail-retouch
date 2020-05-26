from flask import Flask, render_template, request, logging, Response, redirect, flash
app = Flask(__name__)

import ProofreadingAPI


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # return render_template('output.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        text = request.form['textarea1']
        # proofreedingAPI.proofread(text)
        retouch_text = ProofreadingAPI.proofread(text)
        return render_template('index.html', text=retouch_text, beforeText=text)

@app.route('/keigo', methods=['GET', 'POST'])
def keigo():
    if request.method == 'GET':
        dropText = "動詞を選択して▽ボタンを押してください。"
        return render_template('index2.html', dropdownText=dropText)
    else:
        keigo = request.form["keigosearch"]
        print(keigo)
        return render_template('index2.html',dropdownText="敬語の検索結果です。",keigo="aaa")


if __name__ == "__main__":
    app.run(debug=True)
