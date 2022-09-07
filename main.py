from av import available
from flask import Flask, request, render_template
from db import init_db, insert_db, printa
import threading
#from mail import send_ok

db_name="meetings" #To be created if needed
init_db(db_name)#initiate DB

def insert_event():#Insert new meetings run in threading later for more efficiency
    insert_db(title,email,S_time,E_time,db_name)

app = Flask(__name__)
app.config['SECRET_KEY'] = '#$%^&*'

@app.route('/', methods=['GET','POST'])#home page
def index():
    return render_template('index.html')

@app.route("/app", methods=["POST"])# add or not a meeting
def use_app():
    global title,email,S_time,E_time
    r=request.form
    title,email,S_time,E_time=r["title"],r["email"],r["S_time"],r["E_time"]
    if available(S_time,E_time,db_name)==True:   
        threading.Thread(target=insert_event).start() 
        return render_template('ok.html')
    else :
        return render_template('pb.html')

@app.route("/av", methods=['GET','POST'])# availibilities page
def print_av():
    html=printa(db_name,'availibilities')
    return(html)

@app.route("/me", methods=['GET','POST'])# reservations page
def print_me():
    html=printa(db_name,'reservations')
    return(html)

if __name__ == '__main__': #launch app
    app.run(debug=True)
