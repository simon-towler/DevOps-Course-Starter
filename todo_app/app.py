from flask import Flask, render_template, session
from todo_app.flask_config import Config
from todo_app.data.session_items import _DEFAULT_ITEMS, get_items

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    # return 'Hello World!'
    return render_template('index.html', items=get_items())


if __name__ == '__main__':
    app.run()
