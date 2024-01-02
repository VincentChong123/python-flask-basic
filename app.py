from flask import Flask

app = Flask(__name__)
from routes import *


def about():
    return render_template('about.html')
    
if __name__ == "__main__":
    app.run(debug=True)


