import os
from flask import Blueprint, request, render_template, redirect, url_for, current_app
from werkzeug.utils import secure_filename
from .models import insert_document, get_all_documents
from .utils import allowed_file, extract_text

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def index():
    documents = get_all_documents()
    return render_template('index.html', documents=documents)

@routes.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    category = request.form.get('category')

    if not file or not allowed_file(file.filename):
        return 'Invalid file type or missing file', 400

    filename = secure_filename(file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)

    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)

    content = extract_text(filepath)
    insert_document(filename, category, content, filepath)

    return redirect(url_for('routes.index'))
