import mysql.connector


def conn_test(id,name):
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    cursor = conn.cursor()
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))') 
    cursor.execute('select * from user')
    valall = cursor.fetchall()
    print('全部数据',type(valall))
    defalltId = valall[-1]
    addid = int(defalltId[0]) + 1
    print('生成的id',addid)

    
    cursor.execute('insert into user (id, name) values (%s, %s)', [addid,name])

    conn.commit()

    cursor.execute('select * from user where id = %s', (id,))
    values = cursor.fetchall()
    cursor.close()
    return values
