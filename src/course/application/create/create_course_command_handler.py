from src.course.application.create.course_creator import CourseCreator
from src.course.application.create.create_course_command import CreateCourseCommand
from src.course.domain.course_id import CourseId
from src.course.domain.course_title import CourseTitle
from src.shared.domain.bus.command.command_handler import CommandHandler


class CreateCourseCommandHandler(CommandHandler):
    def __init__(self, course_creator: CourseCreator):
        self.course_creator = course_creator

    def __call__(self, command: CreateCourseCommand):
        course_id = CourseId(command.id)
        course_title = CourseTitle(command.title)
        self.course_creator.create(course_id, course_title)
