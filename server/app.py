#!/usr/bin/env python3

from flask import request, session, make_response
from config import app, db
import os
from models import User, Course, Lesson

@app.before_request
def load_user():

    if request.method == 'OPTIONS':
        response = make_response({}, 200)
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response
    
    # Check access:
    open_access_list = [
        'signup',
        'login',
        'logout',
        'check_session',
        'course',
        'courses'
    ]

    print(session.get('user_id'))

    # Returns 401 error if the endpoint is not open access and the user is not logged in:
    if (request.endpoint) not in open_access_list and (not session.get('user_id')):
        return {'error': '401 Unauthorized'}, 401

# Sign up
@app.route('/signup', methods=['POST'], endpoint='signup')
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
@app.route('/login', methods=['POST'], endpoint='login')
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
@app.route('/logout', methods=['DELETE'], endpoint='logout')
def delete():

        session['user_id'] = None
        session.clear()

        return {}, 204

# Check session
@app.route('/check_session', endpoint='check_session')
def get():

    user_id = session.get('user_id')

    if user_id:
        user = User.query.filter(User.id == session.get('user_id')).first()
        
        return user.to_dict(), 200
    else:
        return {'message': '401: Not Authorized'}, 401

# Get user by id
@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'], endpoint='user')
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
@app.route('/courses/', endpoint='courses')
def all_courses():
    courses = [course.to_dict() for course in Course.query.all()]

    return courses, 200

@app.route('/courses/<int:id>', endpoint='course')
def get_course_by_id(id):
    course = Course.query.filter(Course.id == id).first()

    print(session.get('user_id'))

    if course:
        return course.to_dict(), 200
    else:
        return {"error": "Course not found."}, 404
    
@app.route('/lessons/<int:id>', endpoint='lesson')
def get_lesson_by_id(id):
    lesson = Lesson.query.filter(Lesson.id == id).first()

    if lesson:
        return lesson.to_dict(), 200
    else:
        return {"error": "Lesson not found."}, 404
