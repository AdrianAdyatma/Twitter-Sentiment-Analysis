import credentials_var as cred

count = 0

list_results = list(cred.raw_findAll)
for element in list_results:
    try:
        if element["truncated"] is False:
            text = element["text"]
            print(element["text"], "\n=============")
            print("1")
        elif element["truncated"] is True:
            text = element["extended_tweet"]["full_text"]
            print(element["extended_tweet"]["full_text"], "\n=============")
            print("2")
        #     sql = "INSERT INTO tabelmantap (id_str, text) VALUES (%s, %s)"
        # val = (element["id_str"], text)
        # cred.sqlCursor.execute(sql, val)
        #
        # # Commit all changes to sql
        # cred.sqlDb.commit()
    except:
        print(element["id_str"], "export to sql error")
    else:
        print(element["id_str"], "export to sql success")
        count += 1

print(count, "data exported to sql")
