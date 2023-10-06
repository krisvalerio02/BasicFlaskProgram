# 'virtualenv env', env is the conventional name to name your environment
# To activate the environment, type 'source env/bin/activate'
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)