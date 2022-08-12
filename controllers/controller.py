from flask import Flask, render_template, request, redirect
from app import app
from models.book import *
from models.books import add_new_book, delete_book_by_urn, check_book_in_or_out, books


@app.route('/')
def home():
    return '<p>Home</p>'


@app.route('/books')
def index():
    return render_template('index.html', title="Home", books=books)


@app.route('/books/<urn>')
def show_book(urn):
    book_to_show = []
    for book in books:
        if book.urn == urn:
            book_to_show = book
    return render_template("show.html", title="Book Detail", book=book_to_show)


@app.route('/books/new')
def new():
    return render_template('new.html')


@app.route('/books', methods=["POST"])
def create():
    title = request.form['title']
    title_urn = title.replace(" ", "_")
    author = request.form['author']
    author_urn = author.replace(" ", "_")
    urn = title_urn + "_" + author_urn
    genre = request.form['genre']
    description = request.form['description']
    checked_out = request.form['checked_out']
    cover_url = request.form['cover_url']
    new_book = Book(title, description, author, genre,
                    checked_out, cover_url, urn)
    add_new_book(new_book)
    redirect_url = f'/books/{urn}'
    return redirect(redirect_url)


@app.route('/books/delete/<urn>', methods=["POST"])
def delete(urn):
    delete_book_by_urn(urn)
    return redirect('/books')


@app.route('/books/checkin_out/<urn>', methods=["POST"])
def check_in_out(urn):
    check_book_in_or_out(urn)
    redirect_url = f'/books/{urn}'
    return redirect(redirect_url)
