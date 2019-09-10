import mysql.connector

def comm_register(username, password):
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    cursor = conn.cursor()
    cursor.execute('select * from user')

    valall = cursor.fetchall()
    for i in valall:
        if(i[1] == username):
            data = {
                'msg':'改用户名已注册',
                'code':'0'
            }
            return data
       
    defalltId = valall[-1]
    addid = int(defalltId[0]) + 1
    cursor.execute('insert into user (id, username, password) values (%s, %s, %s)', [addid,username,password])
    conn.commit()
    cursor.close()
    data = {
        'msg':'注册成功',
        'code': '1'
    }
    return data

def comm_login(username, password):
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    cursor = conn.cursor()
    cursor.execute('select * from user')
    valall = cursor.fetchall()
    for i in valall:
        if(username in i[1] and password in i[2]):
            data = {
                    'msg':'登录成功',
                    'code':'1'
                }
            return data
    
    data = {
            'msg':'账号密码不正确',
            'code':'0'
        }
    cursor.close()
    return data


def conn_test(id,name):
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    cursor = conn.cursor()
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))') 
    cursor.execute('select * from user')
    valall = cursor.fetchall()
    print('全部数据',type(valall))
    defalltId = valall[-1]
    print('一条',type(defalltId))
    addid = int(defalltId[0]) + 1
    print('生成的id',addid)

    
    cursor.execute('insert into user (id, name) values (%s, %s)', [addid,name])

    conn.commit()

    cursor.execute('select * from user where id = %s', (id,))
    values = cursor.fetchall()
    cursor.close()
    return values


