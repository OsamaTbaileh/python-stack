
from flask import Flask, render_template, request, redirect
app = Flask(__name__)   

@app.route('/')          
def show_main_page():
    return render_template("dojo_survey.html")

@app.route('/result', methods=['POST'])          
def create_ursers():

    results= [
    {"name": request.form['name']},
    {"location": request.form['location']},
    {"language": request.form['language']},
    {"comment": request.form['comment']},
    {"gender": request.form['flexRadioDefault']},
    # {"checkbox": "NO"}
]
    # if request.form['checkbox'] == "on":
    #     results.append={"checkbox": "OK"}

    return render_template("result.html", results_template = results)

@app.errorhandler(404)
def notValidRoute(e):
    return "Sorry, No response. Try again"

if __name__=="__main__":       
    app.run(debug=True)  