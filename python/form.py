from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired



class InputForm(FlaskForm):
    conversion = RadioField('Conversion type', choices=[('jsontocsv', 'JSON to CSV'), ('csvtojson', 'CSV to JSON')], default='jsontocsv')
    user_input = TextAreaField('', render_kw={'placeholder': 'Enter your text to convert here...'})
    output = TextAreaField('', render_kw={'readonly': True, 'placeholder': 'Converted output will appear here...'})
    file = FileField('Upload File')
    submit = SubmitField('Convert')