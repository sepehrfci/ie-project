from flask import Flask , redirect , url_for , request , render_template , send_file
import csv , os
import showsdb


app = Flask(__name__)

UPLOAD_FOLDER = '/home/sepehr/Desktop/py/ie-project/csv-files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
nrpp = 100 # number of records per page
#########  Get routes

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search')
def search():
    pagination = showsdb.page_count(nrpp=nrpp)
    return render_template('search.html',list = showsdb.read_shows(page=1,nrpp=nrpp) , pagination = pagination , page = 1)
@app.route('/search/page/<page>')
def search_page (page):
    pagination = showsdb.page_count(nrpp=nrpp)
    return render_template('search.html',list = showsdb.read_shows(page=page,nrpp=nrpp) , pagination = pagination , page = int(page))

@app.route('/add-csv-file')
def add_csv_file(msg = None):
    return render_template('add-csv-file.html', msg=msg)  


@app.route('/log')
def log(msg = None):
    return msg  
######### Post Routes

@app.route("/upload-csv-file", methods=["POST"])
def upload_csv_file():
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for(add_csv_file(msg="نیومده")))
    file.save(file.filename)
    data = []
    with open(file.filename, "r") as f:
        reader = csv.reader(f)
        id = 0
        for row in reader:
            if id == 0 : 
                id+=1   
                continue
            data.append(row)
            # id+=1
    #create_show_table()
    #return data
    # showsdb.drop_shows_table()
    showsdb.create_show_table()
    show = showsdb.insert_shows(data)
    return data
    # return redirect(url_for(add_csv_file(msg="فایل مورد نظر با موفقیت آپلود و داده ها اضافه شد.")))
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



if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=6600,debug=True)
    
    