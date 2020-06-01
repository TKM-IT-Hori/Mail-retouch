import urllib.parse
import urllib.request
import xml.etree.ElementTree as xml
import sys

appid = "dj00aiZpPVhDRk8yQjZObTRZaiZzPWNvbnN1bWVyc2VjcmV0Jng9Y2M-"
# 添削したい文章を入力
def yahoo(honorific):
    a = honorific
    sentence1 = urllib.parse.quote(a.encode('utf-8'))
    KOUSEI_NAMESPACE = '{urn:yahoo:jp:jlp:KouseiService}'
    FURIGANA_NAMESPACE = '{urn:yahoo:jp:jlp:FuriganaService}'

    # URLの生成（sentence以下は校正項目のフィルタリング）
    b = "https://jlp.yahooapis.jp/KouseiService/V1/kousei?appid="+appid+"&sentence="+sentence1+"&no_filter="
    
    recv = urllib.request.urlopen(b).read()
    data = xml.fromstring(recv)

    results = []
    for result in list(data):
        startPos = int(result.findtext(KOUSEI_NAMESPACE + 'StartPos'))
        length = int(result.findtext(KOUSEI_NAMESPACE + 'Length'))
        endPos = startPos + length
        surface = result.findtext(KOUSEI_NAMESPACE + 'Surface')
        shitekiWord = result.findtext(KOUSEI_NAMESPACE + 'ShitekiWord')
        shitekiInfo = result.findtext(KOUSEI_NAMESPACE + 'ShitekiInfo')

        results.append({
            '間違い箇所-->':surface+'&#13;',
            '間違い内容-->':shitekiInfo+'&#13;',
            '置換結果 -->': shitekiWord+'&#13;',
            })
        return results

if __name__ == "__main__":
	while True:
		user_input = input("校正します：")
		if not user_input:
		 	break
		if yahoo(user_input) is None:
			break
		print(yahoo(user_input))
