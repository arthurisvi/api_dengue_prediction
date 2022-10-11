from flask import Flask, request
import pickle
import json

app = Flask(__name__)

@app.route('/send-form',methods=['POST'])
def createTask():
        
    with open("model_dt.sav", "rb") as f:
        clf = pickle.load(f)
        
    form = request.get_json()
        
    model_exit = clf.predict([[
        form['cs_sexo'], 
        form['febre'], 
        form['mialgia'], 
        form['cefaleia'], 
        form['exantema'],
        form['vomito'],
        form['nausea'], 
        form['dor_costas'], 
        form['astralgia'], 
        form['dor_retro'],
        form['leucopenia'], 
        form['petequia_n']       
        ]])[0]
    
    model_probability = clf.predict_proba([[
        form['cs_sexo'], 
        form['febre'], 
        form['mialgia'], 
        form['cefaleia'], 
        form['exantema'],
        form['vomito'],
        form['nausea'], 
        form['dor_costas'], 
        form['astralgia'], 
        form['dor_retro'],
        form['leucopenia'], 
        form['petequia_n']       
        ]])[0]
    
    response = {
        "exit": int(model_exit),
        "positive_probability": float(model_probability[1]),
        "negative_probability": float(model_probability[0])
    }
    
    return json.dumps(response)
