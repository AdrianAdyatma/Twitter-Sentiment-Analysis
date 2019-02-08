import csv

from collections import Counter


def cek_alay_kbbi():
    with open('references/alay_dict.txt') as alay:
        for row1 in alay:
            un_baku, baku = row1.split(':')
            with open('references/kata_kelas_makna.tsv', encoding="utf8") as kbbi:
                reader = csv.DictReader(kbbi, dialect='excel-tab')
                for row2 in reader:
                    if un_baku == row2.get("kata"):
                        with open('references/data.txt', 'a') as data:
                            data.write(str(un_baku + " = " + baku + " -- " + row2.get("kata") + "\n"))
                        print(un_baku, "=", baku, "--", row2.get("kata"))
                        break


def cek_kembar_per_file():
    with open('references/positive.txt') as f:
        c = Counter(c.strip().lower() for c in f if c.strip())
    for line in c:
        if c[line] > 1:
            print(line)


def cek_kembar_pos_neg():
    count = 0
    with open('references/positive.txt') as p:
        for pos in p:
            with open('references/negative.txt') as n:
                for neg in n:
                    if pos == neg:
                        count += 1
                        print(pos, neg)
    print(count)


def sort():
    with open('references/positive.txt', 'r') as r:
        for line in sorted(r):
            with open('references/positive.txt', 'a') as w:
                w.write(line)
                print(line, end='')

def give_value():
    with open("references/positive.txt") as pos1:
        for i in pos1:
            with open("references/pos_n.txt", "a") as pos2:
                pos2.write(i.replace("\n", ":1\n"))

    with open("references/negative.txt") as pos1:
        for i in pos1:
            with open("references/neg_n.txt", "a") as pos2:
                pos2.write(i.replace("\n", ":-1\n"))

# cek_alay_kbbi()
# cek_kembar_per_file()
# cek_kembar_pos_neg()
# sort()
give_value()
