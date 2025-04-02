from flask import Blueprint, request, jsonify
from models import db, User, Expense, Category, Budget

# Create a Blueprint for API routes
api_bp = Blueprint('api', __name__)

# ---------------- User Routes ----------------
@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])

@api_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201

# ---------------- Expense Routes ----------------
@api_bp.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([{"id": e.id, "amount": e.amount, "category_id": e.category_id} for e in expenses])

@api_bp.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    new_expense = Expense(amount=data['amount'], category_id=data['category_id'], user_id=data['user_id'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Expense added successfully!"}), 201

# ---------------- Category Routes ----------------
@api_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{"id": cat.id, "name": cat.name} for cat in categories])

@api_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message": "Category added successfully!"}), 201

# ---------------- Budget Routes ----------------
@api_bp.route('/budgets', methods=['GET'])
def get_budgets():
    budgets = Budget.query.all()
    return jsonify([{"id": b.id, "amount": b.amount, "category_id": b.category_id} for b in budgets])

@api_bp.route('/budgets', methods=['POST'])
def add_budget():
    data = request.json
    new_budget = Budget(amount=data['amount'], category_id=data['category_id'])
    db.session.add(new_budget)
    db.session.commit()
    return jsonify({"message": "Budget added successfully!"}), 201
