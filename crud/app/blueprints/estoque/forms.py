from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class ProdutoForm(FlaskForm):
    nome = StringField('Nome do Produto', validators=[DataRequired()])
    descricao = TextAreaField('Descrição')
    preco = FloatField('Preço', validators=[DataRequired(), NumberRange(min=0)])
    quantidade = IntegerField('Quantidade', validators=[DataRequired(), NumberRange(min=0)])
    categoria = SelectField('Categoria', choices=[
        ('racao', 'Ração'),
        ('medicamento', 'Medicamento'),
        ('brinquedo', 'Brinquedo'),
        ('higiene', 'Higiene'),
        ('outros', 'Outros')
    ], validators=[DataRequired()])