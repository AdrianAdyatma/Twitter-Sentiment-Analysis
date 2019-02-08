from nltk.tokenize import TweetTokenizer
import re

import formalization

# import ngram_weighting

sentence_example = "Presiden Jok0 Widodo a+ Jum'atan @jokowi https://mantap.com #Jokowi2Periode pada hari-hari ini bertemu dengan Bpk. Hj. Prabowo Subianto dan cipika cipiki dengan istri2nyaaa sebelum 7an!!! @pointer_ID https://t.co/Fys3PYcjlS"


def format_word(sentence):
    # Remove all alphanumeric character and word that starts with @, #, and http
    # Also lower the case of sentence
    result1 = re.sub(r'http\S+|@(\w+)|#(\w+)|[^a-zA-Z0-9\-\+\s]', '', sentence).lower()
    result2 = re.sub(' +', ' ', result1).strip()
    return result2


def tokenize(sentence):
    # tokens = TweetTokenizer().tokenize(sentence)
    tokens = [token for token in sentence.split(" ") if token != ""]
    return tokens


def main():
    # Read tweet text data from SQL
    # For every tweet, main_process() get called
    # Return weighting data to be written to SQL
    pass


# Main process of system
def main_process(sentence):
    # Kalimat awal
    print(sentence, "\n")

    # Kalimat sudah melewati format awal
    formatted = format_word(sentence)
    print(formatted, "\n")

    # Tokenisasi kalimat menjadi list
    tokens = tokenize(formatted)
    print(tokens, "\n")

    # Formalisasi tiap token
    list_temp = []
    for token in tokens:
        # Perbandingan tiap token sebelum dan sesudah formalisasi
        formed_word = formalization.formalize(token)
        print("--------", token, "=", formed_word)
        list_temp.append(formed_word)

    # Hasil formalisasi
    formed_sentence = (' '.join(list_temp))
    print("\n", formed_sentence)


if __name__ == '__main__':
    main_process(sentence_example)
