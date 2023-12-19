from flask import Flask , redirect , url_for , request , render_template , send_file
import csv , os
import sqlite3


app = Flask(__name__)

UPLOAD_FOLDER = '/home/sepehr/Desktop/py/ie-project/csv-files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#########  Get routes

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/add-csv-file')
def add_csv_file(msg = None):
    return render_template('add-csv-file.html', msg=msg)  

######### Post Routes

@app.route("/upload-csv-file", methods=["POST"])
def upload_csv_file():
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for(add_csv_file(msg="نیومده")))
    file.save(file.filename)
    data = {}
    with open(file.filename, "r") as f:
        reader = csv.reader(f)
        id = 0
        for row in reader:
            data[id] = row
            id+=1
    create_show_table()
    return data
    return redirect(url_for(add_csv_file(msg="فایل مورد نظر با موفقیت آپلود و داده ها اضافه شد.")))
    # file = request.files.get("file")
    # with open(file.filename, "r") as f:
    #     reader = csv.reader(f)

    # data = {}
    # for row in reader:
    #     data[row[0]] = row[1]
    # return data
   
   
   
   
   
   
   
   
   
   
   
   
    

@app.route('/static/style.css')
def style():
  return send_file("static/style.css")
@app.route('/static/font.ttf')
def font():
  return send_file("static/Pinar-SemiBold.ttf") 
    
# class user :
#     def __init__(self,username,serverName,password,expirationDate) :
#         self.username = username
#         self.serverName = serverName
#         self.password = password
#         self.expirationDate = expirationDate
#     def __iter__(self) :
#         return iter([self.username,self.serverName,self.password,self.expirationDate])




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
            release_year INTEGER,
            rating REAL,
            duration INTEGER,
            listed_in TEXT,
            description TEXT
        )
    """)
    connection.close()





if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=6600,debug=True)
    
    