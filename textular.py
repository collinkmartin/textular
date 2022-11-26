from flask import Flask, render_template, request, url_for, redirect, session
from forms import ToolForm
from textmanipulator import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '&*!@#)$JcnuaSD*!@#()*#jda0!(ud)AD,@*@!ajsdDJ*@#jdASLI'

# Main Page Routing
@app.route('/')
def index():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

# Tools Routing

'''
    I use sessions to store text for manipulation on the backend. This 
    allowed me to keep the project simple; no need for a database.
'''
@app.route('/tools/reversetext', methods=['GET', 'POST'])
def reverseText():
    sessionData = ''
    # If request method is POST, this means the user submitted the form.
    # Pull the form data from the request and store it in a session
    if request.method == 'POST':
        session['words'] = request.form['toolbox']
        return redirect(url_for('reverseText'))
    else:
        # If the specific session we create exists (after a user submits a form)
        # We manipulate the data and clear the session (in case they want to submit again)
        form = ToolForm()
        if 'words' in session:
            form.message.data = reverse(session['words'])
            session.clear()
            return render_template('reversetext.html', form=form)
        # User's first time getting form.
        else:
            form.message.data = 'Enter your text here!'
        return render_template('reversetext.html', form=form)

@app.route('/tools/uppercasetext', methods=['GET', 'POST'])
def upperText():
    sessionData = ''
    if request.method == 'POST':
        session['words'] = request.form['toolbox']
        return redirect(url_for('upperText'))
    else:
        form = ToolForm()
        if 'words' in session:
            form.message.data = uppercase(session['words'])
            session.clear()
            return render_template('uppercase.html', form=form)
        else:
            form.message.data = 'Enter your text here!'
        return render_template('uppercase.html', form=form)

@app.route('/tools/lowercasetext', methods=['GET', 'POST'])
def lowerText():
    sessionData = ''
    if request.method == 'POST':
        session['words'] = request.form['toolbox']
        return redirect(url_for('lowerText'))
    else:
        form = ToolForm()
        if 'words' in session:
            form.message.data = lowercase(session['words'])
            session.clear()
            return render_template('lowercase.html', form=form)
        else:
            form.message.data = 'Enter your text here!'
        return render_template('lowercase.html', form=form)

@app.route('/tools/sentencecase', methods=['GET', 'POST'])
def sentenceText():
    sessionData = ''
    if request.method == 'POST':
        session['words'] = request.form['toolbox']
        return redirect(url_for('sentenceText'))
    else:
        form = ToolForm()
        if 'words' in session:
            form.message.data = sentence(session['words'])
            session.clear()
            return render_template('sentence.html', form=form)
        else:
            form.message.data = 'Enter your text here!'
        return render_template('sentence.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)