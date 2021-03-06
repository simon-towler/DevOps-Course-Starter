from flask import Flask, render_template, session, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import _DEFAULT_ITEMS, get_items, add_item

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', items=get_items())

@app.route('/addItem', methods=['POST'])
def addItem():
    itemName = request.form['itemName']
    add_item(itemName)
    return redirect("/", code=303)

if __name__ == '__main__':
    app.run()
