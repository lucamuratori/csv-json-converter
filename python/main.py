from brain import *
from flask import Flask, request, render_template, send_from_directory
from flask_bootstrap import Bootstrap5
from form import InputForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    form = InputForm()
    if form.validate_on_submit():
        # gettin data from the form
        conversion = form.conversion.data
        text = request.form.get("user_input")
        file = request.files['file']

        # saving uploaded file to uploads folder
        filename = secure_filename(str(file.filename))
        file_path = os.path.join(os.getcwd(), f'python/uploads/{filename}')
        file.save(file_path)
        
        # cases where the file is provided
        if file:
            # from json to csv
            if conversion == 'jsontocsv':
                output = convert_from_file(file_path, to_csv=True)
                os.remove(file_path)
                return render_template("index.html", form=form, output=output, send_file=send_from_directory('results/', 'output.csv', as_attachment=True))
            # from csv to json
            else:
                output = convert_from_file(file_path, to_json=True)
                form.populate_obj(form.output)
                os.remove(file_path)
                return render_template("index.html", form=form, output=output, send_file=send_from_directory('results/', 'output.json', as_attachment=True))
        
        # cases where text input is provided
        else:
            # from json to csv
            if conversion == 'jsontocsv':
                output = convert_from_text(text, to_csv=True)
                return render_template("index.html", form=form, output=output, send_file=send_from_directory('results/', 'output.csv', as_attachment=True))
            # from csv to json
            else:
                output = convert_from_text(text, to_json=True)
                return render_template("index.html", form=form, output=output, send_file=send_from_directory('results/', 'output.json', as_attachment=True))
            
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000)