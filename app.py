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

