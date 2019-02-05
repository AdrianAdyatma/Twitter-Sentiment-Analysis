import csv


def cek():
    with open('references/formalization_dictionary.txt') as alay:
        for row1 in alay:
            un_baku, baku = row1.split(':')
            with open('references/kata_kelas_makna.tsv', encoding="utf8") as kbbi:
                reader = csv.DictReader(kbbi, dialect='excel-tab')
                for row2 in reader:
                    if un_baku == row2.get("kata"):
                        with open('data.txt', 'a') as data:
                            data.write(str(un_baku+" = "+baku+" -- "+row2.get("kata")+"\n"))
                        print(un_baku, "=", baku, "--", row2.get("kata"))
                        break


cek()
