from nltk.tokenize import TweetTokenizer
import re

import formalization

sentence_example = "Presiden Jok0 Widodo mnt4p @jokowi #Jokowi2Periode pada hari-hari ini bertemu dengan Bpk. Hj. Prabowo Subianto dan cipika cipiki dengan istri2nyaaa sebelum 7an!!! @pointer_ID https://t.co/Fys3PYcjlS"


def delSpecWord(sentence):
    result = re.sub(r'http\S+|@(\w+)|#(\w+)', '', sentence)
    return result.strip()


def tokenize(sentence):
    tokens = TweetTokenizer().tokenize(sentence.lower())
    return tokens


list_temp = []
for word in tokenize(sentence_example):
    list_temp.append(formalization.formalize(word))
    print(list_temp)

sentence = delSpecWord(' '.join(list_temp))

print(sentence_example)
print(sentence)
