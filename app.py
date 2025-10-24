from flask import Flask, render_template, request, send_from_directory
import os
from filters import apply_filter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        filter_type = request.form.get('filter')

        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            # Filtre uygula
            filtered_path = apply_filter(image_path, filter_type)
            return render_template('index.html', uploaded_image=image_path, filtered_image=filtered_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
