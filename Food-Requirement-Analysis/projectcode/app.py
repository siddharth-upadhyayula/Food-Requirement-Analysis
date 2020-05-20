# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:59:01 2020

@author: mamas
"""

from flask import Flask,render_template,request

import pickle
import numpy as np

model=pickle.load(open('num_orders.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    base_price=request.form['base_price']
    Dishes=request.form['Dishes']
    if(Dishes=="Beverages"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=1,0,0,0,0,0,0,0,0,0,0,0,0,0
    if(Dishes=="Extras"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,1,0,0,0,0,0,0,0,0,0,0
    if(Dishes=="Soup"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,0,0,0,1,0
    if(Dishes=="Other Snacks"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,1,0,0,0,0,0,0,0,0
    if(Dishes=="Salad"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,1,0,0,0,0
    if(Dishes=="Rice Bowl"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,1,0,0,0,0,0
    if(Dishes=="Starters"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,0,0,0,0,1
    if(Dishes=="Sandwich"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,0,1,0,0,0
    if(Dishes=="Pasta"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,1,0,0,0,0,0,0,0
    if(Dishes=="Desert"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,1,0,0,0,0,0,0,0,0,0,0,0
    if(Dishes=="Biryani"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,1,0,0,0,0,0,0,0,0,0,0,0,0
    if(Dishes=="Pizza"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,1,0,0,0,0,0,0
    if(Dishes=="Fish"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,1,0,0,0,0,0,0,0,0,0
    if(Dishes=="Sea Food"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,0,0,1,0,0
        
        
        
    checkout_price=request.form['checkout_price']
    
    city_code=request.form['city_code']
    
    cuisine=request.form['cuisine']
    if(cuisine=="continental"):
        b1,b2,b3,b4=1,0,0,0
    if(cuisine=="Indian"):
        b1,b2,b3,b4=0,1,0,0
    if(cuisine=="Italian"):
        b1,b2,b3,b4=0,0,1,0
    if(cuisine=="thai"):
        b1,b2,b3,b4=0,0,0,1
        
        
    id=request.form['id']    
    meal_id=request.form['meal_id']
    
    total=[[float(base_price),s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,float(checkout_price),int(city_code),b1,b2,b3,b4,int(id),int(meal_id)]]
    y_pred=model.predict(np.array(total))
    
    print(y_pred)
    
    return render_template("index.html",showcase="num_orders is:"+str(y_pred))


if __name__=='__main__':
    app.run(debug=True)
    
        
    
    
