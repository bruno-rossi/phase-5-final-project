from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from config import db, bcrypt


# ============= User =============
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String)
    _password_hash = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    # Relationships:
    courses = db.relationship('UserCourse', back_populates='user')

    # Serialization:
    serialize_rules = ['-courses']

    # Validations
    @validates('email')
    def validate_email(self, key, new_email):
        existing_user = User.query.filter(User.email == new_email).first()

        if existing_user:
            raise ValueError('There is already an account with this email.')
        return new_email

    def __repr__(self) -> str:
        return f"<User {self.email}, id: {self.id}"


# ============= UserCourse =============
class UserCourse(db.Model, SerializerMixin):
    __tablename__ = 'users_courses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    # Relationships:
    user = db.relationship('User', back_populates='courses')
    course = db.relationship('Course', back_populates='users')
    user_lessons = db.relationship('UserLesson', back_populates='user_course')

    # Serialization:
    serialize_rules = ['-user.courses', '-course.users', '-user_lessons.user_course']

    def __repr__(self) -> str:
        return f"<UserCourse id: {self.id} user {self.user_id} course {self.course_id}"

# ============= Course =============
class Course(db.Model, SerializerMixin):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))

    # Relationships:
    users = db.relationship('UserCourse', back_populates='course')
    language = db.relationship('Language', back_populates='courses')
    lessons = db.relationship('Lesson', back_populates='course')

    # Serialization:
    serialize_rules = ['-language.courses', '-language.lessons', '-lessons.language', '-lessons.course', '-users']

    # Validations:
    
    def __repr__(self) -> str:
        return f"<Course {self.id}, language: {self.language}"

# ============= UserLesson =============
class UserLesson(db.Model, SerializerMixin):
    __tablename__ = 'users_lessons'

    id = db.Column(db.Integer, primary_key=True)
    user_course_id = db.Column(db.Integer, db.ForeignKey('users_courses.id'))
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    is_unlocked = db.Column(db.Boolean, default=False)

    # Relationships:
    user_course = db.relationship('UserCourse', back_populates='user_lessons')
    lesson = db.relationship('Lesson', back_populates='user_lessons')

    # Serialization:
    serialize_rules = ['-user_course.user_lessons', '-lesson.user_lessons']

    def __repr__(self) -> str:
        return f"<UserLesson id: {self.id} user_course_id:{self.user_course_id} lesson_id: {self.lesson_id}>"


# ============= Lesson =============
class Lesson(db.Model, SerializerMixin):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    title = db.Column(db.String)
    content = db.Column(db.String)
    prev_lesson = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    next_lesson = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    lesson_type = db.Column(db.String)

    # Relationships:
    language = db.relationship('Language', back_populates='lessons')
    course = db.relationship('Course', back_populates='lessons')
    user_lessons = db.relationship('UserLesson', back_populates='lesson')

    # Serialization:
    serialize_rules = ['-language.courses', '-language.lessons', '-course.language', '-course.lessons', '-user_lessons']

    # Validations:

    def __repr__(self) -> str:
        return f"<Lesson {self.id}, language: {self.language}>"


# ============= Language =============
class Language(db.Model, SerializerMixin):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String)
    language_code = db.Column(db.String)

    # Relationships:
    courses = db.relationship('Course', back_populates='language')
    lessons = db.relationship('Lesson', back_populates='language')

    # Serialization:
    serialize_rules = ['-courses.language', '-courses.lessons', '-lessons.language', '-lessons.course']

    # Validations:

    def __repr__(self) -> str:
        return f"<Language {self.id}, language: {self.language_code}"