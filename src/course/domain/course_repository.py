from abc import ABC, abstractmethod

from src.course.domain.course import Course
from src.course.domain.course_id import CourseId


class CourseRepository(ABC):
    @abstractmethod
    def save(self, course: Course):
        pass

    @abstractmethod
    def find(self, id: CourseId) -> Course:
        pass
