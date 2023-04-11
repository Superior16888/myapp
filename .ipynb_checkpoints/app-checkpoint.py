from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    html_files = [f for f in os.listdir('static') if f.endswith('.html')]
    return render_template('index.html', html_files=html_files)

if __name__ == '__main__':
    app.run()
    