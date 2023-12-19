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
        # return redirect(url_for('log',msg = show))
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

def read_shows():
    connection = sqlite3.connect("shows.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description
        FROM shows
    """)

    # تبدیل داده ها به لیست
    shows_list = []
    for row in cursor:
        shows_list.append({
            "show_id": row[0],
            "type": row[1],
            "title": row[2],
            "director": row[3],
            "cast": row[4],
            "country": row[5],
            "date_added": row[6],
            "release_year": row[7],
            "rating": row[8],
            "duration": row[9],
            "listed_in": row[10],
            "description": row[11],
        })

    # بستن اتصال
    connection.close()

    return shows_list
