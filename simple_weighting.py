filePositive = open('references/positive.txt')
fileNegative = open('references/negative.txt')


def weighting(kata):
    pos_count = 0
    neg_count = 0
    for list_ptv in filePositive:
        if kata == list_ptv:
            pos_count += 1

    for list_ngv in fileNegative:
        if kata == list_ngv:
            neg_count += 1

    return pos_count - neg_count


sent = input("Masukan kata : ")
print("Hasil : ", weighting(sent))

# MASIH PERLU PERBAIKAN
# TAMBAHIN CEK KESAMAAN PANJANG
# PAKE N GRAM
