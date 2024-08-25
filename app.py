from flask import Flask, render_template, request, redirect, url_for
import os
import shutil
import atexit
from werkzeug.utils import secure_filename
import re
from validate_log import validate_log

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file and file.filename.endswith('.txt'):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        file.save(file_path)

        response = validate_log(file_path)

        return response
    else:
        return 'Invalid file format. Please upload a .txt file.'

def cleanup():
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        shutil.rmtree(app.config['UPLOAD_FOLDER'])

atexit.register(cleanup)

if __name__ == '__main__':
    app.run(debug=True)
