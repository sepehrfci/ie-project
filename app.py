from flask import Flask , redirect , url_for , request , render_template , send_file
import csv , os
import heartdb


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
    qs = request.query_string.decode()
    age = request.args.get('age')
    sex = request.args.get('sex')
    cp = request.args.get('cp')
    trtbps = request.args.get('trtbps')
    chol = request.args.get('chol')
    fbs = request.args.get('fbs')
    restecg = request.args.get('restecg')
    thalachh = request.args.get('thalachh')
    exng = request.args.get('exng')
    oldpeak = request.args.get('oldpeak')
    slp = request.args.get('slp')
    caa = request.args.get('caa')
    thall = request.args.get('thall')
    output = request.args.get('output')
    result  = heartdb.search_heart_data(1,nrpp,age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall, output)
    pagination = heartdb.page_count(nrpp,age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall, output)
    return render_template('search.html',list = result , pagination = pagination , page = 1 , qs = qs)
@app.route('/search/page/<page>')
def search_page (page):
    qs = request.query_string.decode()
    age = request.args.get('age')
    sex = request.args.get('sex')
    cp = request.args.get('cp')
    trtbps = request.args.get('trtbps')
    chol = request.args.get('chol')
    fbs = request.args.get('fbs')
    restecg = request.args.get('restecg')
    thalachh = request.args.get('thalachh')
    exng = request.args.get('exng')
    oldpeak = request.args.get('oldpeak')
    slp = request.args.get('slp')
    caa = request.args.get('caa')
    thall = request.args.get('thall')
    output = request.args.get('output')
    result  = heartdb.search_heart_data(page,nrpp,age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall, output)
    pagination = heartdb.page_count(nrpp,age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall, output)
    return render_template('search.html',list = result , pagination = pagination , page = int(page) , qs = qs)

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
    heartdb.drop_heart_table()
    heartdb.create_heart_table()
    show = heartdb.insert_heart(data)
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
    
    