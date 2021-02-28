from src.course.application.finder.find_course_query import FindCourseQuery
from src.shared.infrastructure.api_controller import ApiController


class CourseGetController(ApiController):
    def __call__(self, course_id: str):
        query = FindCourseQuery(course_id=course_id)
        return self.query_bus.ask(query)
