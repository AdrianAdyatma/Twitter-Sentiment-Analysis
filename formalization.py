import csv


# def formalize1(original):
#     for words in dictionary_1:
#         kata, kelas, makna = words.split('  ')
#         if (original in kata) and len(original) == len(kata):
#             return kata

# def formalize2(original):
#     for words in dictionary_2:
#         un_baku, baku = words.split(':')
#         if (original in un_baku) and len(original) == len(un_baku):
#             return baku

# def formalize1(original):
#     with open('kata_kelas_makna.txt') as dictionary_1:
#         reader = csv.DictReader(dictionary_1, dialect='excel-tab')
#         for words in reader:
#             if (original )

def formalize2(original):
    with open('formalization_dictionary.txt') as dictionary_2:
        for words in dictionary_2:
            un_baku, baku = words.split(':')
            if original == un_baku:
                return baku


word = input("Masukkan kata : ")
print("Hasil : ", formalize2(word.lower()))
