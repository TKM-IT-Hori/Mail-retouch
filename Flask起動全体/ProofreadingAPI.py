import requests
import neologdn 
import urllib
import json

API = "https://api.a3rt.recruit-tech.co.jp/proofreading/v2/typo"
KEY ="DZZeKNl2D5dOTRkkQtmDtIusXc367NfS" 
# =input('校正を行います:')


def proofread(beforetext):
    quoted_text = beforetext
    # s=neologdn.normalize(quoted_text)

    values = {
    'apikey': KEY,
    'sentence':quoted_text,
    'sensitivity':"low",
    }
    # パラメータをURLエンコードする
    params = urllib.parse.urlencode(values)
    # リクエスト用のURLを生成
    url = API + "?" + params
    #リクエストを投げて結果を取得
    r = requests.get(url)
    #辞書型に変換
    data = json.loads(r.text)
    suggestions=[]
    rets = []

    if data['status'] == 1:
        rets = '疑わしいと判定された箇所があります。'
        text = data['checkedSentence']
        out1 = "メッセージ:"+rets+"&#13;"#テキストエリア内改行特殊文字
        out2 = "間違い箇所:"+text+"&#13;"
        # print(out1)
        # print(out2)

        # text = data['normalizedSentence']
        #指摘単語に対するSuggestionを取得    
        for i in range(len(data['alerts'])):
                        #間違い箇所と修正候補出力
            suggestions.append([data['alerts'][i]['word'], data['alerts'][i]['suggestions']])
            out3 = str(suggestions)
            # print(out3)
        
        outs = (out1 + out2 + out3)
        # print(outs)
        return outs

    elif data['status'] == 0:
        out4 = "変換ミスや誤用は検出されませんでした。&#13;結果はあくまで目安ですので、ご自身でも再度ご確認ください"
        # print("この文章に誤字脱字はありません。")
        return out4
    else:
        out5 = "エラーが発生しました。&#13;ステータスコードは" + data['status'] + "です。"
        # print(out5)
        return out5
    # print(data)

# proofread("システムの規格から開発・運用まＤ幅広く関われます。")
