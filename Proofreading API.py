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
'sensitivity':"medium",
}
# パラメータをURLエンコードする
params = urllib.parse.urlencode(values)
# リクエスト用のURLを生成
url = API + "?" + params
 
#リクエストを投げて結果を取得
r = requests.get(url)
#辞書型に変換
data = json.loads(r.text)

print(data)
# print("正規化:"+s)
# print("敬語置換:"+s.replace('となります', 'です').replace('だ', 'です'))
