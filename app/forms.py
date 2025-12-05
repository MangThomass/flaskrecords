<<<<<<< HEAD
"""WTForms definitions - moved from app.py"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RecordForm(FlaskForm):
    """Form for creating/editing records"""
    title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=1, max=140)]
    )
    content = TextAreaField(
        'Content',
        validators=[Length(max=2000)]
    )
    submit = SubmitField('Save Record')
=======
"""WTForms definitions - moved from app.py"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RecordForm(FlaskForm):
    """Form for creating/editing records"""
    title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=1, max=140)]
    )
    content = TextAreaField(
        'Content',
        validators=[Length(max=2000)]
    )
    submit = SubmitField('Save Record')
>>>>>>> 4eea04cc5b8ab6a74f0a65f3a68c4f6f847b7739
