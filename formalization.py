import csv
import itertools


# First, check in formal word from KBBI
def formalize1(original):
    with open('references/kata_kelas_makna.tsv', encoding="utf8") as dictionary_1:
        reader = csv.DictReader(dictionary_1, dialect='excel-tab')
        # Check every row for same word, if exists then return True, if doesn't then return False
        for row in reader:
            if original == row.get("kata"):
                return True


# Check word from 'alay' dictionary
def formalize2(original):
    with open('references/alay_dict.txt') as dictionary_2:
        # Check every row for same word, if exists then return correct word, if doesn't then return False
        for row in dictionary_2:
            un_baku, baku = row.split(':')
            if original == un_baku:
                return baku


# Main formalization function
def formalize(original):
    formalizing = original
    i = 0
    while i < 3:
        if formalize2(formalizing) is not None:
            print("masuk 2")
            return formalize2(formalizing)
        elif formalize1(formalizing) is True:
            print("masuk 1")
            return formalizing
        elif i == 0:
            print("masuk 3")
            formalizing = ''.join([c for c in formalizing if not c.isdigit()])
        elif i == 1:
            print("masuk 4")
            formalizing = ''.join(c[0] for c in itertools.groupby(formalizing))
        i += 1
    return formalizing


word = input("Masukkan kata : ")
print("Hasil : ", formalize(word.lower()))

