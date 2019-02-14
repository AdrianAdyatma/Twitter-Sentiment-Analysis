import stream_twitter
import mongo_to_sql
import credentials_var as cred

if __name__ == '__main__':
    keyword = ["Joko Widodo", "jokowi", "@jokowi"]
    limit = 250
    stream_twitter.stream(keyword, limit)

    keyword = ["Prabowo Subianto", "prabowo", "@jokowi"]
    limit = 250
    stream_twitter.stream(keyword, limit)

    mongo_to_sql.mongo_to_sql(cred.findall_tweets)
