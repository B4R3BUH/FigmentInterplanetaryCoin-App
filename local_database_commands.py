def local_updating(request, cur, conn, cursor, connection):
    if request == 'creating':
        cur.execute('''create table if not exists Data0(id integer,auto_auth integer,saved_user_id string,do_import integer)''')
        conn.commit()

    elif request == 'update_null':
        cur.execute('select id from Data0')
        sid = cur.fetchone()
        conn.commit()

        if sid is None or sid == '':
            cur.execute('insert into Data0(id,auto_auth,saved_user_id,do_import) values({},{},"{}",0)'.format(1, 0, ""))
            conn.commit()
        else:
            pass

    elif request == 'check_import':
        cur.execute('select do_import from Data0')
        di = cur.fetchone()
        di = di[0]
        conn.commit()
        if int(di) == 0:
            try:
                import os
                os.system('pip install kivy==2.3.0')
                os.system('pip install pymysql==1.1.1')
                os.system('pip install plyer==2.1.0')

                cur.execute('update Data0 set do_import=1')
                conn.commit()
            except:
                pass
        else:
            pass

    elif request == 'get_suid':
        cur.execute('select saved_user_id from Data0')
        suid = cur.fetchone()
        suid = suid[0]
        conn.commit()
        return suid