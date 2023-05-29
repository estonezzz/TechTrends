import sqlite3
import logging
from datetime import datetime
from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # captures all levels, DEBUG and above

# Define a variable for db connection count
db_connection_count = 0


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    global db_connection_count
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    db_connection_count += 1
    return connection


# Function to get a post using its ID
def get_post(post_id):
    with get_db_connection() as connection:
        post = connection.execute('SELECT * FROM posts WHERE id = ?',
                                  (post_id,)).fetchone()
    return post


# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# Define the main route of the web application
@app.route('/')
def index():
    with get_db_connection() as connection:
        posts = connection.execute('SELECT * FROM posts').fetchall()
    logging.info(f'{datetime.now()}, Homepage retrieved!')
    return render_template('index.html', posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        logging.info(f'{datetime.now()}, Non-existing article accessed, returned 404.')
        return render_template('404.html'), 404
    else:
        logging.info('{}, Article "{}" retrieved!'.format(datetime.now(), post['title']))
        return render_template('post.html', post=post)


# Define the About Us page
@app.route('/about')
def about():
    logging.info(f'{datetime.now()}, "About Us" page retrieved!')
    return render_template('about.html')


# Define the post creation functionality
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            with get_db_connection() as connection:
                connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                                   (title, content))
                connection.commit()
            logging.info('{}, A new article titled "{}" created!'.format(datetime.now(), title))
            return redirect(url_for('index'))

    return render_template('create.html')


# Define the healthcheck route of the web application
@app.route('/healthz')
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    return response


# Define the metrics route of the web application
@app.route('/metrics')
def metrics():
    global db_connection_count
    post_count = 0
    try:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM posts')
            posts = cursor.fetchall()
            post_count = len(posts)
            db_connection_count += 1
    except sqlite3.Error as e:
        print(e)

    response = app.response_class(
        response=json.dumps({"db_connection_count": db_connection_count, "post_count": post_count}),
        status=200,
        mimetype='application/json'
    )
    return response


# start the application on port 3111
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3111')
