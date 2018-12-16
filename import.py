import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:xxx@localhost:5432/artykuly')
# engine = create_engine(os.getenv("PSQL_MYDB_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("spis.csv")
    reader = csv.reader(f)
    for title, translation, file in reader:
        db.execute("INSERT INTO articles (title, translation, file) VALUES (:title, :translation, :file)",
                   {"title": title, "translation": translation, "file": file})
        # print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()


if __name__ == "__main__":
    main()
