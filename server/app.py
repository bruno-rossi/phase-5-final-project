#!/usr/bin/env python3

from flask import request, session
from config import app, db
import os
from models import User

# Sign Up
@app.route('/signup', methods=['POST'])
def signup():
    email = request.get_json()['email']
    password = request.get_json()['password']

    try: 
        if email and password:
            new_user = User(email=email)
            new_user.password_hash = password
    except ValueError as e:
       return {'error': str(e)}, 409
       
    db.session.add(new_user)
    db.session.commit()
        
    return new_user.to_dict(), 201

    # return {'error': '422 Unprocessable Entity'}, 422

# Log in
@app.route('/login', methods=['POST'])
def login():

        email = request.get_json()['email']
        password = request.get_json()['password']

        user = User.query.filter(User.email == email).first()

        if user.authenticate(password):

            session['user_id'] = user.id
            return user.to_dict(), 200
        else:
            return {'error': '401 Unauthorized'}, 401

# Log out
@app.route('/logout', methods=['DELETE'])
def delete():

        session['user_id'] = None

        return {}, 204

# Clear session
# @app.route('/clear-session', methods=['DELETE'])
# def delete():
    
#         session['page_views'] = None
#         session['user_id'] = None

#         return {}, 204

# Check session
@app.route('/check_session')
def get():

    user_id = session.get('user_id')

    if user_id:
        user = User.query.filter(User.id == session.get('user_id')).first()
        
        return user.to_dict(), 200
    else:
        return {'message': '401: Not Authorized'}, 401
    