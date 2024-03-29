#!/usr/bin/env python3

from flask import request, session, make_response
from config import app, db
import os
from models import User, Course, Language, Lesson, UserCourse, UserLesson, Topic, UserTopic, Question, UserQuestion

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
        'courses',
        'languages',
        'topics'
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

@app.route('/courses/<int:course_id>/registration/', methods=['GET', 'POST'], endpoint='course-registration')
def course_registration(course_id):

    user_id = session.get('user_id')

    # Check if user is already registered:
    user_course = UserCourse.query.filter(UserCourse.course_id == course_id).filter(UserCourse.user_id == user_id).first()

    if user_course:
        if request.method == 'GET':
            return user_course.to_dict(), 200
        
        return {"error": "User is already registered"}, 409

    elif not user_course:
        if request.method == 'POST':

            new_user_course = UserCourse(
                user_id=request.get_json().get('user_id'),
                course_id=request.get_json().get('course_id')
            )

            db.session.add(new_user_course)
            db.session.commit()

            print(new_user_course)

            course_lessons = []
            for lesson in new_user_course.course.lessons:
                if not lesson.prev_lesson:
                    user_lesson = UserLesson(user_course_id=new_user_course.id, lesson_id=lesson.id, is_unlocked=True)
                else:
                    user_lesson = UserLesson(user_course_id=new_user_course.id, lesson_id=lesson.id)
                course_lessons.append(user_lesson)

            db.session.add_all(course_lessons)
            db.session.commit()

            return new_user_course.to_dict(), 200
    
        # Return 404 error if user course is not found:
        else:
            return {"error": "User course not found."}, 404
        
@app.route('/user-courses/<int:user_course_id>/user-lessons/<int:lesson_id>/', methods=['GET', 'PATCH'], endpoint='user-lessons')
def user_lessons(user_course_id, lesson_id):

    user_lesson = UserLesson.query.filter(UserLesson.lesson_id == lesson_id).filter(UserLesson.user_course_id == user_course_id).first()

    if user_lesson:
        if request.method == 'GET':
            return user_lesson.to_dict(), 200
        if request.method == 'PATCH':
            for attr in request.get_json():
                setattr(user_lesson, attr, request.get_json()[attr])

            db.session.add(user_lesson)
            db.session.commit()

            return user_lesson.to_dict(), 202
    
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
        
# Get, add or delete topics to a user through UserTopic
@app.route('/users/<int:user_id>/courses/', endpoint='user-courses')
def user_courses(user_id):

    user_courses = [user_course.to_dict()['course'] for user_course in UserCourse.query.filter(UserCourse.user_id == user_id)]

    if user_courses:
        return user_courses, 200
    elif not user_courses:
        return {"error": "No courses found for this user."}, 404
    
# @app.route('/users/<int:user_id>/recommended/', endpoint='recommended-courses')
# def recommended_courses(user_id):

#     user = User.query.filter(User.id == user_id).first()
    
#     rec_courses = []
    
@app.route('/users/<int:user_id>/questions/<int:question_id>/', methods=['GET', 'POST', 'PATCH'], endpoint='user-question')
def create_user_question(user_id, question_id):
    
    user_question = UserQuestion.query.filter(UserQuestion.question_id == question_id).filter(UserQuestion.user_id == user_id).first()

    print(user_question)

    if not user_question:
        if request.method == 'POST':
            new_user_question = UserQuestion(
                user_id=user_id,
                question_id=question_id,
                user_input=request.get_json().get("user_input"),
                ai_feedback=request.get_json().get("ai_feedback")
            )
            db.session.add(new_user_question)
            db.session.commit()

            return new_user_question.to_dict(), 200
        
        # Return 404 error if user question isn't found and method isn't POST:
        return {"error": "User question not found"}, 404

    if user_question:
        if request.method == 'GET':
            return user_question.to_dict(), 200
        
        if request.method == 'PATCH':
            for attr in request.get_json():
                setattr(user_question, attr, request.get_json()[attr])

            db.session.add(user_question)
            db.session.commit()

            return user_question.to_dict(), 202
