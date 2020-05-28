import sys
import urllib
import xml.etree.ElementTree as xml


KOUSEI_NAMESPACE = '{urn:yahoo:jp:jlp:KouseiService}'
FURIGANA_NAMESPACE = '{urn:yahoo:jp:jlp:FuriganaService}'


def Proofread(appid, string, filter=None, mask=None):
	results = Spellcheck(appid, string, filter, mask)

	shift = 0
	ret = string
	for result in results:
		if result['ShitekiWord']:
			ret = ret[:result['StartPos'] + shift] + result['ShitekiWord'] + ret[result['EndPos'] + shift:]
			shift += len(result['ShitekiWord']) - result['Length']

	if ret != string:
		return ret


def Spellcheck(appid, string, filter=None, mask=None):
	query  = 'http://jlp.yahooapis.jp/KouseiService/V1/kousei?'
	query += 'dj00aiZpPVhDRk8yQjZObTRZaiZzPWNvbnN1bWVyc2VjcmV0Jng9Y2M-' + appid + '&'
	if isinstance(filter, list) or isinstance(filter, tuple):
		query += 'filter_group=' + ','.join([str(x) for x in set(filter)]) + '&'
	if isinstance(mask, list) or isinstance(mask, tuple):
		query += 'no_filter=' + ','.join([str(x) for x in set(mask)]) + '&'
	query += 'sentence=' + urllib.quote(string.encode('utf-8'))

	recv = urllib.urlopen(query).read()
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
			'StartPos': startPos,
			'EndPos': endPos,
			'Length': length,
			'Surface': surface,
			'ShitekiWord': shitekiWord,
			'ShitekiInfo': shitekiInfo,
		})

	return results


def Ruby(appid, string, grade=1, start='(', end=')'):
	query  = 'http://jlp.yahooapis.jp/FuriganaService/V1/furigana?'
	query += 'dj00aiZpPVhDRk8yQjZObTRZaiZzPWNvbnN1bWVyc2VjcmV0Jng9Y2M-' + appid + '&'
	if grade and grade >= 1 and grade <= 8:
		query += 'grade=' + str(grade) + '&'
	query += 'sentence=' + urllib.quote(string.encode('utf-8'))

	recv = urllib.urlopen(query).read()
	data = xml.fromstring(recv)

	ret = string
	for result in list(list(list(data)[0])[0]):
		src = result.findtext(FURIGANA_NAMESPACE + 'Surface')
		dst = result.findtext(FURIGANA_NAMESPACE + 'Furigana')

		if src and dst:
			dst = src + start + dst + end
			ret = ret.replace(src, dst)

	return ret


if __name__ == '__main__':
	if len(sys.argv) <= 2:
		print(u'yahoo APIを使用した日本語文の校正プログラムです。')
		sys.exit(1)

	arg = ' '.join(sys.argv[2:])
	for enc in ('cp932', 'utf-8', 'euc-jp', 'iso-2022-jp'):
		try:
			arg = arg.decode(enc)
			break
		except:
			pass

	ret = Proofread(sys.argv[1], arg)
	if ret:
		print(ret)
	else:
		print(u'校正の必要はありません')
		sys.exit(-1)
