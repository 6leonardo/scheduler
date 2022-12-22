from flask import Flask, render_template, render_template_string, request
import json
import os
from os.path import exists
import glob

app=Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')
     
@app.route('/api/save',methods=["POST"])
def save():
    j=request.get_json()
    file=open("db-"+j["fn"]+".json","w",encoding="utf-8")
    file.write(json.dumps(j["data"]))
    file.close()    
    db={"saved":1}
    return json.dumps(db)

@app.route('/api/load',methods=["POST"])
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

@app.route('/api/list',methods=["POST"])
def list():
    txtfiles = []
    for file in glob.glob("db-*.json"):
        txtfiles.append(file.replace(".json","").replace("db-",""))
        
    db={"dbs":txtfiles}
        
    return json.dumps(db)

@app.route('/api/delete',methods=["POST"])
def delete():
    j=request.get_json()
    os.remove(j["fn"])
    db={"done":1}
        
    return json.dumps(db)

@app.route('/api/running',methods=["POST"])
def running():
    j=request.get_json()
    if j["op"]=="save":
        running={"running":j["running"]}
        file=open("running.json","w",encoding="utf-8")
        file.write(json.dumps(running))
        file.close()
    else:
        file=open("running.json","r",encoding="utf-8")
        running=json.loads(file.read())
        file.close()

    return json.dumps(running)


if __name__=="__main__":
    app.run()
