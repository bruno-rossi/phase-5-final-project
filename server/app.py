#!/usr/bin/env python3

from flask import request, session
from config import app, db
import os
from models import User, Course

# Sign up
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
        session.clear()

        return {}, 204

# Check session
@app.route('/check_session')
def get():

    user_id = session.get('user_id')

    if user_id:
        user = User.query.filter(User.id == session.get('user_id')).first()
        
        return user.to_dict(), 200
    else:
        return {'message': '401: Not Authorized'}, 401

# Get user by id
@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if user:
        if request.method == 'GET':
            return user.to_dict(), 200
        if request.method == 'PATCH':
            for attr in request.get_json():
                setattr(user, attr, request.get_json()[attr])

            db.session.add(user)
            db.session.commit()

            return user.to_dict(), 202

        if request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()

            return {"success": "User has been successfully deleted"}, 204
    else:
        return { "error": "User not found" }, 404

# Get all courses
@app.route('/courses/')
def all_courses():
    courses = [course.to_dict() for course in Course.query.all()]

    return courses, 200

@app.route('/courses/<int:id>')
def get_course_by_id(id):
    course = Course.query.filter(Course.id == id).first()

    if course:
        return course.to_dict(), 200
    else:
        return {"error": "Course not found."}, 404
