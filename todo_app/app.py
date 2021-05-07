from flask import Flask, render_template, session, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import _DEFAULT_ITEMS, get_items, add_item
import requests

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    response = requests.get("https://trello.com/1/lists/609392e0aaa6e8618e341f90/cards?key=58e57e7addabdcbcfae7f8d62560afbe&token=a9f6f553a13eceaf9eda2839cd85b665638644ca3c36011ccb18545f5325cd8d")
    return render_template('index.html', items=response.json())

@app.route('/addItem', methods=['POST'])
def addItem():
    itemName = request.form['itemName']
    add_item(itemName)
    return redirect("/", code=303)

if __name__ == '__main__':
    app.run()
