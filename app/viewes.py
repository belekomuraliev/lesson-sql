from flask import request, render_template

from . import app, db
from .models import Category, Item
from .forms import CategoryForm, ItemForm

@app.route('/', methods=['GET', 'POST'] )
def index():
    form=CategoryForm()
    if request.method == 'POST':
        new_category_name = request.form.get('category_name')
        if new_category_name:
            new_category = Category(name=new_category_name)
            db.session.add(new_category)
            db.session.commit()

    categories = Category.query.all()
    return render_template('category.html', categories=categories, form=form)


@app.route('/items', methods=['GET', 'POST'])
def get_items():
    form = ItemForm()
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category_id = request.form.get('category_id')
        if name and price and category_id:
            item = Item(name=name, price=price, category_id=category_id)
            db.session.add(item)
            db.session.commit()
    items = Item.query.all()
    categories = Category.query.all()
    return render_template('view.html', items=items, categories=categories, form=form)
