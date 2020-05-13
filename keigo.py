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
    )
    #リストに追加
    list2.append(item_mod)
    
print("置換後：{0}".format(list2))