file = open('formalizationDict.txt')

def formalizationDict(kata):
    for list in file:
        unBaku, Baku = list.split(':')
        # print(list.split())
        # print(list)
        if (kata in list) and len(kata)==len(unBaku):
            print(list)
            if kata in unBaku:
                # print(list)
                return Baku
            else:
                return kata
        # elif (kata in list) and len(kata)!= len(unBaku):
    return kata

sent = input("Masukan Kalimat : ")
print("Hasil : ",formalizationDict(sent))