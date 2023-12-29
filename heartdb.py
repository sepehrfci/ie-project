import sqlite3
from flask import Flask , redirect , url_for

def drop_heart_table():
    connection = sqlite3.connect("heart.db")
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS heart
    """)
    connection.close()



def create_heart_table():
    connection = sqlite3.connect("heart.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE heart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            sex INTEGER,
            cp INTEGER,
            trtbps INTEGER,
            chol INTEGER,
            fbs INTEGER,
            restecg INTEGER,
            thalachh INTEGER,
            exng INTEGER,
            oldpeak INTEGER,
            slp INTEGER,
            caa INTEGER,
            thall INTEGER,
            output INTEGER
        )
    """)
    connection.close()



def insert_heart(heart_list):
    connection = sqlite3.connect("heart.db")
    cursor = connection.cursor()
    for heart in heart_list:
        cursor.execute("""
            INSERT INTO heart (
                age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa , thall , output
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?
            )
        """, (
            heart[0], heart[1], heart[2], heart[3], heart[4], heart[5], heart[6],
            heart[7], heart[8], heart[9], heart[10], heart[11],heart[12], heart[13]
        ))
    connection.commit()
    connection.close()

def read_heart(page,nrpp):
    offset = (int(page) - 1) * nrpp
    connection = sqlite3.connect("heart.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM heart LIMIT {nrpp} OFFSET {str(offset)}")
    # تبدیل داده ها به لیست
    heart_list = []
    for row in cursor:
        heart_list.append({
            "id": row[0],
            "age": row[1],
            "sex": row[2],
            "cp": row[3],
            "trtbps": row[4],
            "chol": row[5],
            "fbs": row[6],
            "restecg": row[7],
            "thalachh": row[8],
            "exng": row[9],
            "oldpeak": row[10],
            "slp": row[11],
            "caa": row[12],
            "thall": row[13],
            "output": row[14],
        })
    connection.close()
    return heart_list


def page_count(nrpp,age=None, sex=None, cp=None, trtbps=None, chol=None, fbs=None, restecg=None, thalachh=None, exng=None, oldpeak=None, slp=None, caa=None, thall=None, output=None):
    conn = sqlite3.connect('heart.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM heart WHERE " 
    conditions = []

    if age:
        conditions.append(f"age = {age}")
    if sex :
        conditions.append(f"sex = '{sex}'")
    if cp:
        conditions.append(f"cp = {cp}")
    if trtbps:
        conditions.append(f"trtbps = {trtbps}")
    if chol:
        conditions.append(f"chol = '{chol}'")
    if fbs:
        conditions.append(f"fbs = {fbs}")
    if restecg:
        conditions.append(f"restecg = {restecg}")
    if thalachh:
        conditions.append(f"thalachh = '{thalachh}'")
    if exng:
        conditions.append(f"exng = {exng}")
    if oldpeak:
        conditions.append(f"oldpeak = {oldpeak}")
    if slp:
        conditions.append(f"slp = '{slp}'")
    if caa:
        conditions.append(f"caa = {caa}")
    if thall:
        conditions.append(f"thall = '{thall}'")
    if output:
        conditions.append(f"output = {output}")

    if not conditions:
        sql = "SELECT * FROM heart"
    else:
        sql += " AND  ".join(conditions)
    cursor.execute(sql)
    heart_list = []
    for row in cursor:
        heart_list.append({
            "id": row[0],
            "age": row[1],
            "sex": row[2],
            "cp": row[3],
            "trtbps": row[4],
            "chol": row[5],
            "fbs": row[6],
            "restecg": row[7],
            "thalachh": row[8],
            "exng": row[9],
            "oldpeak": row[10],
            "slp": row[11],
            "caa": row[12],
            "thall": row[13],
            "output": row[14],
        })
    conn.close()

    return int(len(heart_list) / nrpp +1 )


def search_heart_data(page,nrpp,age=None, sex=None, cp=None, trtbps=None, chol=None, fbs=None, restecg=None, thalachh=None, exng=None, oldpeak=None, slp=None, caa=None, thall=None, output=None):
    offset = (int(page) - 1) * nrpp
    conn = sqlite3.connect('heart.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM heart WHERE " 
    conditions = []

    if age:
        conditions.append(f"age = {age}")
    if sex :
        conditions.append(f"sex = '{sex}'")
    if cp:
        conditions.append(f"cp = {cp}")
    if trtbps:
        conditions.append(f"trtbps = {trtbps}")
    if chol:
        conditions.append(f"chol = '{chol}'")
    if fbs:
        conditions.append(f"fbs = {fbs}")
    if restecg:
        conditions.append(f"restecg = {restecg}")
    if thalachh:
        conditions.append(f"thalachh = '{thalachh}'")
    if exng:
        conditions.append(f"exng = {exng}")
    if oldpeak:
        conditions.append(f"oldpeak = {oldpeak}")
    if slp:
        conditions.append(f"slp = '{slp}'")
    if caa:
        conditions.append(f"caa = {caa}")
    if thall:
        conditions.append(f"thall = '{thall}'")
    if output:
        conditions.append(f"output = {output}")

    if not conditions:
        sql = "SELECT * FROM heart"
    else:
        sql += " AND  ".join(conditions)
    sql += f" LIMIT {nrpp} OFFSET {str(offset)}"
    cursor.execute(sql)
    heart_list = []
    for row in cursor:
        heart_list.append({
            "id": row[0],
            "age": row[1],
            "sex": row[2],
            "cp": row[3],
            "trtbps": row[4],
            "chol": row[5],
            "fbs": row[6],
            "restecg": row[7],
            "thalachh": row[8],
            "exng": row[9],
            "oldpeak": row[10],
            "slp": row[11],
            "caa": row[12],
            "thall": row[13],
            "output": row[14],
        })
    conn.close()

    return heart_list


# heartdb.read_heart(page=1,nrpp=nrpp)
