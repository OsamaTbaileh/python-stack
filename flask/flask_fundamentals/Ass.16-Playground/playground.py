
from flask import Flask, render_template
app = Flask(__name__)   

# # solutoin of first 3 requirements:
# @app.route('/play')          
# def three_bosxes():
#     return render_template("playground.html")  

# @app.route('/play/<int:x>')
# def repeat_boxes(x):
#     return render_template("playground_num.html", times=x)

# @app.route('/play/<int:x>/<color>')
# def repeat_boxes_withcolors(x, color):
#     return render_template("playground_num_color.html", times=x, wanted_color=color)


# Bonus:
@app.route('/play')          
def three_bosxes():
    return render_template("playground_num_color_BONUS.html", times=3, wanted_color="skyblue" )  

@app.route('/play/<int:x>')
def repeat_boxes(x):
    return render_template("playground_num_color_BONUS.html", times=x, wanted_color="skyblue")

@app.route('/play/<int:x>/<color>')
def repeat_boxes_withcolors(x, color):
    return render_template("playground_num_color_BONUS.html", times=x, wanted_color=color)


@app.errorhandler(404)
def notValidRoute(e):
    return "Sorry, No response. Try again"

if __name__=="__main__":       
    app.run(debug=True)  