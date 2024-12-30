
def single_root_words(root_word, *other_words):
    same_words = []
   # print(type(other_words))
    ad = list(other_words)

    for i in ad:
        md = str(i)
        sl = root_word.lower()
        sl2 = md.lower()
        if sl in sl2:
            same_words.append(i)
            continue
        if sl2 in sl:
            same_words.append(i)
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)