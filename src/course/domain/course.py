from dataclasses import dataclass

from src.course.domain.course_id import CourseId
from src.course.domain.course_title import CourseTitle


@dataclass
class Course:
    id: CourseId
    title: CourseTitle
