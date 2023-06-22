from flask import Flask,render_template,url_for,request
import pandas as pd
import numpy as np
import pickle
import os 
from flask import send_from_directory
loaded_model=pickle.load(open('random_forest_model.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        t=float(request.form.get('T',False))
        tm=float(request.form['TM'])
        tmm=float(request.form['Tm'])
        slp=float(request.form['SLP'])
        h=float(request.form['H'])
        vv=float(request.form['VV'])
        v=float(request.form['V'])
        vm=float(request.form['VM'])

        data=np.array([[t,tm,tmm,slp,h,vv,v,vm]])
        pred=loaded_model.predict(data)
        return render_template('result.html',prediction=pred)

if __name__=="__main__":
    app.run(debug=True)
