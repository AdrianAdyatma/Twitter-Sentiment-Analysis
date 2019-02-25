import stream_twitter
import mongo_to_sql
import credentials_var as cred


def stream(n):
    # KEYWORD LENGTH LIMIT PER TEXT = 32

    keyword = ["Joko Widodo", "jokowi"]
    limit = n
    stream_twitter.stream(keyword, limit)

    keyword = ["Prabowo Subianto", "prabowo"]
    limit = n
    stream_twitter.stream(keyword, limit)


if __name__ == '__main__':

    n = input("Jumlah stream per keyword : ")
    stream(int(n))

    # mongo_to_sql.mongo_to_sql(cred.find_all)
    mongo_to_sql.mongo_to_sql(cred.find_unprocessed)
