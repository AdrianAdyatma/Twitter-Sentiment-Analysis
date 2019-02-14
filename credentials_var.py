import pymongo
import mysql.connector


# MySQL Database identifier & connection
sql_db_name = "tweets_db"
sqlDb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database=sql_db_name
)
sqlCursor = sqlDb.cursor()

# MongoDB Database identifier & connection
client = pymongo.MongoClient('localhost', 27017)
TwitterDB = client.TwitterDB

tweets = TwitterDB.tweets
findall_tweets = tweets.find()

