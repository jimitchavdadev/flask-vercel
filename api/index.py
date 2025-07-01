from flask import Flask, render_template
import os

# Use the default templates folder (relative to index.py)
app = Flask(__name__, template_folder="../templates")

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
