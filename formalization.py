dictionary = open('formalization_dictionary.txt')


def formalize(original):
    for words in dictionary:
        original = original.lower()
        un_baku, baku = words.split(':')
        if (original in words) and len(original) == len(un_baku) and (original in un_baku):
            # print("INI IF")
            return baku
    #     print("INI FOR")
    # print("INI GA KEMANA2")
    return original

word = input("Masukkan kata : ")
print("Hasil : ",formalize(word))
