import os
from flask import (
    Blueprint, request, render_template, redirect, url_for, flash, current_app
)
from werkzeug.utils import secure_filename
from .models import insert_document, get_all_documents
from .utils import allowed_file, extract_text

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        category = request.form.get('category')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            os.makedirs(upload_folder, exist_ok=True)  # ensure folder exists

            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)

            # Extract searchable text content
            content = extract_text(filepath)

            # Save metadata + content to DB
            insert_document(filename, category, content, filepath)



            flash('File uploaded successfully!')
            return redirect(url_for('routes.index'))
        else:
            flash('Invalid file type. Only PDF and Markdown allowed.')

    docs = get_all_documents()
    return render_template('index.html', documents=docs)
