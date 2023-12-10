from flask import Flask , redirect , url_for , request , render_template , send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/add-csv-file')
def add_csv_file():
    return render_template('add-csv-file.html')  



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


if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=6600,debug=True)
    
    