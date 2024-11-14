from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired

class WineDataForm(FlaskForm):
    fixed_acidity = FloatField('Fixed acidity',validators=[DataRequired()])
    volatile_acidity = FloatField('Volatile acidity',validators=[DataRequired()])
    citric_acid = FloatField('Citric acid',validators=[DataRequired()])
    residual_sugar = FloatField('Residual Sugar',validators=[DataRequired()])
    chlorides = FloatField('Chlorides',validators=[DataRequired()])
    free_sulphur = FloatField('Free Sulphur Dioxide',validators=[DataRequired()])
    total_sulphur = FloatField('Total Sulphur Dioxide',validators=[DataRequired()])
    density = FloatField('Density',validators=[DataRequired()])
    ph = FloatField('pH',validators=[DataRequired()])
    sulphates = FloatField('Sulphates',validators=[DataRequired()])
    alcohol = FloatField('Alcohol',validators=[DataRequired()])
    