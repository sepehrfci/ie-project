from flask import Flask , redirect , url_for , request , render_template , send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/css/style.css')
def style():
  return send_file("static/style.css")
    
    
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
    
    