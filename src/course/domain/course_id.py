from uuid import UUID

from src.shared.domain.value_object import ValueObject


class CourseId(ValueObject):
    def validate(self, value):
        try:
            UUID(value, version=4)
        except ValueError:
            raise ValueError('Invalid UUID for CourseId')
