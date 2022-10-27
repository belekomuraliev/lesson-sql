
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

from .models import Category


def get_all_category():
    result = []
    for category in Category.query.all():
        result.append((category.id, category.name))
    return result


class CategoryForm(FlaskForm):
    category_name = StringField(label="Наименование Категории")
    submit = SubmitField(label="Сохранить категорию")


class ItemForm(FlaskForm):
    name = StringField(label="Наименование Категории")
    price = IntegerField(label="Сохранить категорию")
    category_id = SelectField(label="Категория Товара", choices=get_all_category())
    submit =SubmitField(label="Сохранить")

