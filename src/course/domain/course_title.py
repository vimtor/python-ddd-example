from src.shared.domain.value_object import ValueObject


class CourseTitle(ValueObject):
    def validate(self, value: str):
        if len(value) < 0:
            raise ValueError('Course title cannot be empty')
        if len(value) > 50:
            raise ValueError('Course title is too long')
