import sqlite3
from flask import Flask , redirect , url_for

def drop_shows_table():
    connection = sqlite3.connect("shows.db")
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS shows
    """)
    connection.close()



def create_show_table():
    connection = sqlite3.connect("shows.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE shows (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            show_id TEXT,
            type TEXT,
            title TEXT,
            director TEXT,
            cast TEXT,
            country TEXT,
            date_added TEXT,
            release_year TEXT,
            rating TEXT,
            duration TEXT,
            listed_in TEXT,
            description TEXT
        )
    """)
    connection.close()



def insert_shows(shows_list):
    connection = sqlite3.connect("shows.db")
    cursor = connection.cursor()
    for show in shows_list:
        cursor.execute("""
            INSERT INTO shows (
                show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        """, (
            show[0], show[1], show[2], show[3], show[4], show[5], show[6],
            show[7], show[8], show[9], show[10], show[11]
        ))
    connection.commit()
    connection.close()

def read_shows(page,nrpp):
    offset = (int(page) - 1) * nrpp
    connection = sqlite3.connect("shows.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM shows LIMIT {nrpp} OFFSET {str(offset)}")
    # تبدیل داده ها به لیست
    shows_list = []
    for row in cursor:
        shows_list.append({
            "id": row[0],
            "show_id": row[1],
            "type": row[2],
            "title": row[3],
            "director": row[4],
            "cast": row[5],
            "country": row[6],
            "date_added": row[7],
            "release_year": row[8],
            "rating": row[9],
            "duration": row[10],
            "listed_in": row[11],
            "description": row[12],
        })
    connection.close()
    return shows_list


def page_count(nrpp):
    connection = sqlite3.connect("shows.db")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM shows")
    count = cursor.fetchone()[0]
    connection.close()

    return int(count / nrpp) +1