filePositive = open('positive.txt')
fileNegative = open('negative.txt')


def weighting(kata):
    pos_count = 0
    neg_count = 0
    for list_ptv in filePositive:
        if kata == list_ptv:
            pos_count += 1

    for list_ngv in fileNegative:
        if kata == list_ngv:
            neg_count += 1

    result = pos_count - neg_count
    if result > 1:
        result = 1
    elif result < -1:
        result = -1
    return result


sent = input("Masukan kata : ")
print("Hasil : ", weighting(sent))
