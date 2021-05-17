from flask import request
from werlzeug import secure_filename

@app.router('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.file['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
        