from flask import Flask, render_template, session, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import _DEFAULT_ITEMS, get_items, add_item
import requests
import os

app = Flask(__name__)
app.config.from_object(Config)
TRELLO_KEY = os.environ.get('TRELLO_KEY')
TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
TRELLO_LIST_ID_DOING = "609392e0aaa6e8618e341f90"
TRELLO_LIST_ID_TODO = "609392e0aaa6e8618e341f8f"
TRELLO_LIST_ID_DONE = "609392e0aaa6e8618e341f91"


@app.route('/')
def index():
    todos = requests.get(f"https://trello.com/1/lists/{TRELLO_LIST_ID_TODO}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}")
    dones = requests.get(f"https://trello.com/1/lists/{TRELLO_LIST_ID_DONE}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}")
    return render_template('index.html', todos=todos.json(), dones=dones.json())

@app.route('/addItem', methods=['POST'])
def addItem():
    itemName = request.form['name']
    requests.post(f"https://trello.com/1/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idList={TRELLO_LIST_ID_TODO}", data={"name":itemName})
    return redirect("/", code=303)

@app.route('/completeItem', methods=['POST'])
def completeItem():
    itemId = request.form['id']
    requests.put(f"https://trello.com/1/cards/{itemId}?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idList={TRELLO_LIST_ID_DONE}")
    return redirect("/", code=303)

@app.route('/resetItem', methods=['POST'])
def resetItem():
    itemId = request.form['id']
    requests.put(f"https://trello.com/1/cards/{itemId}?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idList={TRELLO_LIST_ID_TODO}")
    return redirect("/", code=303)

if __name__ == '__main__':
    app.run()
