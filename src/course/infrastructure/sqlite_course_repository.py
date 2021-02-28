import sqlite3

from antidote import Service

from src.course.domain.course import Course
from src.course.domain.course_id import CourseId
from src.course.domain.course_repository import CourseRepository

connection = sqlite3.connect('courses.db')


class SqliteCourseRepository(CourseRepository, Service):
    def __init__(self):
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS courses (id text primary key, title text) WITHOUT ROWID')

    def save(self, course):
        cursor = connection.cursor()
        cursor.execute('INSERT INTO courses VALUES (?, ?)', (course.id, course.title))

    def find(self, id: CourseId) -> Course:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM courses WHERE id = ? LIMIT 1', id)
        return cursor.fetchone()
