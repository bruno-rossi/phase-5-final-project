#!/usr/bin/env python3

from flask import request, session, make_response
from config import app, db
import os
from models import User, Course, Language, Lesson, UserCourse, UserLesson, Topic, UserTopic

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

@app.route('/courses/<int:course_id>/registration', methods=['GET', 'POST'], endpoint='course-registration')
def course_registration(course_id):

    # Check if user is already registered:
    user_id = session.get('user_id')

    user_course = UserCourse.query.filter(UserCourse.course_id == course_id and UserCourse.user_id == user_id).first()

    if user_course:
        return {"error": "User is already registered"}, 409
    
    # Find the course in the db:
    course = Course.query.filter(Course.id == course_id).first()

    if course:
        if request.method == 'POST':

            new_user_course = UserCourse(
                user_id=request.get_json().get('user_id'),
                course_id=request.get_json().get('course_id')
            )

            db.session.add(new_user_course)
            db.session.commit()

            course_lessons = []
            for lesson in new_user_course.course.lessons:
                user_lesson = UserLesson(user_course_id=new_user_course.course.id, lesson_id=lesson.id)
                course_lessons.append(user_lesson)

            db.session.add_all(course_lessons)
            db.session.commit()

            return new_user_course.to_dict(), 200
    
    # Return 404 error if course is not found:
    elif not course:
        return {"error": "Course not found."}, 404
    
# Get all languages
@app.route('/languages/', endpoint='languages')
def all_languages():
    languages = [language.to_dict() for language in Language.query.all()]

    return languages, 200

# Get all topics
@app.route('/topics/', endpoint='topics')
def all_topics():
    topics = [topic.to_dict() for topic in Topic.query.all()]

    return topics, 200

# Get, add or delete topics to a user through UserTopic
@app.route('/users/<int:user_id>/topics/<int:topic_id>', methods=['GET', 'POST', 'DELETE'], endpoint='user-topics')
def user_topics(user_id, topic_id):

    user_topic = UserTopic.query.filter(UserTopic.topic_id == topic_id and UserTopic.user_id == user_id).first()

    print(user_topic)

    if request.method == 'GET':
        if user_topic:
            return user_topic.to_dict(), 200
        else:
            return {"error": "UserTopic not found"}, 404

    if request.method == 'POST':
        if user_topic:
            return {"error": "User topic already exists"}, 409
        else:
            new_user_topic = UserTopic(
                topic_id=request.get_json().get('topic_id'),
                user_id=request.get_json().get('user_id')
            )
            db.session.add(new_user_topic)
            db.session.commit()

            return new_user_topic.to_dict(), 201
        
    if request.method == 'DELETE':
        db.session.delete(user_topic)
        db.session.commit()

        return {}, 204
        