from src.course.application.create.create_course_command import CreateCourseCommand
from src.shared.infrastructure.api_controller import ApiController


class CoursePostController(ApiController):
    def __call__(self, body):
        command = CreateCourseCommand(id=body['id'], title=body['title'])
        self.command_bus.dispatch(command)
        return '', 201
