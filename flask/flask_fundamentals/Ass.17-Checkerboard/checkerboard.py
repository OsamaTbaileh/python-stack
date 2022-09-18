
from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')          
def eight_by_eight():
    return render_template("checkerboard.html", rows=8, columns=8, color_1="red", color_2="black")

@app.route('/<int:x>')          
def rows_number(x):
    return render_template("checkerboard.html", rows=x, columns=8, color_1="red", color_2="black")  

@app.route('/<int:x>/<int:y>')          
def rows_columns(x, y):
    return render_template("checkerboard.html", rows=x, columns=y, color_1="red", color_2="black" )  

@app.route('/<int:x>/<int:y>/<color1>/<color2>')          
def rows_columns_color1_color2(x, y, color1, color2):
    return render_template("checkerboard.html", rows=x, columns = y, color_1=color1, color_2=color2 )

@app.errorhandler(404)
def notValidRoute(e):
    return "Sorry, No response. Try again"

if __name__=="__main__":       
    app.run(debug=True)  