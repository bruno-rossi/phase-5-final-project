"""Added courses, languages, lessons, relationships

Revision ID: a198d6753255
Revises: 02236a983139
Create Date: 2024-02-21 13:56:28.705209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a198d6753255'
down_revision = '02236a983139'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language_name', sa.String(), nullable=True),
    sa.Column('language_code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_languages'))
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['language_id'], ['languages.id'], name=op.f('fk_courses_language_id_languages')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_courses'))
    )
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_lessons_course_id_courses')),
    sa.ForeignKeyConstraint(['language_id'], ['languages.id'], name=op.f('fk_lessons_language_id_languages')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_lessons'))
    )
    op.create_table('users_courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_users_courses_course_id_courses')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_users_courses_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users_courses'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_courses')
    op.drop_table('lessons')
    op.drop_table('courses')
    op.drop_table('languages')
    # ### end Alembic commands ###
