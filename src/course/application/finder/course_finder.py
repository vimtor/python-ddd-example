from antidote import Service

from src.course.domain.course_id import CourseId
from src.course.domain.course_repository import CourseRepository


class CourseFinder(Service):
    def __init__(self, course_repository: CourseRepository):
        self.course_repository = course_repository

    def find(self, course_id: CourseId):
        return self.course_repository.find(course_id)
