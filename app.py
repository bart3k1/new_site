import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://postgres:xxx@localhost:5432/artykuly')
# engine = create_engine(os.getenv("PSQL_MYDB_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    articles = db.execute("SELECT * FROM articles").fetchall()
    return render_template("index.html", articles=articles)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.form.getlist("file_list[]")
        for i in f:
            for line in i:
                print(line)
        return 'file uploaded successfully'

    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        for line in f:
            print(line)
        f.close()
        return 'file uploaded successfully'
