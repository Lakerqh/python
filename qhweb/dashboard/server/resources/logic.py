from .. import utils


def register_user(username, password):
    conndata = utils.comm_register(username, password)
    return conndata

def login_user(username, password):
    conndata = utils.comm_login(username, password)
    return conndata


def get_home(id, name):
    home_data = utils.conn_test(id, name)
    data = {
        'user': home_data
    }
    return data


def get_books():
    return 'list of books basic info'


def get_book(book_id):
    return 'detailed info of book :{}'.format(book_id)


def get_students():
    return 'list of students basic info'


def get_student(student_id):
    return 'detailed info of student:{}'.format(student_id)
