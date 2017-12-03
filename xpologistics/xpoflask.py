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
pickup_points_list=loadboard.PICKUP.unique()
deliver_points=loadboard.DELIVERY.unique()




app= Flask(__name__)
 
@app.route('/xpologistics/' )
def xpologistics():
      return render_template("profile.html")

@app.route('/loadboard/' , methods = ['GET','POST']  )
def checking():
     return render_template('loadboard.html',pickup_point=pickup_points_list,
                            drop_point=deliver_points)
    
@app.route('/lbdata' , methods = ['GET','POST']  )
def displayloadbaord():
     pickedpoint = request.form.get('pickup_points')
     deliveredpoint = request.form.get('drop_point')
     print (pickedpoint,deliveredpoint)
     j=loadboard[(loadboard['PICKUP'] == pickedpoint) & (loadboard['DELIVERY'] == deliveredpoint)]
     #return pickedpoint
     return render_template('displayloadboard.html',loaddata=[j.to_html(classes='j')])    
 

if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True )