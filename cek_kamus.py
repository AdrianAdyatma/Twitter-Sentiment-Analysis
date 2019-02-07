import csv

from collections import Counter


def cek():
    with open('references/alay_dict.txt') as alay:
        for row1 in alay:
            un_baku, baku = row1.split(':')
            with open('references/kata_kelas_makna.tsv', encoding="utf8") as kbbi:
                reader = csv.DictReader(kbbi, dialect='excel-tab')
                for row2 in reader:
                    if un_baku == row2.get("kata"):
                        with open('data.txt', 'a') as data:
                            data.write(str(un_baku + " = " + baku + " -- " + row2.get("kata") + "\n"))
                        print(un_baku, "=", baku, "--", row2.get("kata"))
                        break


def cek_duplikat():
    with open('references/negative.txt') as f:
        c = Counter(c.strip().lower() for c in f if c.strip())
    for line in c:
        if c[line] > 1:
            print(line)

def cek_n_p():
    count = 0
    with open('references/positive.txt') as p:
        for pos in p:
            with open('references/negative.txt') as n:
                for neg in n:
                    if pos == neg:
                        count +=1
                        print(pos, neg)
    print(count)


# cek()
cek_duplikat()
cek_n_p()