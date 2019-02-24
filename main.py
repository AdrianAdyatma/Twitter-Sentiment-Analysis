import stream_twitter
import mongo_to_sql
import credentials_var as cred

if __name__ == '__main__':
    # KEYWORD LENGTH LIMIT PER TEXT = 32

    # keyword = ["Joko Widodo", "jokowi", "@jokowi"]
    # limit = 1
    # stream_twitter.stream(keyword, limit)
    #
    # keyword = ["Prabowo Subianto", "prabowo", "@prabowo"]
    # limit = 1
    # stream_twitter.stream(keyword, limit)

    mongo_to_sql.mongo_to_sql(cred.find_unprocessed)
