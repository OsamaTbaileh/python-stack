
from flask import Flask, render_template, request, redirect
app = Flask(__name__)   

@app.route('/')          
def show_main_page():
    return render_template("dojo_survey.html")

@app.route('/result', methods=['POST'])          
def create_ursers():
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    # gender_from_form = request.form['flexRadioDefault']
    # checkbox_from_form = request.form['checkbox']
    return render_template("result.html",
        name_on_template = name_from_form,
        location_on_template = location_from_form,
        language_on_template = language_from_form,
        comment_on_template = comment_from_form,  
        # gender_on_template = gender_from_form,
        # checkbox_on_template = checkbox_from_form
        )

@app.errorhandler(404)
def notValidRoute(e):
    return "Sorry, No response. Try again"

if __name__=="__main__":       
    app.run(debug=True)  