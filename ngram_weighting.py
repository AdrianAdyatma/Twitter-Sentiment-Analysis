import re


def generate_ngrams(sentence, n):
    # Tokenize
    tokens = [token for token in sentence.split(" ") if token != ""]
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


# sent = input("Masukkan kalimat : ")
sent = "anda baik sekali alam mimpi itu indah terbaik melebihi alam mimpi"
list_hasil = generate_ngrams(sent, 2)

print('hasil: ', list_hasil)

pos_var = 0

for item in list_hasil:
    with open('references/positive.txt') as pos:
        for c in pos:
            if item == c.replace('\n', ''):
                pos_var += 1
                sent = sent.replace(item, '', 1)

list_hasil = generate_ngrams(sent, 1)
print(list_hasil)

for item in list_hasil:
    with open('references/positive.txt') as pos:
        for c in pos:
            if item == c.replace('\n', ''):
                pos_var += 1
                sent = sent.replace(item, '', 1)

print('hasil: ', sent, '\npos: ', pos_var)
