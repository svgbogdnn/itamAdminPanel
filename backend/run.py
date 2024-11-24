# IMPORT SESSION
# Flask Backend
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from flask_cors import CORS
from marshmallow import Schema, fields, validate, ValidationError
from datetime import datetime, timedelta
import os
# PostgreSQL (SQLAlchemy)
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text,
    Boolean,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
''' For JavaScript
import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router';
import { createStore } from 'vuex';'''
from openpyxl import Workbook
from io import BytesIO
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
import json
#load_dotenv()
# JWT
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)

'''---------------------------------------------------------'''
'''---------------------------------------------------------'''
'''---------------------------------------------------------'''
from app import create_app, db
from app.models import users
from flask_bcrypt import generate_password_hash

app = create_app()

# Add user creation logic inside the application context
with app.app_context():
    # Check if the user already exists to avoid duplicates
    if not users.query.filter_by(email="user@example.com").first():
        hashed_password = generate_password_hash("securepassword").decode('utf-8')
        user = users(
            name="John Doe",
            email="user@example.com",
            password=hashed_password,
            role="student"
        )
        db.session.add(user)
        db.session.commit()
        print("User created successfully!")
    else:
        print("User already exists!")

if __name__ == "__main__":
    app.run(debug=True)
