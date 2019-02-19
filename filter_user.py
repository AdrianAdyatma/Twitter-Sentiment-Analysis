import credentials_var as cred


def insert_location(coll):
    count = 1

    for element in list(coll):

        user_id = int(element['user']['id_str'])
        location = element['user']['location']
        #
        # try:
        #     sql = 'UPDATE tb_user SET user_location =' \
        #           '(%s) WHERE user_id = (%s)'
        #     val = (location, user_id)
        #     cred.sqlCursor.execute(sql, val)
        #     cred.sqlDb.commit()
        # except:
        #     print(user_id, "export user to sql error")
        # else:
        #     count += 1

        try:
            sql = 'UPDATE tb_tweet SET user_location =' \
                  '(%s) WHERE user_id = (%s)'
            val = (location, user_id)
            cred.sqlCursor.execute(sql, val)
            cred.sqlDb.commit()
        except:
            print(user_id, "export user to sql error")
        else:
            count += 1

    # Count data processed
    print(count)


insert_location(cred.find_all)
