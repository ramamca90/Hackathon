# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:35:37 2017

@author: user
"""

#!/usr/bin/python
from flask import Flask ,render_template,request,url_for
import os

import pandas as pd

loadboard = pd.read_excel("C:\\Users\\user\\Desktop\\loadBoard.xlsx")
Weatherandroadcondition =pd.read_excel("C:\\Users\\user\\Desktop\\dr.xlsx")

print (Weatherandroadcondition)
pickup_points_list=loadboard.PICKUP.unique()
deliver_points=loadboard.DELIVERY.unique()
MATERIALTYPE=loadboard.MATERIAL.unique()


CITY_fetched=Weatherandroadcondition.PLACE.unique()


app= Flask(__name__)
 
@app.route('/xpologistics/' )
def xpologistics():
      return render_template("profile.html")

@app.route('/loadboard/' , methods = ['GET','POST']  )
def checking():
     return render_template('loadboard.html',pickup_point=pickup_points_list,
                            drop_point=deliver_points,MATERIALTYPE=MATERIALTYPE)
    
@app.route('/lbdata' , methods = ['GET','POST']  )
def displayloadbaord():
     pickedpoint = request.form.get('pickup_points')
     deliveredpoint = request.form.get('drop_point')
     MATERIALTYPE = request.form.get('MATERIALTYPE')
     print (pickedpoint,deliveredpoint)
     j=loadboard[(loadboard['PICKUP'] == pickedpoint) & (loadboard['DELIVERY'] == deliveredpoint) &  (loadboard['MATERIAL'] == MATERIALTYPE)]
     #return pickedpoint
     return render_template('displayloadboard.html',loaddata=[j.to_html(classes='j')])    

@app.route('/HelpDesk' , methods = ['GET','POST'])
def weatheranalysis():
    return render_template('weatherprediction.html',city=CITY_fetched)

@app.route('/Weatherdata',  methods = ['GET','POST'])
def outputweather():
    CITY_fetched=request.form.get('CITY')
    k=Weatherandroadcondition.PLACE[Weatherandroadcondition.PLACE==CITY_fetched]
    return render_template('output.html',p=k)
    


if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True )