from flask import Flask , redirect , url_for , request , render_template , send_file , send_file
import csv , os
import heartdb


app = Flask(__name__)

UPLOAD_FOLDER = '/home/sepehr/Desktop/py/ie-project/csv-files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
nrpp = 50 # number of records per page
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
    save_csv(result)
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
    save_csv(result)
    return render_template('search.html',list = result , pagination = pagination , page = int(page) , qs = qs)

@app.route('/add-csv-file')
def add_csv_file(msg = None):
    return render_template('add-csv-file.html', msg=msg)  

@app.route('/create-record')
def create_record():
    return render_template('create.html')

@app.post("/delete_record/<id>")
def delete_record(id):
    heartdb.delete_heart(id)
    return redirect(url_for('search'))

@app.route('/update-record/<id>')
def update_record(id):
    record =  heartdb.find(id)
    return render_template('edit.html',record = record)

@app.route('/save-csv')
def save_csv():
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
    result  = heartdb.heart_list(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall, output)
    return save_csv(result)
######### Post Routes


@app.route("/update", methods=["POST"])
def update():
    id = request.form['id']
    record = {
            "age": request.form['age'],
            "sex": request.form['sex'],
            "cp": request.form['cp'],
            "trtbps": request.form['trtbps'],
            "chol": request.form['chol'],
            "fbs": request.form['fbs'],
            "restecg": request.form['restecg'],
            "thalachh": request.form['thalachh'],
            "exng": request.form['exng'],
            "oldpeak": request.form['oldpeak'],
            "slp": request.form['slp'],
            "caa": request.form['caa'],
            "thall": request.form['thall'],
            "output": request.form['output']
    }
    heartdb.update_heart(id,record)
    return redirect(url_for('search'))
@app.route("/store-record", methods=["POST"])
def store_record() :
    record = [
        [
            request.form['age'],
            request.form['sex'],
            request.form['cp'],
            request.form['trtbps'],
            request.form['chol'],
            request.form['fbs'],
            request.form['restecg'],
            request.form['thalachh'],
            request.form['exng'],
            request.form['oldpeak'],
            request.form['slp'],
            request.form['caa'],
            request.form['thall'],
            request.form['output']
        ]
    ]
    heartdb.insert_heart(record)
    return redirect(url_for('index'))





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
   
   
def save_csv(list1):
    result = [list(d.values()) for d in list1]
    with open("save-data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id","age","sex","cp","trtbps","chol","fbs","restecg","thalachh","exng","oldpeak","slp","caa","thall","output"])
        for r in result : 
            writer.writerow(r)
    return send_file('save-data.csv', as_attachment=True, download_name='heart.csv')

   
   
   
   
   
   
   
   
   
    

@app.route('/static/style.css')
def style():
  return send_file("static/style.css")
@app.route('/static/font.ttf')
def font():
  return send_file("static/Pinar-SemiBold.ttf") 



if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=6600,debug=True)
    
    