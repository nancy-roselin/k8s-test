from flask import Flask,render_template,request
#from werkzeug.wrappers import request
import model as m
#tds=[]

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def first():   
    return render_template("home.html")
@app.route("/second",methods=["GET","POST"])
def model():
    tour_pred=[]
    tds=[]
    t_n=""
    s=""
    if request.method=="POST":
        t_n=request.form['tour_name']
        option = request.form.getlist('pref')
        for i in option:
            s=i
        tour_pred=m.tour(t_n,s)
        tds=tour_pred
    return render_template("index.html",my_tour=tds,my_place=t_n,choice=s)
"""
@app.route("/last",methods=['POST'])
def submit():
    if request.method=="POST":
        location_name=request.form["tour_name"]
    return render_template("sub.html",n=location_name)
"""
if __name__=="__main__":
    app.run(debug=True)
