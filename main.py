from nltk.tokenize import TweetTokenizer
# from nltk.tokenize import Tokenizer

test_sent = "Presiden Jok0 Widodo 2342348239237112413 mant4p @jokowi #2019gantibaju pada hari-hari ini bertemu dengan Bpk. Hj. Prabowo Subianto dan cipika cipiki dengan istri2nyaaa sebelum 7an!!! @pointer_ID https://t.co/Fys3PYcjlS"
test_sent = "RT @mumu_qyu: Yah...kesederhanaan adalah icon untuk kepribadian pak ...Jokowi.\n#IndonesiaYangBersyukur \n@erickthohir https://t.co/QDS9oI7sfv"

def test_token(sent):
    tokens = TweetTokenizer().tokenize(sent.lower())
    print(tokens)
    print(type(tokens))
    return tokens


test_token(test_sent)
