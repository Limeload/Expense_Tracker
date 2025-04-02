from app import app, db
from models import Category

categories = ["Food", "Transport", "Entertainment", "Utilities", "Rent", "Salary", "Health", "Others"]

with app.app_context():
    for cat in categories:
        if not Category.query.filter_by(name=cat).first():
            new_category = Category(name=cat)
            db.session.add(new_category)
    db.session.commit()
    print("Categories seeded successfully!")
