from flask import Flask, render_template, session, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import _DEFAULT_ITEMS, get_items, add_item
import requests
import os

app = Flask(__name__)
app.config.from_object(Config)
TRELLO_KEY = os.environ.get('TRELLO_KEY')
TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')


@app.route('/')
def index():
    response = requests.get(f"https://trello.com/1/lists/609392e0aaa6e8618e341f90/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}")
    return render_template('index.html', items=response.json())

@app.route('/addItem', methods=['POST'])
def addItem():
    itemName = request.form['name']
    requests.post(f"https://trello.com/1/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idList=609392e0aaa6e8618e341f90", data={"name":itemName})
    return redirect("/", code=303)

if __name__ == '__main__':
    app.run()
