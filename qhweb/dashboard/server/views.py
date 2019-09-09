# -*- coding: utf-8 -*-

from .resources import logic
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def home_page():
    if request.method == 'GET':  
        id = request.args.get('id')  
        name = request.args.get('name')
        home_data = logic.get_home(id,name)
        return home_data

@app.route('/books')
def books():
    books_data = logic.get_books()
    return books_data


@app.route('/books/<string:book_id>')
def book(book_id):
    book_data = logic.get_book(book_id)
    return book_data


@app.route('/students')
def students():
    students_data = logic.get_students()
    return students_data


@app.route('/student/<string:student_id>')
def student(student_id):
    student_data = logic.get_student(student_id)
    return student_data
