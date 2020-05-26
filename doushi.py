from janome.tokenizer import Tokenizer
import csv
import pandas as pd

t = Tokenizer()
tokens = t.tokenize(input("入力して下さい:"))
for token in tokens:
        # 品詞を取り出し
    partOfSpeech = token.part_of_speech.split(',')[0]
    if partOfSpeech == "動詞":
        df = pd.read_csv('doushi.csv', encoding='utf_8', names=["見出し語","尊敬語","謙譲語","丁寧語"], usecols=[0,1,2,3],skiprows=[0], skipfooter=0, engine='python')
        df= df.replace({'\n': '<br>'}, regex=True)
        df= df.replace({'\r': ''}, regex=True)
        df = df[df['見出し語'].str.contains(token.surface)]
        #.emptyでCSVに入力されてない見出し語の場合に以下を出力
        if df.empty:
            print('ご指定の語句には対応しておりません')
            break
            # .to_stringインデックスの非表示
        print(df.drop("見出し語",axis=1).to_string(index=False).replace("尊敬語","").replace("謙譲語","").replace("丁寧語",""))
        # pprint.pprint(df.drop("見出し語",axis=1).to_string(index=False).replace("尊敬語","").replace("謙譲語","").replace("丁寧語",""))
    elif partOfSpeech =='名詞':
        ds = pd.read_csv('meishi.csv', encoding='utf_8', names=["見出し語","尊敬語","謙譲語","丁寧語"], usecols=[0,1,2,3], skiprows=[0], skipfooter=0, engine='python')
        ds= ds.replace({'\n': '<br>'}, regex=True)
        ds= ds.replace({'\r': ''}, regex=True)
        ds=ds[ds['見出し語'].str.contains(token.surface)]
        if ds.empty:
            print('ご指定の語句には対応しておりません')
            break
        print(ds.drop("見出し語", axis=1).to_string(index=False).replace("尊敬語","").replace("謙譲語","").replace("丁寧語",""))
    elif partOfSpeech =='助詞':
        ds = pd.read_csv('zyoshi.csv', encoding='utf_8', names=["見出し語","尊敬語","謙譲語","丁寧語"], usecols=[0,1,2,3], skiprows=[0], skipfooter=0, engine='python')
        ds= ds.replace({'\n': '<br>'}, regex=True)
        ds= ds.replace({'\r': ''}, regex=True)
        ds=ds[ds['見出し語'].str.contains(token.surface)]
        if ds.empty:
            print('ご指定の語句には対応しておりません')
            break
        print(ds.drop("見出し語", axis=1).to_string(index=False).replace("尊敬語","").replace("謙譲語","").replace("丁寧語",""))
    else :
        print("ご指定の語句には対応しておりません")
        break
