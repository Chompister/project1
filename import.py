import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

i=0  # line counter

def main():
	i=0  # line counter
	f = open("books.csv")
	reader = csv.reader(f)
	for isbn, title, author, year in reader:
		if i > 0:
			db.execute("INSERT INTO p1_books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
				{"isbn": isbn, "title": title, "author": author, "year": year})
			print(f"{i} - Title: {title} - Author: {author} - {year}")
		i += 1
	db.commit()
	print(f"Added {i} books to table ´p1_project´.")

if __name__ == "__main__":
    main()
