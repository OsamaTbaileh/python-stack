
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'keep it secret'

@app.route('/')          
def show_main_page():
    if 'count' not in session:  
        session['count'] = 0
    session['count'] += 1
    return render_template("counter.html")

@app.route('/destroy', methods=['POST'])          
def destroy_session():
    session.clear()		
    return redirect('/')

@app.route('/make_add_two', methods=['POST'])          
def make_2():
    session['count'] += 1
    return redirect('/')


@app.errorhandler(404)
def notValidRoute(e):
    return "Sorry, No response. Try again"

if __name__=="__main__":       
    app.run(debug=True)  


# A way to make it return to 0 not to 1
#     @app.route('/')          
# def show_main_page():
#     if 'count' not in session:  
#         session['count'] = 0
#     else:
#         current_vists = session['count']
#         session['count'] = current_vists+1
#     return render_template("counter.html")