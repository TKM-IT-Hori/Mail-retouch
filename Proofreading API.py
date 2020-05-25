import requests
import neologdn 
import urllib
import json

API = "https://api.a3rt.recruit-tech.co.jp/proofreading/v2/typo"
KEY ="DZZeKNl2D5dOTRkkQtmDtIusXc367NfS" 
quoted_text=input('校正を行います:')
s=neologdn.normalize(quoted_text)

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
    # text = data['normalizedSentence']
    #指摘単語に対するSuggestionを取得    
    for i in range(len(data['alerts'])):
                    #間違い箇所と修正候補出力
        suggestions.append([data['alerts'][i]['word'], data['alerts'][i]['suggestions']])
    
        print("メッセージ:"+rets)
        print("間違い箇所:"+text)
        print(suggestions)
elif data['status'] == 0:
    print("この文章に誤字脱字はありません。")
else:
    print("エラーが発生しました。ステータスコードは" + data['status'] + "です。")

# print(data)
