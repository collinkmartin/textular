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

@app.route('/tools/reversetext', methods=['GET', 'POST'])
def reverseText():
    sessionData = ''
    if request.method == 'POST':
        session['words'] = request.form['toolbox']
        return redirect(url_for('reverseText'))
    else:
        form = ToolForm()
        if 'words' in session:
            form.message.data = reverse(session['words'])
            session.clear()
            return render_template('reversetext.html', form=form)
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