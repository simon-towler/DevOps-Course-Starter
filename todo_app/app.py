from flask import Flask, render_template, session

from todo_app.flask_config import Config

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    # return 'Hello World!'
    def get_items():
        return session.get('items', _DEFAULT_ITEMS)
    return render_template('index.html', items=get_items())


if __name__ == '__main__':
    app.run()
