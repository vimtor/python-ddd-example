from dataclasses import dataclass

from src.shared.domain.bus.query.query import Query


@dataclass
class FindCourseQuery(Query):
    course_id: str
