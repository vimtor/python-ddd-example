from src.course.application.finder.course_finder import CourseFinder
from src.course.application.finder.find_course_query import FindCourseQuery
from src.course.domain.course_id import CourseId
from src.shared.domain.bus.query.query_handler import QueryHandler


class FindCourseQueryHandler(QueryHandler):
    def __init__(self, course_finder: CourseFinder):
        self.course_finder = course_finder

    def __call__(self, query: FindCourseQuery):
        course_id = CourseId(query.course_id)
        return self.course_finder.find(course_id)
