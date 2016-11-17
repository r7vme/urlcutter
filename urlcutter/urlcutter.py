import sys
import sqlite3
from flask import Flask
from flask import request
from flask import redirect
from flask import g
from flask import render_template

import encoder


if len(sys.argv) > 1:
    DATABASE = sys.argv[1]
else:
    # TODO: Check if file exists
    DATABASE = 'db.sqlite'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def handle_index_page():
    return render_template('index.html')

@app.route("/<url>")
def handle_redirect_to(url):
    # Decode url to integer
    url_id = encoder.base_decode(url)

    # Grab original url from database
    cur = get_db().execute("SELECT url FROM urlcutter WHERE id=?", [url_id])
    rv = cur.fetchone()
    cur.close()

    # Redirect to original url if in database
    if rv is not None:
        orig_url = rv[0]
        return redirect(orig_url, code=301)
    else:
        return "Not found", 404

@app.route("/urlcutter", methods=["POST"])
def handle_urlcutter():
    # Dump filtering
    if not request.form['url'].startswith("http"):
        return "Error: URL should start with 'http'", 400

    # Add url to db
    db = get_db()
    with db:
        cur = db.cursor()
        cur.execute("INSERT INTO urlcutter VALUES (NULL, ?)", (request.form['url'],))
        cur.execute("SELECT last_insert_rowid()")
        rv = cur.fetchone()

    # Get url_id
    url_id = rv[0]
    # Encode url_id with Base58
    return request.url_root + encoder.base_encode(url_id)

if __name__ == "__main__":
    # Run with debug from CLI
    app.config["DEBUG"] = True

    # Run application
    app.run(host='0.0.0.0')
