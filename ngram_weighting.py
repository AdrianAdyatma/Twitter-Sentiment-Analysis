
def generate_ngrams(sentence, n):
    # Tokenize
    tokens = [token for token in sentence.split(" ") if token != ""]
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


def weighting(sentence):
    n = 4
    weight = 0
    while n > 0:
        for item_gram in generate_ngrams(sentence, n):
            for row in open(r'references/weighting_data.txt'):
                kata, nilai = row.split(':')
                nilai = int(nilai)
                if item_gram == kata:
                    if nilai == 1:
                        weight += 1
                    elif nilai == -1:
                        weight -= 1
                    # Print kata yang terbobot
                    print("\nKata terbobot pada n", n, ":", item_gram)
                    sentence = sentence.replace(item_gram, '', 1)
                    break
        n -= 1
    return weight
