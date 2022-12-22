from flask import Flask, render_template, render_template_string, request
import json
from os.path import exists

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
     
@app.route('/save',methods=["POST"])
def save():
    j=request.get_json()
    file=open("db-"+j["fn"]+".json","w",encoding="utf-8")
    file.write(json.dumps(j["data"]))
    file.close()    
    db={"saved":1}
    return json.dumps(db)

@app.route('/load',methods=["POST"])
def load():
    j=request.get_json()
    if exists("db-"+j["fn"]+".json"):
        file=open("db-"+j["fn"]+".json","r",encoding="utf-8")
        db=json.loads(file.read())
        file.close()
        db["loaded"]=1
    else:
        db={"loaded":0}
        
    return json.dumps(db)

if __name__=="__main__":
    app.run()
