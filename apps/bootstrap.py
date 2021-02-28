from antidote import implementation, inject

from src.course.application.create.create_course_command import CreateCourseCommand
from src.course.application.create.create_course_command_handler import CreateCourseCommandHandler
from src.course.application.finder.find_course_query import FindCourseQuery
from src.course.application.finder.find_course_query_handler import FindCourseQueryHandler
from src.course.domain.course_repository import CourseRepository
from src.course.infrastructure.sqlite_course_repository import SqliteCourseRepository
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.infrastructure.bus.memory_command_bus import MemoryCommandBus
from src.shared.infrastructure.bus.memory_query_bus import MemoryQueryBus


@implementation(CourseRepository)
def choose_course_repository():
    return SqliteCourseRepository


@implementation(CommandBus)
def choose_command_bus():
    return MemoryCommandBus


@implementation(QueryBus)
def choose_query_bus():
    return MemoryQueryBus


@inject
def register_commands(bus: CommandBus):
    bus.register(CreateCourseCommand, CreateCourseCommandHandler())


@inject
def register_queries(bus: QueryBus):
    bus.register(FindCourseQuery, FindCourseQueryHandler())
