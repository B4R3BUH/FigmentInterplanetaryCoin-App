def check_got_gift(cursor, connection, suid, conn, cur):
    cursor.execute(f'select was_added_as_fren from Data where fic_id="{str(suid)}"')
    waaf = cursor.fetchone()
    waaf = waaf['was_added_as_fren']
    connection.commit()

    if waaf == 1:
        cursor.execute(f'select fren_got_gift from Data where fic_id="{str(suid)}"')
        fgg = cursor.fetchone()
        fgg = fgg['fren_got_gift']
        connection.commit()
        if fgg == 1:
            pass
        elif fgg == 0:
            cursor.execute(f'select user_id from Data where fic_id="{str(suid)}"')
            user_id = cursor.fetchone()
            user_id = user_id['user_id']
            connection.commit()

            cursor.execute(f'''SELECT user_id FROM Data WHERE FIND_IN_SET('{str(user_id)}', referrals) > 0;''')
            referral_id = cursor.fetchone()
            referral_id = referral_id['user_id']
            connection.commit()

            cursor.execute(f'select tokens, alltime_tokens, skin_11 from Data where user_id={referral_id}')
            tats11_1 = cursor.fetchone()
            tokens_db = tats11_1['tokens']
            alltime_tokens_db = tats11_1['alltime_tokens']
            skin_11_db = tats11_1['skin_11']
            connection.commit()

            cursor.execute(f'select tokens, alltime_tokens, skin_11 from Data where fic_id="{str(suid)}"')
            tats11_2 = cursor.fetchone()
            tokens_db_2 = tats11_2['tokens']
            alltime_tokens_db_2 = tats11_2['alltime_tokens']
            skin_11_db_2 = tats11_2['skin_11']
            connection.commit()

            cur.execute('select tokens, alltime_tokens from Data1')
            from_local = cur.fetchone()
            tokens_local_db_2 = from_local[0]
            tokens_local_db_2 = int(tokens_local_db_2)
            alltime_tokens_local_db_2 = from_local[1]
            alltime_tokens_local_db_2 = int(alltime_tokens_local_db_2)
            conn.commit()

            if skin_11_db == 0:
                cursor.execute(
                    f'update Data set tokens={tokens_db + 100000}, alltime_tokens={alltime_tokens_db + 100000}, skin_11=1 where user_id={referral_id}')
            else:
                cursor.execute(
                    f'update Data set tokens={tokens_db + 100000}, alltime_tokens={alltime_tokens_db + 100000} where user_id={referral_id}')
            connection.commit()

            if skin_11_db_2 == 0:
                cursor.execute(
                    f'update Data set tokens={tokens_db_2 + 100000}, alltime_tokens={alltime_tokens_db_2 + 100000}, skin_11=1 where fic_id="{str(suid)}"')
                cur.execute(f'update Data1 set tokens={tokens_local_db_2 + 100000}, alltime_tokens={alltime_tokens_local_db_2 + 100000}')
            else:
                cursor.execute(
                    f'update Data set tokens={tokens_db_2 + 100000}, alltime_tokens={alltime_tokens_db_2 + 100000} where fic_id="{str(suid)}"')
            conn.commit()
            connection.commit()

            cursor.execute(f'update Data set fren_got_gift=1 where fic_id="{str(suid)}"')
            connection.commit()