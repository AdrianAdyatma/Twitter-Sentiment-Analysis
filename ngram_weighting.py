def generate_ngrams(sentence, n):
    # Tokenize
    tokens = [token for token in sentence.split(" ") if token != ""]
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


# # sent = input("Masukkan kalimat : ")
# sent = "anda baik sekali alam mimpi itu indah terbaik melebihi alam mimpi"
# list_hasil = generate_ngrams(sent, 2)
#
# print('hasil: ', list_hasil)
#
# pos_var = 0
#
# for item in list_hasil:
#     with open('references/positive.txt') as pos:
#         for c in pos:
#             if item == c.replace('\n', ''):
#                 pos_var += 1
#                 sent = sent.replace(item, '', 1)
#
# list_hasil = generate_ngrams(sent, 1)
# print(list_hasil)
#
# for item in list_hasil:
#     with open('references/positive.txt') as pos:
#         for c in pos:
#             if item == c.replace('\n', ''):
#                 pos_var += 1
#                 sent = sent.replace(item, '', 1)
#
# print('hasil: ', sent, '\npos: ', pos_var)


def weighting(sentence):
    n = 4
    weight = 0
    while n > 0:
        list_temp = generate_ngrams(sentence, n)
        for item_gram in list_temp:
            with open('references/weighting_data.txt') as data:
                for row in data:
                    kata, nilai = row.split(':')
                    nilai = int(nilai.replace('\n', ''))
                    if item_gram == kata:
                        if nilai == 1:
                            weight += 1
                        elif nilai == -1:
                            weight -= 1
                        sentence = sentence.replace(item_gram, '', 1)
        n -= 1
    return weight
