from janome.tokenizer import Tokenizer
import csv
import pandas as pd

def doushi(honorific):
    t = Tokenizer()
    tokens = t.tokenize(honorific)
    for token in tokens:
            # 品詞を取り出し
        partOfSpeech = token.part_of_speech.split(',')[0]
        if partOfSpeech == "動詞":
            df = pd.read_csv('doushi2.csv', encoding='utf_8', names=["見出し語","尊敬語","謙譲語","丁寧語"], usecols=[0,1,2,3],skiprows=[0], skipfooter=0, engine='python')
            df= df.replace({'\n': '<br>'}, regex=True)
            df= df.replace({'\r': ''}, regex=True)
            df = df[df['見出し語']==token.surface]
            #.emptyでCSVに入力されてない見出し語の場合に以下を出力
            if df.empty:
                response_empty='<font color="red">ご指定の語句には対応しておりません</font>'
                return response_empty
            
            # if honorific==token.surface:
                
                

            #尊敬語配列
            son=df["尊敬語"].to_string(index=False).replace("\n","").replace("NaN","").replace("'","")
            s=[son]
            #謙譲語配列
            ken=df["謙譲語"].to_string(index=False).replace("\n","").replace("NaN","")
            k=[ken]
            #丁寧語配列
            tei=df["丁寧語"].to_string(index=False).replace("\n","").replace("NaN","")
            t=[tei]
            return s,k,t

            # response_string=df.drop("見出し語",axis=1).to_string(index=False)
            # response_string={df.drop("見出し語",axis=1).to_string(index=False).replace("尊敬語","").replace("謙譲語","").replace("丁寧語","")}
            # return response_string
            #pprint.pprint(df.drop("見出し語",axis=1).to_string(index=False).replace("尊敬語","").replace("謙譲語","").replace("丁寧語",""))
        
        elif partOfSpeech =='名詞':
            ds = pd.read_csv('meishi.csv', encoding='utf_8', names=["見出し語","尊敬語","謙譲語","丁寧語"], usecols=[0,1,2,3], skiprows=[0], skipfooter=0, engine='python')
            ds= ds.replace({'\n': '<br>'}, regex=True)
            ds= ds.replace({'\r': ''}, regex=True)
            ds=ds[ds['見出し語']==(token.surface)]
            if ds.empty:
                response_empty='<font color="red">ご指定の語句には対応しておりません</font>'
                return response_empty
            #尊敬語配列
            son=ds["尊敬語"].to_string(index=False).replace("\n","").replace("NaN","").replace("'","")
            s=[son]
            #謙譲語配列
            ken=ds["謙譲語"].to_string(index=False).replace("\n","").replace("NaN","")
            k=[ken]
            #丁寧語配列
            tei=ds["丁寧語"].to_string(index=False).replace("\n","").replace("NaN","")
            t=[tei]
            return s,k,t
            # response_string=ds.drop("見出し語", axis=1).to_string(index=False).replace("尊敬語","").replace("謙譲語","").replace("丁寧語","")
            # return response_string
        
        elif partOfSpeech =='助詞':
            ds = pd.read_csv('zyoshi.csv', encoding='utf_8', names=["見出し語","尊敬語","謙譲語","丁寧語"], usecols=[0,1,2,3], skiprows=[0], skipfooter=0, engine='python')
            ds= ds.replace({'\n': '<br>'}, regex=True)
            ds= ds.replace({'\r': ''}, regex=True)
            ds=ds[ds['見出し語']==(token.surface)]
            if ds.empty:
                response_empty='<font color="red">ご指定の語句には対応しておりません</font>'
                return response_empty

            #尊敬語配列
            son=ds["尊敬語"].to_string(index=False).replace("\n","").replace("NaN","").replace("'","")
            s=[son]
            #謙譲語配列
            ken=ds["謙譲語"].to_string(index=False).replace("\n","").replace("NaN","")
            k=[ken]
            #丁寧語配列
            tei=ds["丁寧語"].to_string(index=False).replace("\n","").replace("NaN","")
            t=[tei]
            return s,k,t
            # response_string=ds.drop("見出し語", axis=1).to_string(index=False).replace("尊敬語","").replace("謙譲語","").replace("丁寧語","")
            # return response_string

        else:
            if honorific:
                df = pd.read_csv('doushi2.csv', encoding='utf_8', names=["見出し語","尊敬語","謙譲語","丁寧語"], usecols=[0,1,2,3],skiprows=[0], skipfooter=0, engine='python')
                df= df.replace({'\n': '<br>'}, regex=True)
                df= df.replace({'\r': ''}, regex=True)
                #janomeで解析せず、見出し語と入力された語句が一致した場合に尊敬語・謙譲語・丁寧語を出力
                df = df[df['見出し語']==honorific]
                if df.empty:
                    response_empty='<font color="red">ご指定の語句には対応しておりません</font>'
                    return response_empty
                
                son=df["尊敬語"].to_string(index=False).replace("\n","").replace("NaN","").replace("'","")
                s=[son]
                #謙譲語配列
                ken=df["謙譲語"].to_string(index=False).replace("\n","").replace("NaN","")
                k=[ken]
                #丁寧語配列
                tei=df["丁寧語"].to_string(index=False).replace("\n","").replace("NaN","")
                t=[tei]
                return s,k,t

            else:
                response_error='<font color="red">ご指定の語句には対応しておりません</font>'
                return response_error

if __name__=="__main__":
    while True:
        user_input=input("語句を入力してください:")
        if not user_input:
            break
        print(doushi(user_input))
