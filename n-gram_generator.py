import re

filePositive = open('positive.txt')

# for list in filePositive:
#     a = (list.replace(" ",""))
#     print(a)

def generate_ngrams(s, n):
    s = s.lower()
    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    print(s)
    # Tokenize
    tokens = [token for token in s.split(" ") if token != ""]

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


sent = input("Masukkan kalimat : ")
ngram = int(input("Masukkan (n)gram: "))
print('hasil: ',generate_ngrams(sent,ngram))
