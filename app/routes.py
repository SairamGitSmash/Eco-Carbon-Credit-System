# from flask import Blueprint, render_template, request, redirect, url_for, jsonify
# from app import db
# from app.models import User
# from flask_jwt_extended import create_access_token
# from flask import flash, session
# import bcrypt

# main_bp = Blueprint('main', __name__)

# @main_bp.route('/')
# def home():
#     return render_template('index.html')

# @main_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         role = request.form['role']

#         existing_user = User.query.filter_by(username=username).first()
#         if existing_user:
#             flash('Username already exists!', 'danger')
#             return redirect(url_for('main.register'))

#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#         new_user = User(username=username, password_hash=hashed_password.decode('utf-8'), role=role)
#         db.session.add(new_user)
#         db.session.commit()
#         flash('Registration successful! You can now log in.', 'success')
#         return redirect(url_for('main.login'))

#     return render_template('main.register')

# @main_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         user = User.query.filter_by(username=username).first()
#         if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
#             access_token = create_access_token(identity={'username': user.username, 'role': user.role})
#             session['user'] = {'username': user.username, 'role': user.role}
#             flash('Login successful!', 'success')
#             return redirect(url_for('main.dashboard'))

#         flash('Invalid username or password!', 'danger')
#         return redirect(url_for('main.login'))

#     return render_template('main.login')

# @main_bp.route('/dashboard')
# def dashboard():
#     if 'user' not in session:
#         return redirect(url_for('main.login'))
#     return render_template('dashboard.html', user=session['user'])














from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash, session
from app import db
from app.models import User
from flask_jwt_extended import create_access_token
import bcrypt

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!', 'danger')
            return redirect(url_for('main.register'))  # Corrected

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        new_user = User(username=username, password_hash=hashed_password.decode('utf-8'), role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('main.login'))  # Corrected

    return render_template('register.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            access_token = create_access_token(identity={'username': user.username, 'role': user.role})
            session['user'] = {'username': user.username, 'role': user.role}
            flash('Login successful!', 'success')
            return redirect(url_for('main.dashboard'))  # Corrected

        flash('Invalid username or password!', 'danger')
        return redirect(url_for('main.login'))  # Corrected

    return render_template('login.html')

@main_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('main.login'))
    return render_template('dashboard.html', user=session['user'])

















