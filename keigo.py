import neologdn 

text=input('校正を行います:')
#neologdnで正規化→連続した伸ばし棒や全角が半角へ変換
seikika=neologdn.normalize(text)

list1=[seikika]
list2 = []

print("置換中：{0}".format(list1))

for item in list1:
    
    #文字列の置換
    item_mod = (item.replace('となります', 'です').replace('である', 'です').replace('なるほどですね', 'おっしゃる通りだと思います')
    .replace('しばらくぶりです', 'ご無沙汰しております')
    .replace('お世話様です', 'お世話になっております').replace('了解しました', '承知しました').replace('厚く', '深く')
    .replace('ご苦労様です', 'お疲れ様です')
    .replace('どうしましょうか', 'いかが致しましょうか').replace('ご一緒します', 'お供させていただきます')
    .replace('参考になりました', '勉強になりました').replace('すいません', '申し訳ございません')
    .replace('すみません', '申し訳ございません').replace('します', 'いたします').replace('わが社', '弊社')
    .replace('どうかいたしましたか？', 'いかがなさいましたか？')
    .replace('おっしゃられました', 'おっしゃいました')

    # https://business-textbooks.com/honorific70/
    # 社会人の教科書間違えやすいビジネス敬語70選　ソースが曖昧なため使用するかどうかは要相談

    .replace('これ', 'こちら').replace('ここ', 'こちら').replace('こっち', 'こちら')
    .replace('それ', 'そちら').replace('そこ', 'そちら').replace('そっち', 'そちら')
    .replace('あれ', 'あちら').replace('あそこ', 'あちら').replace('あっち', 'あちら')
    .replace('どれ', 'どちら').replace('どこ', 'どちら').replace('どっち', 'どちら')
    .replace('どう', 'いかが').replace('どのくらい', 'いかほど').replace('ほんとうに', 'まことに')
    .replace('少し', '少々').replace('よい', 'よろしい').replace('うまい', 'おいしい')
    .replace('きょう', '本日').replace('きのう', '昨日').replace('おととい', '一昨日')
    .replace('今日','本日').replace('あす', '明日').replace('あさって', 'あさって')
    .replace('あすの朝', '明朝').replace('明日の朝', '明朝').replace('あすの夜', '明晩').replace('明日の夜', '明晩').replace('今年', '本年')
    .replace('ことし', '本年').replace('去年', '昨年').replace('おととし', '一昨年')
    .replace('来年', '明年').replace('このあいだ', '先日').replace('この間', '先日')
    .replace('今度', 'このたび').replace('いま', 'ただいま').replace('さっき', 'さきほど')
    .replace('あとで', '後ほど').replace('後で', '後ほど')
    .replace('わたし', 'わたくし').replace('前に', '以前').replace('ちょっと', '少々')
    .replace('すごく', '非常に').replace('とても', '大変')
    )
    #リストに追加
    list2.append(item_mod)
    
# https://www.sanseido.biz/Main/Words/hyakka/Sonkei/03.aspx
# 三省堂より参照(29~41行目)

print("置換後：{0}".format(list2))