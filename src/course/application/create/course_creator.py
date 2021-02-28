from antidote import Service

from src.course.domain.course import Course
from src.course.domain.course_id import CourseId
from src.course.domain.course_repository import CourseRepository
from src.course.domain.course_title import CourseTitle


class CourseCreator(Service):
    def __init__(self, course_repository: CourseRepository):
        self.course_repository = course_repository

    def create(self, id: CourseId, title: CourseTitle):
        course = Course(id, title)
        self.course_repository.save(course)
