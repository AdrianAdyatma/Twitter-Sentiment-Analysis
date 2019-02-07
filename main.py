from nltk.tokenize import TweetTokenizer
import re

import formalization

test_sent = "Presiden Jok0 Widodo mnt4p @jokowi #Jokowi2Periode pada hari-hari ini bertemu dengan Bpk. Hj. Prabowo Subianto dan cipika cipiki dengan istri2nyaaa sebelum 7an!!! @pointer_ID https://t.co/Fys3PYcjlS"
# test_sent = "RT @mumu_qyu: Yah...kesederhanaan adalah icon untuk kepribadian pak ...Jokowi.\n#IndonesiaYangBersyukur \n@erickthohir https://t.co/QDS9oI7sfv"

# !!!!!!!!!!!!!!!!!!!
def delSpecWord(sentence):
    result = re.sub(r'http\S+|@(\w+)|#(\w+)', '', sentence)
    return result.strip()

def test_token(sent):
    tokens = TweetTokenizer().tokenize(sent.lower())
    return tokens

list_temp = []
for word in test_token(test_sent):
    list_temp.append(formalization.formalize(word))
    print(list_temp)

sentence = delSpecWord(' '.join(list_temp))

print(test_sent)
print(sentence)
