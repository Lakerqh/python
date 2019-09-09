import mysql.connector


def conn_test(id,name):
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    cursor = conn.cursor()
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')   
    cursor.execute('insert into user (id, name) values (%s, %s)', [id, name])

    conn.commit()

    cursor.execute('select * from user where id = %s', (id,))
    values = cursor.fetchall()
    cursor.close()
    return values
