from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file and file.filename.endswith('.txt'):
        # Process the file here
        return 'File successfully uploaded and is a .txt file.'
    else:
        return 'Invalid file format. Please upload a .txt file.'

if __name__ == '__main__':
    app.run(debug=True)
