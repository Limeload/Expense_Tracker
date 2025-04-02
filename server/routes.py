from flask import Blueprint, request, jsonify
from models import db, User, Expense, Category, Budget

routes = Blueprint('routes', __name__)

# Get all categories
@routes.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{'id': cat.id, 'name': cat.name} for cat in categories])

# Get all expenses
@routes.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([
        {'id': exp.id, 'title': exp.title, 'amount': exp.amount, 'category': exp.category.name, 'user_id': exp.user_id, 'date': exp.date}
        for exp in expenses
    ])

# Get all expenses for a specific user
@routes.route('/expenses/user/<int:user_id>', methods=['GET'])
def get_expenses_by_user(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return jsonify([
        {'id': exp.id, 'title': exp.title, 'amount': exp.amount, 'category': exp.category.name, 'date': exp.date}
        for exp in expenses
    ])

# Get all users
@routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {'id': user.id, 'username': user.username, 'email': user.email, 'created_at': user.created_at}
        for user in users
    ])

# Get a specific user by ID
@routes.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at
    })

# Create a new category
@routes.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully'}), 201

# Create a new expense
@routes.route('/expenses', methods=['POST'])
def create_expense():
    data = request.get_json()
    new_expense = Expense(
        title=data['title'],
        amount=data['amount'],
        category_id=data['category_id'],
        user_id=data['user_id']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'}), 201

# Create a new user
@routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# Add a budget
@routes.route('/budgets', methods=['POST'])
def create_budget():
    data = request.get_json()
    new_budget = Budget(
        user_id=data['user_id'],
        category_id=data['category_id'],
        amount_limit=data['amount_limit'],
        month=data['month'],
        year=data['year']
    )
    db.session.add(new_budget)
    db.session.commit()
    return jsonify({'message': 'Budget added successfully'}), 201

# Get all budgets for a specific user
@routes.route('/budgets/user/<int:user_id>', methods=['GET'])
def get_budgets_by_user(user_id):
    budgets = Budget.query.filter_by(user_id=user_id).all()
    return jsonify([
        {'id': b.id, 'category': b.category.name, 'amount_limit': b.amount_limit, 'month': b.month, 'year': b.year}
        for b in budgets
    ])
