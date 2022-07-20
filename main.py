from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/hello', )
def page_hello():
    return "Привет"

@app.route('/goodbye', )
def page_goodbye():
    return "Пока"

@app.route('/seeyou', )
def page_seeyou():
    return "Увидимся"

