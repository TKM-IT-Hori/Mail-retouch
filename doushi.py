from janome.tokenizer import Tokenizer
import neologdn
import csv
import pandas as pd

t = Tokenizer()
tokens = t.tokenize(input("入力して下さい:"))

for token in tokens:
    # 品詞を取り出し
    partOfSpeech = token.part_of_speech.split(',')[0]
    if partOfSpeech == "動詞":
        s=input("尊敬語:1,謙譲語:2,丁寧語:3 ->")
        df = pd.read_csv('doushi.csv', encoding='utf_8', names=["動詞","尊敬語","謙譲語","丁寧語"], usecols=[0,int(s)], skiprows=[0], skipfooter=0, engine='python')
        df= df.replace({'\n': '<br>'}, regex=True)
        df= df.replace({'\r': ''}, regex=True)
        df = df[df['動詞'].str.contains(token.surface)]
        # .drop 入力された名詞の削除
        # .to_stringインデックスの非表示
        print(df.drop("動詞", axis=1).to_string(index=False))

    # elif partOfSpeech =='名詞':
    #     s=input("尊敬語:1,謙譲語:2,丁寧語:3 ->")
    #     ds = pd.read_csv('meishi.csv', encoding='utf_8', names=["名詞","尊敬語","謙譲語","丁寧語"], usecols=[0,int(s)], skiprows=[0], skipfooter=0, engine='python')
    #     ds= ds.replace({'\n': '<br>'}, regex=True)
    #     ds= ds.replace({'\r': ''}, regex=True)
    #     ds=ds[ds['名詞'].str.contains(token.surface)]
    #     # .drop 入力された名詞の削除
    #     # .to_stringインデックスの非表示
    #     print(ds.drop("名詞", axis=1).to_string(index=False))
    
    # elif partOfSpeech =='副詞':
    #     print("副詞:"+token.surface)
    # elif partOfSpeech =='形容詞':
    #     print("形容詞:"+token.surface)
    # elif partOfSpeech =='判定詞':
    #     print("判定詞:"+token.surface)
    # elif partOfSpeech =='助動詞':
    #     print("助動詞:"+token.surface)
    # elif partOfSpeech =='接続詞':
    #     print("接続詞:"+token.surface)
    # elif partOfSpeech =='感動詞':
    #     print("感動詞:"+token.surface)
    # elif partOfSpeech =='記号':
    #     print("記号:"+token.surface)
    # elif partOfSpeech =='連用形':
    #     print("連用形:"+token.surface)
    else :
        print(token.surface)
        break

