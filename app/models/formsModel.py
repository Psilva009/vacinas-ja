from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class InputDataForm(FlaskForm):
    capacity = IntegerField('capacity', validators=[DataRequired()])
    numberPosts = IntegerField('numberPosts', validators=[DataRequired()])
    req1 = IntegerField('req1', validators=[DataRequired()])
    req2 = IntegerField('req2', validators=[DataRequired()])
    req3 = IntegerField('req3', validators=[DataRequired()])
    req4 = IntegerField('req4', validators=[DataRequired()])
    req5 = IntegerField('req5', validators=[DataRequired()])