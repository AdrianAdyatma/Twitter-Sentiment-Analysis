import re
import nltk
import numpy as np
import formalization

import ngram_weighting

example = "Presiden Jokowi github.com/adrianadyatma telah berhasil macam-macam janjinya pada akhir tahun, masa-masa kesuksesan tugas tsb dirayakan di Istana Bogor dengan keluarga. #JokowiAja https://t.co/WAOAW9sja"


def my_tokenizer(s):
    s = re.sub(r'http\S+|@(\w+)|#(\w+)|-(\w+)|[^a-zA-Z0-9\-\s]', '', s).lower()
    tokens = nltk.tokenize.word_tokenize(s)
    print(tokens)
    tokens = [formalization.formalize(t) for t in tokens]
    print(tokens)
    # tokens = [t for t in tokens if t in open(r'references/positive.txt') or t in open(r'references/negative.txt')]


if __name__ == '__main__':
    my_tokenizer(example)
