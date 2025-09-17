#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Healix - Health Management System
--------------------------------
This module initializes the Flask application for the Healix project,
setting up routes, configurations, and file handling capabilities.
"""

import os
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, abort, jsonify
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'healix_dev_key')  # Set a proper key in production
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file size
app.config['DEBUG'] = True  # Set to False in production

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Ensure upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Helper function to check allowed file extensions
def allowed_file(filename):
    """Check if the file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    """Render the homepage"""
    return render_template('index.html', page_title="Healix - Your Health, Organized")

@app.route('/dashboard')
def dashboard():
    """
    Dashboard route - displays user's health overview
    Future enhancement: Add user authentication check
    """
    # Placeholder for dashboard data
    dashboard_data = {
        "user": "Sample User",
        "recent_reports": [],
        "upcoming_appointments": [],
        "vitals": {}
    }
    return render_template('dashboard.html', page_title="Dashboard", data=dashboard_data)

@app.route('/upload-report', methods=['GET', 'POST'])
def upload_report():
    """Handle report uploads - GET shows form, POST processes upload"""
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If user does not select file, browser submits an empty file
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        # If file is valid and allowed
        if file and allowed_file(file.filename):
            # Secure the filename to prevent directory traversal attacks
            filename = secure_filename(file.filename)
            
            # Add timestamp to filename to make it unique
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"{timestamp}_{filename}"
            
            # Save the file to the uploads folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            flash('File successfully uploaded', 'success')
            
            # Future enhancement: Process the file (OCR, extract data, etc.)
            # Future enhancement: Save metadata to database
            
            # Redirect to view the uploaded report details
            return redirect(url_for('dashboard'))
    
    # GET request - show the upload form
    return render_template('upload_report.html', page_title="Upload Report")

@app.route('/vitals')
def vitals():
    """Display user's health vitals and trends"""
    # Placeholder for vitals data
    vitals_data = {
        "blood_pressure": [],
        "heart_rate": [],
        "weight": [],
        "glucose": []
    }
    return render_template('vitals.html', page_title="Health Vitals", data=vitals_data)

@app.route('/reminders')
def reminders():
    """Display and manage user's health reminders"""
    # Placeholder for reminders data
    reminders_data = {
        "medications": [],
        "appointments": [],
        "tests": []
    }
    return render_template('reminders.html', page_title="Reminders", data=reminders_data)

@app.route('/settings')
def settings():
    """User settings and preferences"""
    return render_template('settings.html', page_title="Settings")

# API Routes for future enhancement
@app.route('/api/health', methods=['GET'])
def api_health():
    """API health check endpoint"""
    return jsonify({"status": "healthy", "version": "0.1.0"})

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html', page_title="Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template('500.html', page_title="Internal Server Error"), 500

# Future enhancements (commented out)
"""
# Database configuration
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healix.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User authentication
from flask_login import LoginManager, UserMixin
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Internationalization (i18n)
from flask_babel import Babel
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

# Email functionality
from flask_mail import Mail
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'
"""

if __name__ == "__main__":
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
