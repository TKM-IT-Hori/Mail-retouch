import requests
import json
import re
 
class Api:
    def __init__(self):
        self.key = 'DZZeKNl2D5dOTRkkQtmDtIusXc367NfS'
        self.api = 'https://api.a3rt.recruit-tech.co.jp/proofreading/v2/typo'
 
    def get(self,inputtext):
        url = self.api
        quoted_text = inputtext
        r = requests.post(url,{
            'apikey':self.key,
            'sentence':quoted_text})

        data = json.loads(r.text)
        rets = []
        suggestions = []

        if data['status'] == 1:
            rets = '<font color="red">疑わしい部分と判定された箇所があります。</br>色がついた箇所を確認してください。</font></br><hr>'
            text = data['checkedSentence']
            rets = rets + self.__trans_word(text)
            #指摘単語に対するSuggestionを取得    
            for i in range(len(data['alerts'])):
                suggestions.append([data['alerts'][i]['word'], data['alerts'][i]['suggestions']])
        elif data['status'] == 0:
            rets = "この文章に誤字脱字はありません。</br>指摘すべき修正を見つけられませんでした。"
        else:
            rets = "エラーがありました。</br>応答コードは" + data['status'] + "です。"
        return rets, suggestions
 
    def __trans_word(self,inputtext):
        replacements = {'<<':'<span class="mark font-weight-bold text-danger" style="background-color:yellow">','>>':'</span>'}
        return re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], inputtext)]

        